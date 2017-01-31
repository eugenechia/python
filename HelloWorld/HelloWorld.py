from flask import Flask
application = Flask(__name__)

@application.route("/")
def Hello():
	return "<h1 style='color:blue'>Hello World! This is my 1st site using Flask framework!</h1>"

if __name__ == "__main__":
	application.run(host='0.0.0.0')
