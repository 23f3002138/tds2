from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'it works!'

@app.route('/api', methods=['GET'])
def get_marks():
    with
    names = request.args.getlist('name')
    response = {name: marks_data.get(name, "Name not found") for name in names}
    return jsonify(response)

@app.route('/about')
def about():
    return 'About'
