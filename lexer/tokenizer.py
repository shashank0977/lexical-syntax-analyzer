import re

class LexicalAnalyzer:

    def __init__(self):
        # Token patterns (your language rules)
        self.token_patterns = [
            ("KEYWORD", r"\b(if|else|while|int|float|return)\b"),
            ("IDENTIFIER", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
            ("NUMBER", r"\b\d+\b"),
            ("OPERATOR", r"[+\-*/=]"),
            ("SEPARATOR", r"[();{}]"),
            ("WHITESPACE", r"\s+")
        ]

    def tokenize(self, source_code):
        tokens = []
        position = 0

        while position < len(source_code):
            match = None

            for token_type, pattern in self.token_patterns:
                regex = re.compile(pattern)
                match = regex.match(source_code, position)

                if match:
                    if token_type != "WHITESPACE":
                        tokens.append({
                            "type": token_type,
                            "value": match.group()
                        })
                    position = match.end()
                    break

            if not match:
                raise Exception(f"Invalid character: {source_code[position]}")

        return tokens