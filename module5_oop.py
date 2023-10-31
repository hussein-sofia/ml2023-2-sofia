class NumberSearcher:
  def __init__(self):
    self.numbers = []
    self.size = 0
  
  def read_size(self):
    self.size = int(input("Enter the size of the array: "))

  def read_numbers(self):
    for i in range(self.size):
      self.numbers.append(int(input("Enter a number to add to the array: ")))

  def find_number(self, number_to_search):
    if number_to_search in self.numbers:
      index = self.numbers.index(number_to_search)+1
      return index
    
    return -1

def main():
  number_searcher = NumberSearcher()

  number_searcher.read_size()
  number_searcher.read_numbers()

  number_to_search = int(input(f"Enter the integer to be searched: "))
  index = number_searcher.find_number(number_to_search)

  if(index == -1):
    print("-1")
    return;
  
  print(f"The first occurence of number {number_to_search} is at index {index}")

main()
