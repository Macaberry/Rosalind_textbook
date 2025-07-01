# Compute the Number of Times a Pattern Appears in a Text

def PatternCount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern)):
        if text[i:i+len(pattern)-1] == pattern:
            count += 1
    return count

text = "GCGCG"
pattern = "GCG"

result = PatternCount(text, pattern)
print(result)