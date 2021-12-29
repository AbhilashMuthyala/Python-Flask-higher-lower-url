from flask import Flask
import random

app = Flask(__name__)

rand_num = random.randint(1,9)

print(rand_num)

@app.route('/')
def start():
    return '<h1>Guess a number between 0 and 9</h1>'

@app.route("/<int:num>")
def guess_num(num):
    if num == rand_num:
        return "<h1>You found me</h1>"
    elif num < rand_num:
        return "<h1>number is too low</h1>"
    else:
        return "<h1>number is too high</h1>"

if __name__ == '__main__':
    app.run(debug=True)
