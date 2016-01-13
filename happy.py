from flask import Flask, request
from flask import render_template

# set the project root directory as the static folder, you can set others.
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080, debug=True)

