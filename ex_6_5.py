text = "X-DSPAM-Confidence:    0.8475"
zro = text.find('0')
print(float(text[zro:]))
