#ex 1

# DFA: L = {w|w contine nr par de 0-uri si nr impar de 1-uri}
# stari : {q1, q2, q3, q4}
# alfabet : {0, 1}
# stare initiala : q1
# q1: {0:q2, 1:q3}
# stare finala: q3
# pt fiecare litera din input vedem starea actuala, modificam stea in functie de litera citita
# ne oprim cand se termina inputul sau nu ajungem la o stare finala
# daca ajungem la o stare finala inseamna ca cuvantul este acceptat daca nu este respins

class DFA:
    def __init__(self):
    #definim starile
        self.states = ['q1', 'q2', 'q3', 'q4']
        self.alphabet = ['0', '1']
        self.initial_state = 'q1'
        self.final_states = ['q3']
        self.transitions = {
            'q1': {'0': 'q2', '1': 'q3'},
            'q2': {'0': 'q1', '1': 'q4'},
            'q3': {'0': 'q4', '1': 'q1'},
            'q4': {'0': 'q3', '1': 'q2'}
        }

    def process_string(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            current_state = self.transitions[current_state][symbol]
        return current_state in self.final_states
if __name__ == '__main__':
    dfa = DFA()
    test_strings = ['0', '1', '01', '10', '11', '00', '001', '010', '101', '110', '111', '000']
    for test_string in test_strings:
        result = dfa.process_string(test_string)
        print(f'{test_string} is accepted: {result}')

#ex 2
# NFA: L = {w|w se termina in '10' sau '01'}. Transformam NFA in DFA

class NFA:
    def __init__(self):
        self.states = ['q1', 'q2', 'q3', 'q4']
        self.alphabet = ['0', '1']
        self.initial_state = 'q0'
        self.final_states = ['q3', 'q4']
        self.transitions = {
            'q0' : {'0': ('q1', 'q0'), '1': ('q0', 'q2')},
            'q2' : {'1': ('q3')}, 
            'q3' : {},
            'q4' : {'0': ('q3')}
            }
    
    def process_string(self, input_string):
        current_states = {self.initial_state} 
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False  
            next_states = set()  # Următoarele stări posibile
            for state in current_states:
                if state in self.transitions and symbol in self.transitions[state]:
                    next_states.update(self.transitions[state][symbol])
            current_states = next_states 
        for var in current_states:
            if var in self.final_states:
                return True
            else:
                return False
            
       
            
if __name__ == '__main__':
    nfa = NFA()
    test_strings = ['0', '1', '01', '10', '11', '00', '001', '010', '101', '110', '111', '000']
    for test_string in test_strings:
        result = nfa.process_string(test_string)
        print(f'{test_string} is accepted: {result}')
