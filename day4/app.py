# 0. flask 패키지 에서 Flask, render_template 가져오기
from flask import Flask, render_template

# 1. app 설정
app = Flask(__name__)

# 2. 요청 경로(route) + 함수 만들기
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello<string:name>')
def hello(name):
    return render_template('hello.html', namee = name)
    
if __name__ == '__main__':
    app.run(debug=True)

