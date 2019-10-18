from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('colors.html')

@app.route("/response")
def render_response():
    response = returnColor(request.args['color'])
    return render_template('response.html', responseFromServer = response)

@app.route("/measurements")
def render_measurements():
    if "inches" in request.args:
        inches = float(request.args['inches'])
        response = str( inches * 2.54) + "centimeters"
        return render_template('response.html', responseFromServer = response)
    else:
        return render_template('measurements.html')

@app.route("/money")
def render_money():
    return render_template('money.html')

@app.route("/response")
def render_response():
    return render_template('response.html', responseFromServer = response)
    
if __name__=="__colors__":
    app.run(debug=False)

def returnColor(english):
    if english == "red":
        return "Rojo"
    if english == "orange":
        return "Naranja"
    if english == "yellow":
        return "Amarillo"
    if english == "green":
        return "Verde"
    if english == "blue":
        return "Azul"
    if english == "purple":
        return "Morado"
