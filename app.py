from flask import Flask, jsonify, send_from_directory, request, redirect
from logging import warning

app = Flask(__name__)



@app.route('/page/<path:path>', methods=['GET'])
def page(path):
    return send_from_directory('static', path)


@app.route('/page/login.html', methods=['POST'])
def loadin():
    login = request.form.get('exampleInputEmail1', 'noname')
    pwd = request.form.get('exampleInputPassword1', 'pwd')

    if (login, pwd) == ('Lisin@gmail.com', '1234'):
        return redirect('/page/name.html')
    else:
        return redirect('/page/login.html')


# @app.route('/', methods=['GET'])
# def hmtl():
#     return """
#     <html>
#     <body>
#     <h1>BOT BLUN</h1>
#     </body>
#     </html>
#     """


# @app.route('/', methods=['GET'])
# def hi_with_json():
#     return jsonify({'msg': 'hi', 'data': data})
#
#
# @app.route('/', methods=['POST'])
# def login():
#     name = request.args.get('username', 'noname')
#     pwd = request.args.get('pass', '***')
#     try:
#         body = json.loads(request.data)
#     except Exception as e:
#         body = {'error': 'error'}
#     return jsonify({'your_name': name, 'pass': pwd, "data": body})