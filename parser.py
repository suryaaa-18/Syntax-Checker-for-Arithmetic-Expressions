class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def error(self):
        raise SyntaxError("Invalid Syntax")

    def eat(self, token_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == token_type:
            self.pos += 1
        else:
            self.error()

    def parse(self):
        self.expr()
        if self.pos != len(self.tokens):
            self.error()
        return True

    def expr(self):
        self.term()
        while self.pos < len(self.tokens) and self.tokens[self.pos][1] in ('+', '-'):
            self.eat('OP')
            self.term()

    def term(self):
        self.factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos][1] in ('*', '/'):
            self.eat('OP')
            self.factor()

    def factor(self):
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]

            if token[1] in ('+', '-'):
                self.eat('OP')
                self.factor()
            elif token[0] == 'NUMBER' or token[0] == 'ID':
                self.eat(token[0])
            elif token[0] == 'LPAREN':
                self.eat('LPAREN')
                self.expr()
                self.eat('RPAREN')
            else:
                self.error()
        else:
            self.error()