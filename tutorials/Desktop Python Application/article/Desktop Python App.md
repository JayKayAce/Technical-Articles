# Building Desktop Applications with Python

This tutorial will go through the steps of creating an application for a Windows environment, from creating the first python script and ending up with the packaged application. The application we are creating will be an interactive command line interface application, where the user can write tasks future use. With that in mind lets get started. The focus of this tutorial is to avoid requiring the user to have python installed and make sure that the program can be used in any folder. The application will be called **Todo** and give the user the possibility to create todo files in a folder.

## Requirements for the application

TODO: add application requirements, and requirements for building the application.

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

We can see that the application can start up, print the welcome message and shut down then we send the `Q` command, and we are ready to make an application. This step is important because we now know that the application does not have any syntactical errors or strange behavior. 

> **Note**: Using the `print(__doc__)` in the beginning of the code is a nifty feature that makes sure that anything we put into the documentation in the top of the todo file will be printed when the program starts. This is useful for our users to see the application documentation for now when starting the program.

The reason for doing this so early in the process, where the application still really simple and easy to understand, is to eliminate the complications of building the application. This is key to building applications in general, that we take small increments and solve the problems we run into in before moving on to implement the next feature. Consider the opposite case where you write more than 1000 lines of application code before testing if the code actually works and then tests this application using the python interpreter, are you then testing on the same level as the user or could there be some errors?

### Before moving on

Before we move on let's make sure that our environment is setup correctly, so we have all the tools for building the application.

1. Create a [Virtual Environment](https://realpython.com/python-virtual-environments-a-primer/) and activate this
2. Install [pyinstaller](https://realpython.com/pyinstaller-python/) in the activated environment using [pip](https://realpython.com/what-is-pip/)
3. Create a `todo.py` file in a folder next to your environment, you can use my example here.

After all these steps we are ready to move on.

### Building from command line

When the package is installed we now have access to the pyinstaller command inside our virtual environment, so lets get specific before we start building.
We would like the application be combined into a single file for easy distribution. Reading the documentation for pyinstaller this can be done with the `--onefile` flag. lets try that from the command line:

```shell
c:\Code> pyinstaller todo.py --onefile
```

After the process of building the application has finished we can see that it adds some things to our project folder. It creates two new folders, called **build** and **dist** and it creates a todo.spec file. These are the outcomes of the build process and what we would like to end up with. In the **dist** folder we find our new windows program, all ready to hand over someone who does not have python on their system. One thing to think about when building applications is that in order to build our program again after we have changed something in the python code, we need to delete the dist folder and run the `pyinstaller` command again with the same arguments to get the application compiled. What happens if we forget to add the `--onefile` argument to the command? What happens if we forget to delete the old artifact and should we do that manually? If only there were a way to package our application from a build script, where we could define all the settings once and for all. We are in luck, because the PyInstaller is just python code, so we can make a python build script, that we can use to automate the building of our applications, with the same configurations every time the application is run. Let us get started on making our lives a bit easier.  

## Automating the building of applications

Let us start of with creating a new python file called `build_automation.py` where we can write our new build automation. From the  [pyinstaller documentation](https://pyinstaller.readthedocs.io/en/stable/usage.html#running-pyinstaller-from-python-code) we can find a code snippet for running the installer from a python file. This 

```python
"""
build_automation.py
this is a script which is used to automate the process of the application ToDo.
"""
# according to the Pyinstaller documentation we must import the special __main__ module
# in the package to package up the application.

import PyInstaller.__main__

# this is our package configuration and all the arguments we would like to add to the application
install_config = [
    "todo.py",
    "-n todo",
    "--clean",
    "--onefile"
]

# calling the build function from the PyInstaller package
PyInstaller.__main__.run(install_config)
```


## Using other peoples code as a dependency

### Development vs runtime dependencies

## Testing the application

## Building the application

## Where to go from here
