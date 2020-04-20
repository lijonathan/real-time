import time
import os
from os.path import isfile, join
from os import listdir
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

start_time = time.time()

onlyfiles = [f for f in listdir("../glove/training_data") if isfile(join("../glove/training_data", f))]

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


def display(results):
    print(f'{results.best_params_}\n')


print("RF Start")
rf = RandomForestClassifier()
rf_parameters = {
    	"max_depth": [1, 5, 15, 25, 50, 75, 100, 1000],
	"min_samples_split" : [2, 3, 4, 5, 6, 7, 8],
	"min_samples_leaf" : [1, 2, 3, 4, 5, 6, 7, 8]
}

cv = GridSearchCV(rf, rf_parameters, n_jobs = -1, cv = 5)
cv.fit(X, Y)
#print("Random Forest\n")
display(cv)
with open("rf_parameters.txt", "a") as rf_file:
    rf_file.write(f'{cv.best_params_}\n')

print("CV Start")
knn = KNeighborsClassifier()
knn_parameters = {
	"n_neighbors": [2, 5, 10, 25, 50, 100, 250, 500, 1000],
	"leaf_size": [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],
	"p": [1, 2]
}   

cv = GridSearchCV(knn, knn_parameters, n_jobs = -1)
cv.fit(X, Y)
#print("KNN\n")
display(cv)
with open("knn_parameters.txt", "a") as knn_file:
    knn_file.write(f'{cv.best_params_}\n')

end_time = time.time()

print("Execution time: ", int((time.time() - start_time) / 60), " minutes, ", (time.time() - start_time) % 60, "seconds")