from flask import Flask, request, jsonify

app = Flask(__name__)

# members route


@app.route('/members')
def members():
    return jsonify({'members': ['Member1', 'Member2', 'Member3']}),200


if __name__ == "__main__":
    app.run(debug=True)
