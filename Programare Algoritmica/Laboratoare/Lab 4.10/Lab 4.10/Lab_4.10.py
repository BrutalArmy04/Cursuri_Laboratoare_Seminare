sir = "abcde"
L = [sir[:i] + sir[i:] for i in range(len(sir))]
print(L)
