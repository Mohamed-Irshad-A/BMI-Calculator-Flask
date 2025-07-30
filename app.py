from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        weight=float(request.form['weight'])
        height=float(request.form['height'])

        bmi=round(weight/((height/100)**2),2)

        if bmi<18.5:
            category="Underweight"
        elif 18.5<=bmi<25:
            category="Normal"
        elif 25<=bmi<30:
            category="Overweight"
        else:
            category="Obese"

        return render_template("result.html",b=bmi,c=category)
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)