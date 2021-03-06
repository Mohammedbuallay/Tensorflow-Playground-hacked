from flask import Flask,render_template,send_from_directory
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/js/<path:path>')
def send_images(path):
    return send_from_directory('js', path)

if __name__ == '__main__':
    app.run(debug=True)
