import numpy as np
class InputReader:
  def __init__(self):
    self.coordinates = []
    self.size = 0
    self.k = 0

  def read_size(self):
    self.size = int(input("Enter the size of the data points, must be > 0: "))

  def read_k(self):
    self.k = int(input("Enter the k hyperparameter value (0 < k <= size): "))
    if self.k <= 0 or self.k > self.size:
      print("K must be bigger than 0 and less than or equal to the size of the data points")
      return -1;

  def read_coordinates(self):
    for i in range(self.size):
      x = int(input(f"Enter x coordiante for point # {i + 1}: "))
      y = int(input(f"Enter y coordiante for point # {i + 1}: "))
      self.coordinates.append([x,y])

  def read_test_input(self):
    return int(input("Enter the test x coordinate to predict the corresponding y value: "))

class MLModels:
  def knn_regression(self, coordinates, k, input):
    # Euclidean distance
    distances = np.sqrt(np.sum((coordinates[:,:-1] - input) ** 2, axis=1))
    indices_to_sort = np.argsort(distances)
    k_indices = indices_to_sort[:k]
    k_values = coordinates[k_indices, 1]
    return np.mean(k_values)

def main():
  input_reader = InputReader()
  input_reader.read_size()
  if input_reader.read_k() == -1:
    return;
  input_reader.read_coordinates()
  coordinates = np.array(input_reader.coordinates)
  input_x = input_reader.read_test_input()

  ml_models = MLModels()
  y_pred = ml_models.knn_regression(coordinates, input_reader.k, np.array([input_x], dtype=int));

  print(f"The predicted y value for {input_x} is {y_pred}")

main()
