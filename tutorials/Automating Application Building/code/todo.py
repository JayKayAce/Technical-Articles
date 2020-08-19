"""
Welcome to the ToDo application, Type Q to Quit
"""

def main():
  print(__doc__) # 
  while True:
    command = input("ToDo>")
    if command == "Q":
      break
  print("Exiting ToDo")

if __name__ == "__main__":
  main()
