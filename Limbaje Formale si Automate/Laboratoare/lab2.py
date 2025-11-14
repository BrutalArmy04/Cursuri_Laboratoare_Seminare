# lambda-NFA care modeleaza traseul unui robor intr-o fabrica
# f(ollow) path
# d(etect) obstacle
# p(ick) object
# r(otate) to dock
# v(alidate) object
# e(rror)
# q0: dock
# q1: hall A
# q2: hall B
# q3: hall C
# q4: packing zone
# q5 CP
# q6: finalize task

#calculam lambda inchideri pt fiecare stare -> luam in calcul toate literele din alfabet + lambda transitii
# luam fiecare stare existenta si adaugam o noua stare pt tranzitii daca lambda-inchiderea != dictionarul de tranzitii

class LambdaNFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}
        self.alphabet = {'f', 'd', 'p', 'r', 'v', 'e', 'lambda'}
        self.transitions = {
            'q0': {'f': {'q1'}, 'lambda': {'q2', 'q3'}},
            'q1': {'f': {'q2'}, 'lambda': {'q4'}, 'd': {'q3'}},
            'q2': {'f': {'q3', 'q5'}, 'p': {'q4'}},
            'q3': {'f': {'q4', 'q2'}, 'd': {'q5'}},
            'q4': {'f': {'q5'}, 'r': {'q0'}, 'p': {'q6'}},
            'q5': {'v': {'q6'}, 'e': {'q1', 'q3'}},
            'q6': {'lambda': {'q0'}, 'v': {'q4'}}
        }
        self.initial_state = 'q0'
        self.final_states = {'q6'}

    def remove_lambdas(self):
        lambda_closures = {state: set() for state in self.states}
        for state in self.states:
            lambda_closures[state].add(state)  
            if 'lambda' in self.transitions.get(state, {}):
                stack = list(self.transitions[state]['lambda']) # nu stiu daca era mai bn sa dau import la stack, am auzit la colegi ca asa au facut
                while stack:
                    next_state = stack.pop()
                    if next_state not in lambda_closures[state]:
                        lambda_closures[state].add(next_state)
                        if 'lambda' in self.transitions.get(next_state, {}):
                            stack.extend(self.transitions[next_state]['lambda'])

        new_transitions = {state: {} for state in self.states}
        
        for state in self.states:
            for reachable in lambda_closures[state]:
                if reachable in self.transitions:
                    for symbol, destinations in self.transitions[reachable].items():
                        if symbol != 'lambda':  
                            if symbol not in new_transitions[state]:
                                new_transitions[state][symbol] = set()
                            new_transitions[state][symbol].update(destinations)

        new_final_states = set(self.final_states)
        for state in self.states:
            if any(f in self.final_states for f in lambda_closures[state]):
                new_final_states.add(state)

        self.transitions = new_transitions
        self.final_states = new_final_states

        print("Lambda transitions removed.")
        print("New transitions:", self.transitions)
        print("New final states:", self.final_states)


if __name__ == '__main__':
    A = LambdaNFA()
    A.remove_lambdas()



    