import pandas as pd

# Fetching the hotels from the dataset
def getHotels_info(city,facility,ptype):

	#read the dataset
	df = pd.read_csv("data.csv")

	#filter based on the city
	res = df.loc[df['city']==city]
	
	#filter based on the type of property
	if(res.shape[0]>=5):
		res = res.loc[df['property_type'] == ptype]

	#filter based on the facilities
	for fac in facility:
		if(res.shape[0]>5):
			#print(res.shape[0])
			res1 = res['additional_info'].str.contains(fac)
			res1 = res1.fillna(False)
			res = res.loc[res1] 
	
	res = res.dropna(subset=["review_count_by_category"])
	reviews = []
	ratings = []
	temp = res.values.tolist()
	for i in range(len(temp)):

		#positive reviews	
		t = temp[i][24].split("|")
		s = t[0].split("::")
		reviews.append(int(s[1]))

		#ratings
		t1 = temp[i][32].split("|")
		r1 = 0
		for j in t1:
			s1 = j.split("::")
			r1 = r1 + float(s1[1])
		ratings.append(r1+temp[i][31])

	#print(reviews)
	#print(ratings)
	res["reviews"] = reviews
	res["ratings"] = ratings

	res1 = res.sort_values(by=['ratings'] , ascending = False)
	res2 = res1.sort_values(by=['reviews'], ascending = False)

	l1 = (res['property_name'].head(5)).values.tolist()
	l2 = (res['additional_info'].head(5)).values.tolist()
	result = [l1,l2]
	return result
"""
#main function
if __name__ == "__main__":
	city = input("Enter the city you want to visit : ")
	facility = ['Internet','Pool']
	ptype = "Hotel"
	hotel = getHotels(city,facility,ptype)
	print(hotel)

"""
