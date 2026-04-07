import re

def tokenize(expression):
    tokens = []
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),
        ('ID',       r'[A-Za-z]+'),
        ('OP',       r'[+\-*/]'),
        ('LPAREN',   r'\('),
        ('RPAREN',   r'\)'),
        ('SKIP',     r'[ \t]+'),
        ('MISMATCH', r'.'),
    ]

    tok_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_specification)

    for match in re.finditer(tok_regex, expression):
        kind = match.lastgroup
        value = match.group()

        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f'Unexpected character: {value}')
        else:
            tokens.append((kind, value))

    return tokens