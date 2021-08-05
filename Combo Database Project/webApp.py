from flask import Flask, render_template, request, redirect
from PythonSQL import *
app = Flask(__name__)


@app.route('/')
def testing():
    return render_template("home.html")

@app.route("/submit_combo", methods=["GET", "POST"])
def submit_combo():
    if request.method == "POST":
        req = request.form
        #print(req)
        gameV = req.get("gameSelected")
        char_nameV = req.get("charSelected")
        comboV  = req.get("Combo")
        positionV  = req.get("Position")
        damageV  = req.get("Damage")
        meterV  = req.get("Meter")
        difficultyV = req.get("Difficulty")
        notesV = req.get("Notes")

        missing = list()

        for k, v in req.items():
            if v =="":
                missing.append(k)
        
        if missing:
            feedback = f"Missing fields for {'. '.join(missing)}"
            return render_template("/submit_combo", feedback=feedback)
        
        #print(gameV)
        #print(comboV)
        


        if gameV != None and char_nameV != None and comboV != None:
            call_insert_combo(gameV, char_nameV, comboV, positionV, damageV, meterV, difficultyV, notesV)		

        #TODO: Else show user error message 

        return redirect(request.url)

    return render_template("submit_combo.html")


@app.route('/test2')
def testing2():
    return render_template("test2.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)