# unsolved
global p_AA, p_AB, p_BA, p_BB
global p_xA, p_yA, p_zA, p_xB, p_yB, p_zB

# transition probability
p_AA = 0.641
p_AB = 0.359
p_BA = 0.729
p_BB = 0.271

# emission probability
p_xA = 0.117
p_yA = 0.691
p_zA = 0.192
p_xB = 0.097
p_yB = 0.42
p_zB = 0.483

string = "xyxzzxyxyy"

def maximized_path(string):
    path = []
    current_observed = ""

    # 초기확률 결정
    if string[0] == "x":
        current_observed = max(["A","B"], key=lambda k: {"A":p_xA, "B":p_xB}[k])
        path.append(current_observed)
    elif string[0] == "y":
        current_observed = max(["A","B"], key=lambda k: {"A":p_yA, "B":p_yB}[k])
        path.append(current_observed)
    else:
        current_observed = max(["A","B"], key=lambda k: {"A":p_zA, "B":p_zB}[k])
        path.append(current_observed)

    for i in range(1, len(string)-1):
        if (string[i] == "x") and (current_observed == "A"):
            current_observed = max({"A", "B"}, key=lambda k :{"A":p_xA*p_AA, "B":p_xB*p_AB}[k])
            path.append(current_observed)
            i+=1
        elif (string[i] == "y") and (current_observed == "A"):
            current_observed = max({"A", "B"}, key=lambda k :{"A":p_yA*p_AA, "B":p_yB*p_AB}[k])
            path.append(current_observed)
            i+=1
        elif (string[i] == "z") and (current_observed == "A"):
            current_observed = max({"A", "B"}, key=lambda k :{"A":p_zA*p_AA, "B":p_zB*p_AB}[k])
            path.append(current_observed)
            i+=1
        elif (string[i] == "x") and (current_observed == "B"):
            current_observed = max({"A", "B"}, key=lambda k :{"A":p_xA*p_BA, "B":p_xB*p_BB}[k])
            path.append(current_observed)
            i+=1
        elif (string[i] == "y") and (current_observed == "B"):
            current_observed = max({"A", "B"}, key=lambda k :{"A":p_yA*p_BA, "B":p_yB*p_BB}[k])
            path.append(current_observed)
            i+=1
        elif (string[i] == "z") and (current_observed == "B"):
            current_observed = max({"A", "B"}, key=lambda k :{"A":p_zA*p_BA, "B":p_zB*p_BB}[k])
            path.append(current_observed)
            i+=1
    return path
        
if __name__ == "__main__":
    result = maximized_path(string)
    result = ''.join(result)
    print("%s" %result)

# 메모
# 현재 상태가 A고 그 다음이 y면?
# max(p(B|A)*p(B|y)), p(A|A)*p(A|y))