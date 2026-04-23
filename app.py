from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api')
def api():
    return jsonify({"message": "Hello from API"})

@app.route('/submittodoitem', methods=['POST'])
def submit():
    data = request.json
    return jsonify({
        "itemName": data.get("itemName"),
        "itemDescription": data.get("itemDescription"),
        "status": "received"
    })

if __name__ == '__main__':
    app.run(debug=True)