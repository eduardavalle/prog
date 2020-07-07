from config import *
from modelo_sapato import Sapato

@app.route("/")
def inicio():
    return 'Sistema de cadastro de sapatos. '+\
        '<a href="/listar_pessoas">Operação listar</a>'

@app.route("/listar_pessoas")
def listar_pessoas():
    sapato = db.session.query(Sapato).all()
    sapato_em_json = [ x.json() for x in sapato ]
    resposta = jsonify(sapato_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 
    

app.run(debug=True)

