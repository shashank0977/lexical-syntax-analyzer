from lexer.tokenizer import LexicalAnalyzer
from parser.grammar import Grammar
from parser.first_follow import FirstFollow
from parser.ll1_parser import LL1Parser


# ---------------- LEXER ----------------
def run_lexer():
    print("\nEnter source code:")
    code = input()

    lexer = LexicalAnalyzer()
    tokens = lexer.tokenize(code)

    print("\nGenerated Tokens:")
    for token in tokens:
        print(token)


# ---------------- BUILD GRAMMAR ----------------
def build_grammar():
    grammar = Grammar()

    n = int(input("How many productions? "))

    for _ in range(n):
        production = input("Enter production (Example: E -> T E'): ")
        left, right = production.split("->")
        left = left.strip()
        rules = [r.strip() for r in right.split("|")]
        grammar.add_production(left, rules)

    return grammar


# ---------------- SHOW GRAMMAR ----------------
def run_grammar():
    grammar = build_grammar()
    grammar.display_grammar()


# ---------------- FIRST SET ----------------
def run_first():
    grammar = build_grammar()

    ff = FirstFollow(grammar)
    ff.compute_first()
    ff.display_first()


# ---------------- FOLLOW SET ----------------
def run_follow():
    grammar = build_grammar()

    ff = FirstFollow(grammar)
    ff.compute_first()
    ff.compute_follow()
    ff.display_follow()


# ---------------- LL(1) PARSER ----------------
def run_parser():
    grammar = build_grammar()

    parser = LL1Parser(grammar)

    input_string = input("Enter input string (space separated tokens): ")
    parser.parse(input_string)


# ---------------- MAIN MENU ----------------
if __name__ == "__main__":
    while True:
        print("\n=== Lexical Syntax Analyzer ===")
        print("1. Run Lexical Analyzer")
        print("2. Enter Grammar")
        print("3. Compute FIRST set")
        print("4. Compute FOLLOW set")
        print("5. Run LL(1) Parser")
        print("6. Exit")

        choice = input("Select option: ")

        if choice == "1":
            run_lexer()

        elif choice == "2":
            run_grammar()

        elif choice == "3":
            run_first()

        elif choice == "4":
            run_follow()

        elif choice == "5":
            run_parser()

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Try again.")