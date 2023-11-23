import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import precision_score, recall_score

class InputReader:
  def __init__(self):
    self.size = 0

  def read_size(self):
    self.size = int(input("Enter the size of the data points, must be > 0: "))
    self.truth_values = np.zeros(self.size, dtype=int)
    self.predicted_values = np.zeros(self.size, dtype=int)

  def read_coordinates(self):
    for i in range(self.size):
      x = int(input(f"Enter truth value for # {i + 1}, it must be 0 or 1: "))
      if x != 0 and x != 1:
        print("Truth value must be 0 or 1")
        return -1
      y = int(input(f"Enter prediction value for # {i + 1}, it must be 0 or 1: "))
      if y != 0 and y != 1:
        print("Prediction value must be 0 or 1")
        return -1
      self.truth_values[i] = x
      self.predicted_values[i] = y


class PredictionCalculations:
  def __init__(self, truth_values, predicted_values):
    self.truth_values = truth_values
    self.predicted_values = predicted_values
  
  def precision_score(self):
    return precision_score(self.truth_values, self.predicted_values)
  
  def recall_score(self):
    return recall_score(self.truth_values, self.predicted_values)


def main():
  input_reader = InputReader()
  input_reader.read_size()
  if input_reader.read_coordinates() == -1:
    return;

  prediction_calculations = PredictionCalculations(input_reader.truth_values, input_reader.predicted_values)

  precision = prediction_calculations.precision_score()
  recall = prediction_calculations.recall_score()

  print(f"The precision is {precision:.2f}")
  print(f"The recall is {recall:.2f}")

main()
