class Grammar:
    def __init__(self):
        self.productions = {}

    def add_production(self, non_terminal, rules):
        if non_terminal not in self.productions:
            self.productions[non_terminal] = []

        self.productions[non_terminal].extend(rules)

    def display_grammar(self):
        print("\nGrammar Rules:")
        for non_terminal in self.productions:
            rules = " | ".join(self.productions[non_terminal])
            print(f"{non_terminal} -> {rules}")