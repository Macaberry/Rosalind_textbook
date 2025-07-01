# Compute the Probability of a String emitted by an HMM
# Outcome likelihood problem
# Pr(x) that the HMM emits the string x

str = "xzyyzzyzyy"

# AABB transision matrix
tran_matrix = [0.303, 0.697, 
               0.831, 0.169]
p_aa = tran_matrix[0]
p_ab = tran_matrix[1]
p_ba = tran_matrix[2]
p_bb = tran_matrix[3]

# AB to zyx emission matrix
emi_matrix = [0.533, 0.065, 0.402,
              0.342, 0.334, 0.324]
p_ax = emi_matrix[0]
p_ay = emi_matrix[1]
p_az = emi_matrix[2]
p_bx = emi_matrix[3]
p_by = emi_matrix[4]
p_bz = emi_matrix[5]

def tran_compute(current,previous):
    if (current == "A") & (previous == "A"):
        return p_aa
    elif (current == "A") & (previous == "B"):
        return p_ba
    elif (current == "B") & (previous == "A"):
        return p_ab
    elif (current == "B") & (previous == "B"):
        return p_bb
    else:
        print("Wrong input")

def compute(chr):
    prev_state = ""

    if chr == "x":
        """
        P(x|A)-P(A|A)-P(...)
        P(x|B)-P(B|A)-P(...)
        x-B-pA
        x-B-pB
        """
        return p_ax * tran_compute("A", prev_state)
    elif chr == "y":
        return 
    elif chr == "z":
        return 
    
def probability(str):
    for i in (-1, -len(str)):
        if str[i] == "x":
            return p_ax * compute(str[i])


for i in (1, len(str)-1):
    previous = str[-i]
    current = str[-i]

print(f"{result:e}")

"""
Recursive function example:
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)
"""