class PushdownAutomata:
    def __init__(self):
        #am definit componentele PDA care recunoaste limbajul L = {0^n1^n | n >= 0}
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.input_alphabet = {'0', '1'}
        self.stack_alphabet = {'$', '0'}
        self.initial_state = 'q0'
        self.initial_stack_symbol = '$'
        self.final_states = {'q3'}
        self.transitions = {
            # Cele 5 tranzitii ale PDA-ului
            ('q0', '0', '$'): ('q1', ['0', '$']),  
            ('q1', '0', '0'): ('q1', ['0', '0']),  
            ('q1', '1', '0'): ('q2', []),          
            ('q2', '1', '0'): ('q2', []),          
            ('q2', '', '$'): ('q3', ['$']),        
        }
    def accept(self, input_string):
        # Incepem cu starea initiala si cu stiva goala
        current_state = self.initial_state
        stack = [self.initial_stack_symbol]
        input_ptr = 0
        while True:
            # Luăm elementul curent
            current_input = input_string[input_ptr] if input_ptr < len(input_string) else ''
            # Vedem daca avem o tranzitie
            transition_key = (current_state, current_input, stack[-1])
            if transition_key in self.transitions:
                # Aplicam tranzitia
                new_state, stack_operation = self.transitions[transition_key]
                # Updatam starea
                current_state = new_state
                # Updatam stiva
                stack.pop() 
                for symbol in reversed(stack_operation): 
                    stack.append(symbol)
                # Avansam in input daca am folosit un simbol
                if current_input != '':
                    input_ptr += 1
            else:
                # Nu avem tranzitie, deci verificam daca suntem in starea finala
                if current_state in self.final_states and input_ptr >= len(input_string):
                    return True
                else:
                    return False
            # Verificam daca am ajuns la finalul inputului si suntem in starea finala
            if input_ptr >= len(input_string) and current_state in self.final_states:
                return True

pda = PushdownAutomata()

test_cases = [
    ("01", True),
    ("0011", True),
    ("000111", True),
    ("1", False),
    ("10", False),
    ("001", False),
    ("00111", False),
    ("00", False),
    ("", False),
]

for input_str, expected in test_cases:
    result = pda.accept(input_str)
    print(f"Input: '{input_str}'\tExpected: {expected}\tResult: {result}")