# Building Desktop Applications with Python

This tutorial will go through the steps of creating an application for a Windows environment, from creating the first python script and ending up with the packaged application. The application we are creating will be an interactive command line interface application, where the user can write tasks future use. With that in mind lets get started. The focus of this tutorial is to avoid requiring the user to have python installed and make sure that the program can be used in any folder. The application will be called **Todo** and give the user the possibility to create todo files in a folder.

## Creating the application skeleton

In this tutorial I will be using python 3.8. It is not vitally important that you have the same version but as long as you use Python 3 on windows this should be enough.
TODO: Determine level required to build application
Let's open a text editor and start out by creating a python file named `todo.py` for our main application functionality with the following content:

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

This is the skeleton we are going to use for our application, and it is ready to test from the command line out using:

```shell
c:\Code> python todo.py
Welcome to the TODO application, Type Q to Quit
ToDo>Q
Exiting ToDo
```

We can see that the application can start up, print the welcome message and shut down then we send the `Q` command, and we are ready to make an application.

> **Note**: Using the `print(__doc__)` in the beginning of the code is a nifty feature that makes sure that anything we put into the documentation in the top of the todo file will be printed when the program starts. This is useful for our users to see the application documentation for now.

The reason for doing this so early in the process, where the application still really simple and easy to understand, is to eliminate the complications of building the application. This is key to building applications in general, that we take small increments and solve the problems we run into in before moving on to implement the next feature. Consider the opposite case where you write more than 1000 lines of application code before testing if the code actually works and then tests this application using the python interpreter, are you then testing on the same level as the user or could there be some errors?

### Isolating our development from other projects

We need to install an python package in order to compile the todo script we created into an application. To make sure we do not break any other python projects we have on our machine we will create a virtual environment. This is included in python 3 using the [venv](https://docs.python.org/3/library/venv.html) module, and to run it from the command line:

```shell
c:\Code> python -m venv venv
c:\Code> venv\Scripts\activate
(venv) c:\code>
```

The first line will create a virtual environment named `venv` inside out code folder and the second line will activate this. Now it is time to install the [pyinstaller](https://www.pyinstaller.org/) package in our virtual environment.

```shell
(venv) C:\Code> pip install pyinstaller
```

When the installation is complete we can convert our

## Interaction

## Using other peoples code as a dependency

### Development vs runtime dependencies

## Testing the application

## Building the application

## Where to go from here
