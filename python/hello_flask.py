from flask import Flask, escape, request,render_template,url_for,redirect


'''
@app.route("/")
def home():
	return "Hello, World!"

@app.route("/salvador")
def salvador():
	return "Hello, Salvador"

if __name__ == "__main__":
	app.run(debug=True)

'''

app = Flask(__name__,template_folder='./')
print(app)
@app.route('/')

def index():
	return render_template('home.html')

#def hello():
#	name = request.args.get("name", "World")
#	return 'hello'
if __name__ == '__main__':
	app.debug=True
	app.run()

