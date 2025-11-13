from re import search

def parola(sir):
    a = search(r"^[a-z]{1-5}$", sir)
    A = search(r"^[A-Z]{1-5}$", sir)
    c = search(r"^[0-9]{1-5}$", sir)
    print(a, A, c, sep = "\n")
    if a or A or c:
        print(f"parola {sir} este slaba")
#parola("34")
    
