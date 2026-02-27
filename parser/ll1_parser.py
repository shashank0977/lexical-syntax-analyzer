class LL1Parser:

    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, input_string):
        # Start symbol = first production
        start_symbol = list(self.grammar.productions.keys())[0]

        stack = ["$", start_symbol]
        input_tokens = input_string.split() + ["$"]

        print("\nParsing Steps:")
        print("Stack\t\tInput")

        while stack:
            print(f"{stack}\t{input_tokens}")

            top = stack.pop()
            current = input_tokens[0]

            # If terminal match
            if top == current:
                input_tokens.pop()

            # If non-terminal
            elif top in self.grammar.productions:
                rules = self.grammar.productions[top]

                # Take first rule (simple LL(1))
                rule = rules[0]

                if rule != "ε":
                    symbols = rule.split()
                    for symbol in reversed(symbols):
                        stack.append(symbol)

            else:
                print("❌ Parsing Error")
                return False

            if top == "$" and current == "$":
                print("✅ String Accepted")
                return True

        print("❌ String Rejected")
        return False