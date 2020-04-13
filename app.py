from flask import Flask, render_template, request
from model import getHotels_info

app = Flask(__name__)

@app.route('/home')
def getHome():
	return render_template('index.html')

@app.route('/about')
def getAbout():
	return render_template('about.html')

@app.route('/hotels',methods=["POST"])
def getHotels():
	destination = request.form.get("city",None)
	property_type = request.form.get("property",None)
	facility = []
	Internet = request.form.get("Internet",None)
	if (Internet != None):
		facility.append(Internet)
	pool = request.form.get("pool",None)
	if (pool != None):
		facility.append(pool)
	Restaurant = request.form.get("Restaurant",None)
	if (Restaurant != None):
		facility.append(Restaurant)
	gym = request.form.get("Gym",None)
	if (gym != None):
		facility.append(gym)

	print(destination)
	print(property_type)
	print(facility)
	hotel = getHotels_info(destination,facility,property_type)
	print(hotel)
	return render_template('room.html',res=hotel)

if __name__ == '__main__':
	app.run(debug=True)
