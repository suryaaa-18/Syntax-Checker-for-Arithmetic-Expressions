# 🔍 Syntax Checker for Arithmetic Expressions

## 📌 Project Overview

This project is a **Syntax Checker for Arithmetic Expressions** developed using concepts from **Compiler Design**. It verifies whether a given arithmetic expression is syntactically correct based on predefined grammar rules.

The system performs two major phases of a compiler:

* **Lexical Analysis (Tokenization)**
* **Syntax Analysis (Parsing)**

Additionally, the project is extended into a **web application** using Flask for better user interaction.

---

## 🎯 Objectives

* To implement core compiler design concepts
* To check the syntax of arithmetic expressions
* To demonstrate lexical and syntax analysis
* To provide a simple web-based interface for user input

---

## ⚙️ Technologies Used

* **Python** – Core programming language
* **Flask** – Web framework for backend
* **HTML** – Structure of the web page
* **CSS** – Styling the UI

---

## 🧠 Concepts Used

* Context-Free Grammar (CFG)
* Recursive Descent Parsing
* Tokenization
* Syntax Checking

---

## 📜 Grammar Used

The following grammar is used to validate expressions:

```
E → E + T | E - T | T  
T → T * F | T / F | F  
F → (E) | id | number
```

---

## 🚀 Features

* Checks whether an expression is **Valid or Invalid**
* Supports operators: `+`, `-`, `*`, `/`
* Handles parentheses `()`
* Displays tokens generated during lexical analysis
* Provides error messages for invalid syntax
* User-friendly web interface

---

## 🗂️ Project Structure

```
syntax-checker/
│── main.py
│── parser.py
│── tokenizer.py
│── templates/
│     └── index.html
│── static/
│     └── style.css
│── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```
git clone <your-repo-link>
cd syntax-checker
```

### 2. Install Dependencies

```
pip install flask
```

### 3. Run the Application

```
python main.py
```

### 4. Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🧪 Example Test Cases

### ✅ Valid Expressions

```
a + b
a + b * (c - 2)
( x + y ) * z
```

### ❌ Invalid Expressions

```
a + * b
(a + b
a + / b
```

---

## ❗ Limitations

* Only performs syntax checking
* Does not evaluate expressions
* Limited to basic arithmetic operators

---

## 🚀 Future Enhancements

* Add expression evaluation
* Implement semantic analysis
* Add parse tree visualization
* Improve UI/UX design

---

## 🎓 Academic Use

This project is developed as part of a **Compiler Design academic project** to demonstrate understanding of parsing techniques and grammar validation.

---

## 👨‍💻 Author

* Your Name

---

## ⭐ Acknowledgement

This project is built for educational purposes to understand the fundamentals of compiler design.

---
