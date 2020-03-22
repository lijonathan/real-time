from sklearn.ensemble import RandomForestClassifier
import json

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
data = []
for key, item in json_data["state"]["reported"].items():
	data.append(item)

x = []
x.append(data)

print(data)
rf = RandomForestClassifier()
rf.fit(x, y)



#rf.fit(train_X, train_y)




