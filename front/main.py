from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/questao1', methods = ['GET'])
def inicial():
    request = requests.get("http://localhost:8080/link_pdf")
    resposta = json.loads(request.content)
    return "Bruno Mafra e Klaus Kupper" + resposta["link"]

if __name__ == '__main__':
    app.run(debug=True)
