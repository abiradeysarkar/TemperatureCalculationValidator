

# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)


@app.route('/c2f')
def celcius_to_fahrenheit() -> float:
    celsius = (float)(request.args.get('c'))
    fahrenheit = (celsius * 1.8) + 32
    return '''<h1>The fahrenheit value is: {}</h1>'''.format(fahrenheit)

@app.route('/f2c')
def celcius_to_fahrenheit() -> float:
    celsius = (float)(request.args.get('f'))
    fahrenheit = (celsius * 1.8) + 32
    return '''<h1>The fahrenheit value is: {}</h1>'''.format(fahrenheit)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)


