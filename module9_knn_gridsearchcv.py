import numpy as np
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import accuracy_score

class InputReader:
  def __init__(self):
    self.size = 0

  def read_size(self):
    self.size = int(input("Enter the size of the datapoints, must be > 2 (for gridsearch): "))
    return np.zeros(self.size, dtype=int), np.zeros(self.size, dtype=int)

  def read_pairs(self, x_array, y_array):
    for i in range(x_array.size):
      x = float(input(f"Enter input feature # {i + 1}, any real number: "))
      y = int(input(f"Enter class label for # {i + 1}, it must be nonnegative integer: "))
      while(y < 0):
        print("Class label must be nonnegative integer")
        y = int(input(f"Enter prediction value for # {i + 1}, it must be 0 or 1: "))
      x_array[i] = x
      y_array[i] = y
    return x_array,y_array


def main():
  input_reader = InputReader()
  x_train, y_train = input_reader.read_size()
  x_train, y_train = input_reader.read_pairs(x_train, y_train);

  print("---------------------------------------------------------")

  x_test, y_test = input_reader.read_size()
  x_test, y_test = input_reader.read_pairs(x_test, y_test);

  knn = KNeighborsRegressor()
  params = {'n_neighbors': list(range(1, min(x_train.size+1, x_test.size + 1, 11)))}
  
  grid_search = GridSearchCV(knn, params, verbose=1, cv=min(x_test.size+1, x_train.size + 1), scoring='accuracy')

  grid_search.fit(x_train.reshape(-1, 1), y_train)

  print(grid_search.best_params_)
  print(grid_search.best_score_)

  y_pred = grid_search.predict(x_test.reshape(-1, 1))

  accuracy = accuracy_score(y_test, y_pred)

  print(accuracy)

main()
