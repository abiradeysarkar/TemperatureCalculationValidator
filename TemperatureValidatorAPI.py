
# import main Flask class and request object
import decimal
import math

from flask import Flask, request

# create the Flask app
app = Flask(__name__)


@app.route('/convert', methods=['POST'])
def convert() -> float:
    fahrenheit: str = 'fahrenheit'
    celsius = 'celsius'
    kelvin = 'kelvin'
    rankine = 'rankine'
    valid_units = [fahrenheit, celsius, kelvin, rankine]
    if request.method == 'POST':
        data = request.json
        response = ''
        fromUnit:str = data['from']
        toUnit:str = data['to']
        value = (float)(data['value'])
        answer = (float)(data['answer'])

        if (fromUnit not in valid_units) or (toUnit not in valid_units):
            response = 'invalid'

        else:
            if fromUnit == fahrenheit:
                if toUnit == celsius:
                    actual = (5/9) * (value - 32)
                if toUnit == kelvin:
                    actual = (value - 32) * (5/9) + 273.15
                if toUnit == rankine:
                    actual = value + 459.67

            if fromUnit == celsius:
                if toUnit == fahrenheit:
                    actual = (value * 1.8) + 32
                if toUnit == kelvin:
                    actual = value + 273.15
                if toUnit == rankine:
                    actual = (value + 273.15) * 1.8

            if fromUnit == kelvin:
                if toUnit == fahrenheit:
                    actual = (value * 1.8) - 459.67
                if toUnit == celsius:
                    actual = value - 273.15
                if toUnit == rankine:
                    actual = value * 1.8

            if fromUnit == rankine:
                if toUnit == fahrenheit:
                    actual = value - 459.67
                if toUnit == celsius:
                    actual = (value - 491.67) * (5/9)
                if toUnit == kelvin:
                    actual = value * (5/9)

            if math.isclose(actual, answer, abs_tol=0.01):
               response = "Correct"
            else:
               response = "Incorrect"


    return response

@app.route('/f2c')
def celcius_to_fahrenheit() -> float:
    celsius = (float)(request.args.get('f'))
    fahrenheit = (celsius * 1.8) + 32
    return '''<h1>The fahrenheit value is: {}</h1>'''.format(fahrenheit)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)