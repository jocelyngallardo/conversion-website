from flask import Flask, url_for, render_template

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('colors.html')

@app.route("/colors")
def render_response():
    response = returnColor(resquest.args['color'])
    return render_template('response.html', responseFromServer = response)

@app.route("/money")
def render_money():
    return render_template('money.html')

@app.route("/measurements")
def render_measurements():
    return render_template('measurements.html')
    
if __name__=="__colors__":
    app.run(debug=False)

def returnColor(english)
    if english = "red"
        return "rojo"
    if english = "orange"
        return "naranja"
    if english = "yellow"
        return "amarillo"
    if english = "green"
        return "verde"
    if english = "blue"
        return "azul"
    if english = "purple"
        return "morado"
