class DFAtoCFGConverter:
    # Definim starile din DFA si viitoarele stari din CFG
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions  
        self.initial_state = initial_state
        self.final_states = final_states
        self.variables = set()
        self.terminals = alphabet
        self.start_symbol = None
        self.productions = []
    
    def state_to_variable(self, state):
        # Starea o sa o scriu cu S_ prefix pentru a o face variabila in CFG
        return f"S_{state}"
    
    def convert(self):
        # Creez variabile pentru stari
        for state in self.states:
            var = self.state_to_variable(state)
            self.variables.add(var)
            # Setez startul
            if state == self.initial_state:
                self.start_symbol = var
        # Adaug productiile pentru tranzitii
        for (state, symbol), next_state in self.transitions.items():
            lhs = self.state_to_variable(state)
            rhs = [symbol, self.state_to_variable(next_state)]
            self.productions.append((lhs, rhs))
        # Adaug epsilon productiile pentru starile finale
        for final_state in self.final_states:
            lhs = self.state_to_variable(final_state)
            self.productions.append((lhs, [])) 
        
        return self
    
    def print_grammar(self):
        print("\nGenerated Context-Free Grammar:")
        print(f"Variables: {self.variables}")
        print(f"Terminals: {self.terminals}")
        print(f"Start Symbol: {self.start_symbol}")
        print("Production Rules:")
        for lhs, rhs in self.productions:
            rhs_str = ''.join(rhs) if rhs else 'epsilon'
            print(f"{lhs} → {rhs_str}")

states = {'s', 'd', 'e'}
alphabet = {'0', '1'}
transitions = {
    ('s', '0'): 'e',
    ('s', '1'): 'd',
    ('d', '0'): 'e',
    ('d', '1'): 'd',
    ('e', '0'): 'e',
    ('e', '1'): 'd',
}
initial_state = 's'
final_states = {'e'}
dfa_cfg_converter = DFAtoCFGConverter(
    states, alphabet, transitions, initial_state, final_states
).convert()

dfa_cfg_converter.print_grammar()


print("\nTest Case 2: Strings ending with 'b'")
states = {'q0', 'q1'}
alphabet = {'a', 'b'}
transitions = {
    ('q0', 'a'): 'q0',
    ('q0', 'b'): 'q1',
    ('q1', 'a'): 'q0',
    ('q1', 'b'): 'q1',
}
initial_state = 'q0'
final_states = {'q1'}

dfa_cfg_converter = DFAtoCFGConverter(
    states, alphabet, transitions, initial_state, final_states
).convert()

dfa_cfg_converter.print_grammar()