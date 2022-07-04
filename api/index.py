from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/link_pdf', methods = ['GET'])
def link_pdf():
    dicionario = {'link':'http://127.0.0.1:8080/get_pdf'}
    return jsonify(dicionario)

@app.route('/get_pdf/',methods = ['GET','POST'])
def get_files():
    return send_from_directory("./","teste.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
