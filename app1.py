from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html')


@app.route('/num1', methods=['POST'])
def button_click(num1, operation):
    if request.method == 'POST':
        operation = request.form['operation']
        num1 = request.form['numview'] 
        return render_template('app.html')


@app.route('/sum', methods=['POST'])
def send(operation, num1, num2, op):
    if request.method == 'POST':
        num2 = request.form['numview']
        operation = request.form['operation']

        if operation == 'add':
            sum = float(num1) + float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'subtract':
            sum = float(num1) - float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'divide':
            sum = float(num1) / float(num2)
            return render_template('app.html', sum=sum)
        else:
            return render_template('app.html')

if __name__ == ' __main__':
    app.debug = True
    app.run(host = '0.0.0.0')
