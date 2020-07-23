from flask import Flask, request, abort, jsonify, make_response

app = Flask(__name__)
app.config['DEBUG'] = True

# TODO: Add API Key header
@app.route('/', methods=['GET'])
def root():
    result = { "success": True }
    return jsonify(result)


def start_app():
    app.run(debug=True)