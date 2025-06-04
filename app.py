from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='.', template_folder='.')

@app.route('/')
def home():
    return render_template("index.html")

# Serve static files like CSS, JS, images
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True)
