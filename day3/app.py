import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route("/hi")
def hi():
    return render_template('hi.html')

# variable routing! 경로를 변수로 활용한다.
@app.route("/hi<string:name>")
def higyo(name):
    return render_template('hi2.html', namee=name)

# /cube/<숫자>
# 세제곱 결과를 보여주는 페이지!
@app.route("/cube<int:num>")
def cube(num):
    return f'{num}의 세제곱은 {num**3}'

# /lunch/사람이름
# 점심메뉴 추천해주는 페이지
@app.route("/lunch<string:name>")
def lunch(name):
    food = random.choice(['한식','특식A','특식B','굶어'])
    return render_template('lunch.html', foods=food, namee=name)

# /lotto
# 로또 번호 6개를 추천해주는 페이지
@app.route("/lotto")
def lotto():
    numbers = sorted(random.sample(range(1, 46),6))
    return f'이번주 당첨번호는 {numbers} !!'

if __name__ == '__main__':
    # python app.py 를 하면 아래의 코드 블록을 실행시킨다.
    app.run(debug=True)