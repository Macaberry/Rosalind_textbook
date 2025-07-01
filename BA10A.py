# solved
# Probability of a hidden path problem

# transition rate
p_aa = 0.456
p_ab = 0.544
p_ba = 0.763
p_bb = 0.237

input = "BBABAAAABBAABABBABBABABBBAAABABBAAAABABAAABBABABBA" # input sequence

def prob_hidden_path(input):
    p = 0.5
    for i in range(len(input) - 1):
        if input[i] == 'A':
            if input[i + 1] == 'A': # A to A
                p *= p_aa
            else: # A to B
                p *= p_ab
        else:
            if input[i + 1] == 'A': # B to A
                p *= p_ba
            else: # B to B
                p *= p_bb
    return p

result = prob_hidden_path(input)
print(f"{result:e}")