# Building Desktop Applications with Python.

This tutorial will go through the steps of creating an application for a Windows environment, from creating the first python script and ending up with the packaged application. The application we are creating will be an interactive command line interface application, where the user can write tasks future use. With that in mind lets get started. The focus of this tutorial is to avoid requiring the user to have python installed and make sure that the program can be used in any folder. The application will be called **Todo** and give the user the possibility to create todo files in a folder.


## Creating the application skeleton

In this tutorial I will be using python 3.8. It is not vitally important that you have the same version but as long as you use Python 3 on windows this should be enough.
TODO: Determine level required to build application
Let's start out by creating a python file named todo.py for our main application function with the following content: 
```python
"""
"Welcome to the ToDo application, Type Q to Quit"
"""

def main():
  print(__doc__) # Prints the doc string from the todo.py
  while True:
    command = input("ToDo>")
    if command == "Q":
      break
  print("Exiting ToDo")

if __name__ == "__main__":
  main()

```

This is the skeleton we are going to use for our application, and it is ready to test out using:
```
c:\Users\jaykayace> python todo.py
Welcome to the TODO application, Type Q to Quit
ToDo>Q
Exiting ToDo
```

We can see that the application can start up, print the welcome message and shut down then we send the `Q` command, and we are ready to make an application. 

**Note**: Using the `print(__doc__)` in the beginning of the code is a nifty feature that makes sure that anything we put into the documentation of the todo file will be printed when the program starts. This is useful for our users to see the application documentation for now.

The reason for doing this so early in the process, where the application still really simple and easy to understand, is to eliminate the complications of building the application. This is key to building applications in general, that we take small increments and solve the problems we run into in before moving on to implement the next feature.
Consider the opposite case where you write more than 1000 lines of application code before testing if the code actually works and then tests this application using the python interpreter, are you then testing on the same level as the user or could there be some errors?

### Pyinstaller



## Interaction

## Using other peoples code as a dependency

### Development vs runtime dependencies

## Testing the application

## Building the application

## Where to go from here