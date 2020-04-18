from os.path import isfile, join
from os import listdir
from sklearn.ensemble import RandomForestClassifier, KNeighbborsClassifier
from sklearn.model_selection import GridSearchCV



onlyfiles = [f for f in listdir("../glove/training_data") if isfile(join"../glove/training_data", f)]

for i in range(0, len(onlyfiles)):
    onlyfiles[i] = os.path.join("../glove/training_data", onlyfiles[i])


X = []
Y = []

for i in range(0, len(onlyfiles)):
    with open(onlyfiles[i]) as data_file:
        for line in data_file:
            line = line.strip("\n")
            x_pt = []
            data_pts = line.split(",")
            result = data_pts[- 1]
            del data_pts[-1]
            for k in range(0, len(data_pts)):
                x_pt.append(float(data_pts[k]))
            X.append(x_pt)
            Y.append(result)


val_range = []
for i in range(1, 251):
	val_range.append(i * 5)

rf = RandomForestClassifier()
rf_parameters = {
	"n_estimators:": val_range,
	"max_depth": val_range,
	"min_samples_split" : val_range,
	"min_samples_leaf" : val_range
}

cv = GridSearchCV(rf, parameters, n_jobs = -1)
cv.fit(X, Y)
print("Random Forest best parameters are: {results.best_params_}\n\n")




knn = KNeighbborsClassifier()
knn_parameters = {
	"n_neighbors": list(range(100)),
	"leaf_size": list(range(100)),
	"p": [1, 2]
}

cv = GridSearchCV(knn, parameters, n_jobs = -1)
cv.fit(X, Y)
print("KNN best parameters are: {results.best_params_}")



