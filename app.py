from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.json
        temp = float(data.get('temperature'))
        unit = data.get('unit')
        
        results = {}
        
        if unit == "Celsius":
            results['Fahrenheit'] = round((temp * 9/5) + 32, 2)
            results['Kelvin'] = round(temp + 273.15, 2)
        
        elif unit == "Fahrenheit":
            results['Celsius'] = round((temp - 32) * 5/9, 2)
            results['Kelvin'] = round(((temp - 32) * 5/9) + 273.15, 2)
        
        elif unit == "Kelvin":
            if temp < 0:
                return jsonify({'error': 'Kelvin cannot be less than 0.'}), 400
            results['Celsius'] = round(temp - 273.15, 2)
            results['Fahrenheit'] = round(((temp - 273.15) * 9/5) + 32, 2)
        
        return jsonify(results)
    
    except ValueError:
        return jsonify({'error': 'Please enter a valid numeric temperature.'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
