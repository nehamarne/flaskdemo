from flask import Flask
from tasks import add
app = Flask(__name__)
@app.route("/")
def hello():
	add.delay(4,4)
	return "Hello, I love Digital Ocean!"
if __name__ == "__main__":
    app.run()
