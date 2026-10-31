from flask import Flask, jsonify


app=Flask(__name__)


@app.route('/' methods=['GET'])
def index():
	return jsonify({'message':'welcome victor'})

@app.route('/api/v1/students/<int:id>', methods=['GET'])
def get_one_student()
	return jsonify({'message':'successfully fetched student'})



if __name__=='__main__':
	app.run(debug=True)