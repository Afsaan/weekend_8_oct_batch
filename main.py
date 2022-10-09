from flask import Flask,request

#initialize the flask
app = Flask(__name__)

data = {"present_student" : ["tanveer","ajay","Deepak","Niyaz","Saurav","Mani"]}

@app.route('/',methods=['GET'])
def home():
    return {"message" : "all student data"}


@app.route('/get_names',methods=['GET'])
def get_names():
    return data

@app.route('/post_names',methods=['POST'])
def post_names():
    updated_data = request.json['new_data']
    print(updated_data)
    return {"status":"Success"}

@app.route('/update_names',methods=['PUT'])
def update_names():
    updated_data = request.json['new_data']
    data['present_student'].append(updated_data)
    return {"status":"Success"}

#run the app
app.run(debug=True)