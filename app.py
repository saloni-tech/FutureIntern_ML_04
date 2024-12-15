import pickle
from flask import Flask, request, render_template

app = Flask(__name__)
# Example using raw string
with open(r"C:\Users\Lenovo\Downloads\fraud_detection_model.pkl", 'rb') as model_file:
    # Load your model or perform operations here
    model = pickle.load(model_file)

@app.route('/')
def index(): 
    return render_template('index.html')  # Make sure you have an index.html file in the templates folder

@app.route('/predict_fraud', methods=['POST'])
def predict_fraud():
    if request.method=='POST':
        type = int(request.form.get('type'))
        amount= float(request.form.get('amount'))
        oldbalanceOrg = float(request.form.get('oldbalanceOrg'))
        newbalanceOrig = float(request.form.get('newbalanceOrig'))
        prediction = model.predict([[type,amount,oldbalanceOrg,newbalanceOrig]])
        #return the prediction result
    return render_template('/predict_fraud.html',is_fraud=prediction[0])
   
if __name__ == '__main__':
    app.run(debug=True)                                                                     
     
