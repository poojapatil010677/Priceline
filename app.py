from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home')
def getHome():
	return render_template('index.html')

@app.route('/about')
def getAbout():
	return render_template('about.html')

@app.route('/hotels',methods=["POST"])
def getHotels():
	destination = request.form["Destination"]
	checkin = request.form["checkin-date"]
	checkout = request.form["checkout-date"]
	adults = request.form["adults"]
	children = request.form["children"]
	print(destination)
	print(checkin)
	print(checkout)
	print(adults)
	print(children)
	return render_template('room.html')

if __name__ == '__main__':
	app.run(debug=True)
