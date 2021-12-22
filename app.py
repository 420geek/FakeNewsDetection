from flask import*
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer


vector = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("finalized_model.pkl", 'rb'))

app = Flask(__name__,template_folder="template")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction' ,methods = ['GET','POST'])
def prediction():
    if request.method == "POST":
        news = request.form['news']
        print(news)
        predict = model.predict(vector.transform([news]))[0]
        print(predict)

        return render_template("prediction.html", prediction_text="News Headline is {}".format(predict))

    else:
        return render_template("prediction.html")    

app.run(debug=True)