# Extract number from the following string
text = "X-DSPAM-Confidence:    0.8475";
start = text.find("0")
print text[start:len(text)]