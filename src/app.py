from flask import Flask , request , jsonify

app = Flask(__name__)

#genero ruta mediante un post
@app.route('/ping' , methods=['POST'])

def ping():
    #leo datos y convierto a json
    data = request.get_json();
    
    #genero una condicion para saber si el contenido del json es 
    #ping para luego responder ping
    
    #jsonify -> convertir datos en diccionarios
    
    if data and data.get('data') == 'ping':
        return jsonify({'response': 'Pong'}),200
    else:
        #valido si el imput es valido o no
        return jsonify({'error': 'Input Inválido'}),400
    
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)