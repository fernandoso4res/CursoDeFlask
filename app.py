from flask import Flask, render_template, request

app = Flask(__name__) #parametro de execução

frutas = []	
registros = []


#http://google.com/search?q=bcyrvca

@app.route('/', methods=["GET", "POST"])
def principal():
	#frutas = ["Morango", "Laranja", "Uva", "Mamão", "Pera", "Abacaxi", "Melancia", "Melão"]

	if request.method == "POST":
		if request.form.get("fruta"):
			frutas.append(request.form.get("fruta"))
	return render_template("index.html", frutas=frutas)

@app.route('/sobre', methods=["GET", "POST"])
def sobre():
	#notas = {"Fulano": 5.0, "Ciclano": 7.0, "Beltrano": 8.5, "Rodrigo": 5.5}
	if request.method == "POST":
		if request.form.get("aluno") and request.form.get("nota"):	
			registros.append({"aluno": request.form.get("aluno"), "nota":request.form.get("nota")})
	return render_template("sobre.html", registros=registros)

if __name__ =="__main__":
	app.run(debug=True)

#http://127.0.0.1:5000