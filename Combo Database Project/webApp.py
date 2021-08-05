from flask import Flask, render_template, request, redirect, flash
from PythonSQL import *
app = Flask(__name__)
app.secret_key = "BX\xbe\x0f\xbe\xc4@\xd8K\xd6P\xc7"

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

        # for k, v in req.items():
        #     if v =="":
        #         missing.append(k)
        
        # if missing:
        #     feedback = f"Missing fields for {'. '.join(missing)}"
        #     return render_template("/submit_combo", feedback=feedback)
        
        #print(gameV)
        #print(comboV)
        


        if gameV != None and char_nameV != None and comboV != None:
            eCode = call_insert_combo(gameV, char_nameV, comboV, positionV, damageV, meterV, difficultyV, notesV)
            #TODO: Else show user error message 		
            if eCode == "45000":
                print("DEBUG: error, already in database!")
                flash('Combo already exists in database, please try submitting a different combo.')
            else:
                flash('Combo submitted to database.')
        return redirect(request.url)
    return render_template("submit_combo.html")


@app.route('/test2')
def testing2():
    return render_template("test2.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)