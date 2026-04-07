print("THIS IS FLASK VERSION")
from flask import Flask, render_template, request
from tokenizer import tokenize
from parser import Parser

app = Flask(__name__)

# -------- CHECK FUNCTION --------
def check_syntax(expression):
    tokens = tokenize(expression)
    parser = Parser(tokens)
    parser.parse()
    return tokens


# -------- ROUTE --------
@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    tokens = None
    expr = ""

    if request.method == 'POST':
        expr = request.form['expression']

        try:
            tokens = check_syntax(expr)
            result = "✅ Valid Expression"
        except Exception as e:
            result = f"❌ Invalid Expression: {e}"

    return render_template(
        'index.html',
        result=result,
        tokens=tokens,
        expression=expr
    )


# -------- RUN APP --------
if __name__ == '__main__':
    print("🚀 Flask Syntax Checker Running...")
    app.run(debug=True)