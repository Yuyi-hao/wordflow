from flask import Flask, render_template, request, jsonify
from src import suggest_word 


maximum_word = 5

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    prefix = request.args.get('prefix').split(' ')[-1].lower()
    suggestions = None
    if prefix:
        suggestions = suggest_word(prefix)[:maximum_word]
    return jsonify(suggestions=suggestions)


if __name__=="__main__":
    app.run()