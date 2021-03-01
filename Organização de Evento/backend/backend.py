from config import *
from model import Pessoa, Sala, EspacoCafe

@app.route("/")
def padrao():
    return "Teste"


#Lisatgens#

@app.route("/listar_pessoas")
def listar_pessoas():
    p = db.session.query(Pessoa).all()
    p_js = [Pessoa.json() for Pessoa in p]
    return (jsonify(p_js))

@app.route("/listar_salas")
def listar_salas():
    salas = db.session.query(Sala).all()
    salas_js = [s.json() for s in salas]
    resp = jsonify(salas_js)
    resp.headers.add("Access-Control-Allow-Origin", "*") 
    return resp

@app.route("/listar_cafe")
def listar_cafe():
    cafe = db.session.query(EspacoCafe).all()
    cafe_js = [c.json() for c in cafe]
    resp = jsonify(cafe_js)
    resp.headers.add("Access-Control-Allow-Origin", "*") 
    return resp


#Cadastrar pessoa
@app.route("/cadastrar_pessoa", methods=['POST'])
def cadastar_Pessoa():
    resp = jsonify({"resultado":"ok","detalhes": "ok"})
    
    dados = request.get_json()
    try:      
        nova_p = Pessoa(**dados)
        db.session.add(nova_p)
        
        add_p_sala(nova_Pessoa.sala_1_id,nova_Pessoa.id_pessoa,1)
        add_p_cafe(nova_Pessoa.ecafe_1_id,nova_Pessoa.id_pessoa,1)
        
        db.session.commit()   
    
    except Exception as x: 
        resposta = jsonify({"resultado":"erro","detalhes":str(x)})
        
    resp.headers.add("Access-Control-Allow-Origin","*")
    
    
    return resp

#Cadastrar salas
@app.route("/cadastrar_sala", methods=['POST'])
def cadastrar_sala():
    
    resp = jsonify({"resultado":"ok","detalhes": "ok"})
    dados = request.get_json()
    
    try:        
        nova_Sala = Sala(**dados)
        db.session.add(nova_Sala)
        dividir_pessoas()
        db.session.commit()
        
    except Exception as x: 
        resposta = jsonify({"resultado":"erro","detalhes":str(x)})
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    
    return resp

#Cadastrar espaços café
@app.route("/cadastrar_Ecafe", methods=['POST'])
def cadastrar_Ecafe():
    
    resp = jsonify({"resultado":"ok","detalhes": "ok"})
    dados = request.get_json()
    try:
        novoEspaco = EspacoCafe(**dados)
        db.session.add(novoEspaco)
        db.session.commit()
            
    except Exception as x: 
        resposta = jsonify({"resultado":"erro","detalhes":str(x)})
            
    resp.headers.add("Access-Control-Allow-Origin","*")
    
    return resp


