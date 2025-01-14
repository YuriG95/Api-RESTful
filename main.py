from flask import Flask,jsonify,request

# Criação do app Flask
app = Flask (__name__)

# Rota para validar o funcionamento da api
@app.route('/')
def home():
    return "Bem-vindo a minha API!"

# Rota Get
@app.route('/api/saudacao', methods=['GET'])
def saudacao():
     return jsonify({"mensagem":"Bem vindo"})

# Rota Rota Get com entrada de dados
@app.route('/api/saudacao/<nome>', methods=['GET'])
def saudacao_nome(nome):
    return jsonify({"mensagem": f"Olá, {nome}! Seja bem-vindo à minha API!"})

#Rota  teste Get
@app.route('/api/teste', methods=['GET'])
def teste():
    return jsonify({"mensagem":f"Teste aceito"})
    

# Rota qcom entrada de dados via POST e calcular as duas entradas ulltilizando uma soma
@app.route('/api/soma', methods=['POST'])
def soma():
    dados = request.get_json() #Receber as entradas de dados da Api
    num1 = dados.get('numero1')
    num2 = dados.get('numero2')
    if num1 is not None and num2 is not None:
        resultado = num1 + num2
        return jsonify({"resultado": resultado})
    else:
        return jsonify(
            {"erro": "Entrada'numero1' e 'numero2' são necessárias!"}), 400

# Rodando o servidor (modo local http://127.0.0.1:5000)
if __name__ =='__main__':
    app.run(debug=True)
