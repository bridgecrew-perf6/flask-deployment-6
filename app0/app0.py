from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World from app0!!'

# this block is not necessary. i put this for a testing.
# if __name__ == "__main__":
# 	app.run()