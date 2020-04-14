from flask import Flask, render_template, request
from model import getHotels_info
import pandas as pd

app = Flask(__name__)

@app.route('/about')
def getAbout():
	return render_template('about.html')

@app.route('/contact', methods=['POST','GET'])
def getContact():
	user_list = []
	if(request.method == "post"):
		inform = request.form.get("info",None)
		user_list.append(inform)
		return render_template('index.html')
	else:	
		return render_template('contact.html')

@app.route('/details',methods=["POST"])
def getHotel_Details():
	return render_template('single-room.html')

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
	print(len(hotel[0]))
	if(len(hotel[0])<5):
		return render_template('notfound.html')
	else:
		return render_template('room.html',res=hotel)

@app.route('/home')
def getHome():
	hotel = pd.read_csv("data.csv")
	hotel_info = hotel[(hotel['guest_recommendation'] == 100) & (hotel['site_review_rating'] == 5)]
	r=[]
	count = (hotel_info.groupby('city')['guest_recommendation'].count()>=3).reset_index()
	for index,row in count.iterrows():
		r.append(row['city']) if row['guest_recommendation'] else 0
	return render_template("index.html", data=r)

@app.route('/bangalore')
def bang_get():
	b_list=[]
	b_fac=[]
	hotel = pd.read_csv("data.csv")
	blore_info = hotel[(hotel['guest_recommendation'] == 100) & (hotel['site_review_rating'] == 5) & (hotel['city'] == 'Bangalore')]
	a=blore_info['property_name'].reset_index()
	for index,row in a.iterrows():
		b_list.append(row['property_name'])
	b=blore_info['additional_info'].reset_index()
	for index,row in b.iterrows():
		b_fac.append(row['additional_info'])
	return render_template('bangalore.html',blore_fac=b_fac,blore=b_list)

@app.route('/manali')
def manali_get():
	man_list=[]
	man_fac=[]
	hotel = pd.read_csv("data.csv")
	man_info = hotel[(hotel['guest_recommendation'] == 100) & (hotel['site_review_rating'] == 5) & (hotel['city'] == 'Manali')]
	a=man_info['property_name'].reset_index()
	for index,row in a.iterrows():
		man_list.append(row['property_name'])
	b=man_info['additional_info'].reset_index()
	for index,row in b.iterrows():
		man_fac.append(row['additional_info'])
	return render_template('manali.html',man_fac=man_fac,man=man_list)

@app.route('/goa')
def goa_get():
	goa_list=[]
	goa_fac=[]
	hotel = pd.read_csv("data.csv")
	goa_info = hotel[(hotel['guest_recommendation'] == 100) & (hotel['site_review_rating'] == 5) & (hotel['city'] == 'Goa')]
	a=goa_info['property_name'].reset_index()
	for index,row in a.iterrows():
		goa_list.append(row['property_name'])
	b=goa_info['additional_info'].reset_index()
	for index,row in b.iterrows():
		goa_fac.append(row['additional_info'])
	return render_template('goa.html',goa_fac=goa_fac,goa=goa_list)


if __name__ == '__main__':
	app.run(debug=True)
