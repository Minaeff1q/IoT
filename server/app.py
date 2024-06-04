from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    if not data or 'temperature' not in data or 'windspeed' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    temperature = data['temperature']
    windspeed = data['windspeed']
    city = data['city']
    
    print(f"Received data - City: {city}, Temperature: {temperature}, windspeed: {windspeed}",flush=True)
    
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)