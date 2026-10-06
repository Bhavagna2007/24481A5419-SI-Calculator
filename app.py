from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/greet/<uname>')
def greet(uname):
    return f"Good Morning, {uname}!"


@app.route('/delete/<int:roll>')
def delete(roll):
    return f"Deleting record with rollno {roll}"


@app.route('/calculator', methods=['GET', 'POST'])
def simple_interest():

    if request.method == 'POST':
        P = float(request.form['p'])
        T = float(request.form['t'])
        R = float(request.form['r'])

        simple_interest = (P * T * R) / 100
        total_amount = P + simple_interest

        return render_template(
            'result.html',
            Si=simple_interest,
            total=total_amount
        )

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=3500)