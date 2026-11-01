from flask import Flask, jsonify


app=Flask(__name__)

@app.route('/api/v1/students' methods=['GET'])
def get_all_student():
	return jsonify({'message':'successfully pulled all student'})


@app.route('/api/v1/student/dashboard' methods=['GET'])
def index():
	return jsonify({'message':'welcome'})

@app.route('/api/v1/students/<int:id>', methods=['GET'])
def get_one_student()
	return jsonify({'message':'successfully fetched student'})

@app.route('/api/v1/students/<int:id>', methods=['PATCH'])
def update_student()
	return jsonify({'message':'student updated successful'})



if __name__=='__main__':
	app.run(debug=True)