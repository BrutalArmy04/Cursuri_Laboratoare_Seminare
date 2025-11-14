s = "o zi frumoasa!"
new_s = ""
k = 9
for letter in s:
    if letter.isalpha() == False:
        new_s += letter
    else:
        if letter.islower() == True:
            x = ord(letter)
            x -= k 
            #x += k
            if x<ord('a'): 
            #if x>ord('z'):
                x += ord('z') - ord('a') + 1
        else:
            x = ord(letter)
            x -= k  
            #x += k
            if x<ord('A'): 
            #if x>ord('Z'):
              x += ord('Z') - ord('A') + 1
        new_s += chr(x)
#print(new_s)
lung = ord('z') - ord('a') + 1
L = [(chr((ord(c) - ord('a') + k )% lung + ord('a'))if c.isalpha() else c) for c in s]
prop2 = ''.join(L)
print(prop2)