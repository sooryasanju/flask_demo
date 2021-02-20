from flask import Flask,jsonify,request


app = Flask(__name__)

@app.route('/')
def hello_world():
    s= "Hello"
    return s

@app.route('/sum/',methods=['POST'])
def sum():
    try:
        number_1          = int(request.form.get('number_1'))
        number_2          = int(request.form.get('number_2'))

        if type(number_1) != int or type(number_2) != int:
            response = {
                "status"  : False,
                "message" : "enter integers only"
            }
            return jsonify(response)
        sum = number_1 + number_2
        response = {
            "status"      : True,
            "sum"         : sum
        }
        return jsonify(response)
    except Exception as e :
        response = {
            "status"      : False,
            "message"     : str(e)
        }
        return jsonify(response)
if __name__ == '__main__' :
   app.run(debug=True,host='0.0.0.0', port='5000')