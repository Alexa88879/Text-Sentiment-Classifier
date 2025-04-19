# 🧠 Sentiment Analysis Web App

A simple yet effective web application that uses machine learning to classify text input as **positive**, **negative**, or **neutral**. Built with **Flask**, this app leverages a trained machine learning model and a TF-IDF vectorizer to analyze sentiments from user-provided text.

---

## 🚀 Features

- ✅ Classifies user input as Positive, Negative, or Neutral
- 🧠 Uses machine learning with TF-IDF and a pre-trained model
- 🌐 Web interface built with Flask and HTML/CSS
- 📂 Easily extendable for other NLP tasks
- 🛠 Lightweight and easy to deploy

---

## 📁 Project Structure

```
sentiment-main/
│
├── app.py                # Main Flask application
├── model.py              # Script to train or evaluate the model
├── clf.pkl               # Trained classification model
├── tfidf.pkl             # Pre-trained TF-IDF vectorizer
├── stop.txt              # Stopwords file (optional usage)
├── requirements.txt      # Python dependencies
│
├── static/               # Static assets (CSS, JS, images)
│   └── style.css
│
├── templates/            # HTML templates
│   └── index.html
│
└── README.md             # Project documentation
```

---

## ⚙️ Installation

### 🔹 Prerequisites

- Python 3.6+
- pip (Python package installer)

### 🔹 Steps

```bash
# 1. Clone the repository or unzip the project
git clone https://github.com/yourusername/sentiment.git
cd sentiment

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install the required dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py
```

Once running, open your browser and visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 How It Works

1. The user enters a sentence into the web form.
2. The text is preprocessed and transformed using the pre-trained **TF-IDF vectorizer** (`tfidf.pkl`).
3. The transformed vector is passed to the **classifier** (`clf.pkl`), which predicts the sentiment.
4. The sentiment (Positive/Negative/Neutral) is shown on the screen.

---

## 📚 Technologies Used

- **Python**
- **Flask**
- **Scikit-learn**
- **HTML/CSS**
- **Pickle**

---

## 📌 TODO / Improvements

- Add more advanced NLP preprocessing
- Add user authentication and history
- Improve UI with Bootstrap or TailwindCSS
- Deploy to Heroku, Vercel, or Render

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

