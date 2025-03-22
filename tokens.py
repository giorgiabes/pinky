class Token:
    def __init__(self, token_type, lexem) -> None:
        self.token_type = token_type
        self.lexem = lexem

        def __repr__(self):
            return f"({self.token_type}, {self.lexem!r})"
