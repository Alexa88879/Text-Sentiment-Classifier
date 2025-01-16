from flask import Flask , render_template ,url_for , request ,jsonify
from model import *
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/sentiment_result" ,methods=['POST'])
def sentiment_result():
    comment=request.form['comment']
    sentiment = prediction(comment)
    sentiment_text = "Positive" if sentiment == 1 else "Negative"
    return jsonify({'sentiment': sentiment, 'message': sentiment_text})

if __name__ == "__main__":
    app.run(debug=True)