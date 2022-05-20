from flask import Flask, redirect, url_for, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

index = 1

# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/img', methods=['POST'])
def img():
    global index
    file = request.files['img']

    extension = file.filename.split('.')[-1]
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'{mytime}'

    print(file, extension, filename)

    save_to = f'static/images/{str(index)}_{filename}.{extension}'
    file.save(save_to)

    return jsonify({'msg': '연결 완료'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)