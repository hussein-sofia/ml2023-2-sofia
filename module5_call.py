from module5_mod import NumberSearcher

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
