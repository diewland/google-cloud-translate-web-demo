from flask import Flask, render_template, request, jsonify
from google.cloud import translate

app = Flask(__name__)
client = translate.Client()

# front
@app.route('/')
def hello():
    return render_template('index.html')

# controller
@app.route('/translate', methods=['POST'])
def func_translate():
    source_text = request.json.get('text', '')
    source_language = request.json.get('from', 'en')
    target_language = request.json.get('to', 'th')
    result = client.translate(source_text, source_language=source_language, target_language=target_language)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)