from flask import Flask, url_for, render_template

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/colors")
def render_colors():
    return render_template('colors.html')

@app.route("/money")
def render_page1():
    return render_template('money.html')

@app.route("/measurements")
def render_measurements():
    return render_template('measurements.html')
    
if __name__=="__colors__":
    app.run(debug=False)
