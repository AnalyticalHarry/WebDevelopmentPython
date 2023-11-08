from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if operation == 'add':
            result = float(num1) + float(num2)
        elif operation == 'subtract':
            result = float(num1) - float(num2)
        elif operation == 'multiply':
            result = float(num1) * float(num2)
        elif operation == 'divide':
            if num2 == '0':
                result = 'Error: Division by zero'
            else:
                result = float(num1) / float(num2)

        return f"The result is: {result}"

if __name__ == '__main__':
    app.run(debug=True)
