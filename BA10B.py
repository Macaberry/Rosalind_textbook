# solved
observed = "xzyxxyzyxxzyxxyzxyyzyyxyzxxzxxyxxxxxxxyyyxzyxzzzzz"
hidden_path = "ABABBAAAAAAABAABAABAABBBBBBBBBBBBAAAABBABABAABABAA"

#emission matrix
p_x2A = 0.141
p_y2A = 0.481
p_z2A = 0.378
p_x2B = 0.306 
p_y2B = 0.331
p_z2B = 0.363

def cdt_prob(observed, hidden_path):
    p=1.0
    for i in range(len(observed)):
        if hidden_path[i] == "A":
            if observed[i] == "x":
                p*= p_x2A
            elif observed[i] == "y":
                p*= p_y2A
            else: p*= p_z2A
        else:
            if observed[i] == "x":
                p*= p_x2B
            elif observed[i] == "y":
                p*= p_y2B
            else: p*= p_z2B
    return p


result = cdt_prob(observed, hidden_path)
print("%e" %result)