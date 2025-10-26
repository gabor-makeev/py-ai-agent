from functions.run_python_file import run_python_file

def test():
  result = run_python_file("calculator", "main.py")
  print("Result for python script:")
  print(result)

  result = run_python_file("calculator", "main.py", ["3 + 5"])
  print("Result for python script with arguments:")
  print(result)

  result = run_python_file("calculator", "tests.py")
  print("Result for python script with no output:")
  print(result)

  result = run_python_file("calculator", "../main.py")
  print("Result for an executable outside of the working directory:")
  print(result)

  result = run_python_file("calculator", "nonexistent.py")
  print("Result for a non-existent executable:")
  print(result)

  result = run_python_file("calculator", "lorem.txt")
  print("Result for a non-python executable:")
  print(result)

if __name__ == "__main__":
    test()