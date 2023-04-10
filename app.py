from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "hello world"
		return jsonify({'data': data})


@app.route('/smote', methods = ['GET'])
def disp():

	return '''
	X, y = make_classification(
    n_samples=1000, # 1000 observations 
    n_features=5, # 5 total features
    n_informative=3, # 3 'useful' features
    n_classes=2, # binary target/label 
    random_state=999 # if you want the same results as mine
)
    '''

if __name__ == '__main__':

	app.run(debug = True)
