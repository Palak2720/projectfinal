from flask import Flask, escape, render_template, request
import pickle

vector=pickle.load(open("vector.pkl",'rb'))
model=pickle.load(open("finalized_model.pkl",'rb'))
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")




@app.route('/prediction', methods=['GET','POST'])
def prediction():
    if request.method=="POST":
        news=str(request.form['news'])
        predict=model.predict(vector.transform([news]))[0]
        if predict==0:
            predict = "REAL"
        elif predict==1:
            predict="FAKE"
        else:
            predict="Something went wrong"
        


        return render_template("prediction.html", prediction_text="News headline is -> {}".format(predict))


    else:
        return render_template("prediction.html")


@app.route('/contactus')
def contactus():
    return render_template("contactus.html")



if __name__=='__main__':
    app.run()
