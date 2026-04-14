from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/health', methods=['GET'])
def health():
    logger.info("Health check called")
    return jsonify({'status': 'UP', 'version': '1.0.0'}), 200


@app.route('/sum', methods=['POST'])
def get_sum():
    data = request.get_json()

    if data is None:
        return jsonify({'error': 'Invalid JSON body'}), 400

    a = data.get('a', 0)
    b = data.get('b', 0)

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({'error': 'Both a and b must be numbers'}), 400

    result = a + b
    logger.info(f"Sum called: {a} + {b} = {result}")
    return jsonify({'result': result}), 200


@app.route('/reverse-string', methods=['POST'])
def reverse_string():
    data = request.get_json()

    if data is None:
        return jsonify({'error': 'Invalid JSON body'}), 400

    text = data.get('text', '')

    if not isinstance(text, str):
        return jsonify({'error': 'text must be a string'}), 400

    result = text[::-1]
    logger.info(f"Reverse string called with: '{text}'")
    return jsonify({'result': result}), 200


@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()

    if data is None:
        return jsonify({'error': 'Invalid JSON body'}), 400

    a = data.get('a', 0)
    b = data.get('b', 0)

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({'error': 'Both a and b must be numbers'}), 400

    result = a * b
    logger.info(f"Multiply called: {a} * {b} = {result}")
    return jsonify({'result': result}), 200


@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Route not found'}), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({'error': 'Method not allowed'}), 405


if __name__ == '__main__':
    app.run(debug=False)