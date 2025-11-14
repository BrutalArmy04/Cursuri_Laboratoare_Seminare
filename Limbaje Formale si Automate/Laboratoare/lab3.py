# a*b | (sau + sau reunit) (ab)*   
# RegEx: a) multimea vida, lambda, orice cuv din alfabet
# b) pt orice e1, e2 din RegEx => e1 + e2, e1 x e2 e din RegEx
# c) pt orice e din RegEx => e* e din RegEx

# 1. NFA -> RegEx: ab*ab*a

# 1) reunim tranzitiile de pe aceiasi sageata
# 2) verific statea initiala -> sa nu fie stare finala si sa nu aiba sageti catre ea 
# 3) verific starea finala -> sa fie unica finala si sa nu plece sageti din ea
# 4) eliminam pe rand fiecare stare care nu e initiala sau finala
# -> eliminam q1: adaug muche cu tot ce lega q1 (similar cu eliminarea lambdaurilor)    (ar trb folosit lambda stelat)
# daca obtinem 2 RegEx-uri de ex (qi, qj) reunesc tranzitii
# 5) Postprocesare RegEx (daca e cazul)

#2. RegEx -> NFA    a(a+b)*b    
# a: -> q0 -> q1 (final)
# b: -> q0 -> q1 (final)
# a + b -> q0 -> a -> q1 -> lambda -> q3 -> lambda -> q4
#             -> b -> q2 -> lambda -> q3
#           -> lambda -> q3
# folosim forma poloneza

