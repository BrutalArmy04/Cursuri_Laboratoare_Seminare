s = "Ana are mere"
prop2 = "".join([f'{c}p{c}' if c in "aeoiuAEIOU" else c for c in s])
print(prop2)