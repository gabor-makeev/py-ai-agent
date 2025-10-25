from functions.write_file import write_file

def test():
  result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
  print("Result for existing file:")
  print(result)

  result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
  print("Result for new file:")
  print(result)

  result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
  print("Result for file outside of the working directory:")
  print(result)

if __name__ == "__main__":
    test()