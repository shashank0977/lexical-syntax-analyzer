class FirstFollow:

    def __init__(self, grammar):
        self.grammar = grammar
        self.first = {}
        self.follow = {}

    # ---------------- FIRST ----------------
    def compute_first(self):
        for non_terminal in self.grammar.productions:
            self.first[non_terminal] = set()

        changed = True

        while changed:
            changed = False

            for non_terminal in self.grammar.productions:
                for rule in self.grammar.productions[non_terminal]:
                    symbols = rule.split()
                    first_symbol = symbols[0]

                    # If terminal
                    if first_symbol.islower() or not first_symbol.isalpha():
                        if first_symbol not in self.first[non_terminal]:
                            self.first[non_terminal].add(first_symbol)
                            changed = True

                    # If non-terminal
                    elif first_symbol in self.grammar.productions:
                        before = len(self.first[non_terminal])
                        self.first[non_terminal].update(
                            self.first[first_symbol]
                        )
                        if len(self.first[non_terminal]) > before:
                            changed = True

        return self.first

    def display_first(self):
        print("\nFIRST Sets:")
        for non_terminal in self.first:
            print(f"FIRST({non_terminal}) = {self.first[non_terminal]}")

    # ---------------- FOLLOW ----------------
    def compute_follow(self):
        for non_terminal in self.grammar.productions:
            self.follow[non_terminal] = set()

        # Add $ to start symbol
        start_symbol = list(self.grammar.productions.keys())[0]
        self.follow[start_symbol].add("$")

        changed = True

        while changed:
            changed = False

            for lhs in self.grammar.productions:
                for rule in self.grammar.productions[lhs]:
                    symbols = rule.split()

                    for i in range(len(symbols)):
                        symbol = symbols[i]

                        if symbol in self.grammar.productions:
                            # If not last symbol
                            if i + 1 < len(symbols):
                                next_symbol = symbols[i + 1]

                                if next_symbol not in self.grammar.productions:
                                    if next_symbol not in self.follow[symbol]:
                                        self.follow[symbol].add(next_symbol)
                                        changed = True
                                else:
                                    before = len(self.follow[symbol])
                                    self.follow[symbol].update(
                                        self.first[next_symbol]
                                    )
                                    if len(self.follow[symbol]) > before:
                                        changed = True

                            # If last symbol
                            else:
                                before = len(self.follow[symbol])
                                self.follow[symbol].update(self.follow[lhs])
                                if len(self.follow[symbol]) > before:
                                    changed = True

        return self.follow

    def display_follow(self):
        print("\nFOLLOW Sets:")
        for non_terminal in self.follow:
            print(f"FOLLOW({non_terminal}) = {self.follow[non_terminal]}")