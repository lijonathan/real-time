from sklearn.ensemble import RandomForestClassifier
import json


'''
json_data = {"state":
					{
					"reported":{

								"imu_z": -17.625,
								"imu_y": 0.1875,
								"imu_x": 251.625
								}
					}

}


y = ["a"]

##l = json.dumps(json_data)
#print(type(l))
'''

with open ("..\\src\\web-app\\misc\\fabData.json") as json_file:
	data = json.load(json_file)
	#print(data)


X = []
Y = []

print(data)
for data_pt in data:
	vals = data_pt["state"]["reported"]
	X.append(list(vals.values()))
	result = data_pt["result"]
	Y.append(result)


#print(len(Y))
#print(len(X))
'''
data = []
for key, item in json_data["state"]["reported"].items():
	data.append(item)
'''
#x = []
#x.append(data)

#print(data)
rf = RandomForestClassifier()
rf.fit(X, Y)
while True:
	



#rf.fit(train_X, train_y)




