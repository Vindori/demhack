from flask import Flask, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle


app = Flask(__name__)

@app.route('/api/get_score/', methods=['POST'])
def get_score():
	text = request.json.get('text')
	if not text:
		return {'error': 'No text provided.'}


	vectorizer = TfidfVectorizer()
	X_1 = vectorizer.fit_transform(data)
	X_train = X_1[:split]
	X_test = X_1[split:]
	Y_test = inv_data(Y_test)
	a = vectorizer.transform([data[0]])
	model = pickle.load(open('../model/finalized_model.sav', 'rb'))
	score = model.predict(a)

	return {'score': score}

app.run(host='localhost', port=8080, debug=True)