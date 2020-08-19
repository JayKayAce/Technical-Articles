# Automating the process of Building Desktop Applications with Python

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

After all these steps we are ready to build our application.

### Building from command line

When the package is installed we now have access to the pyinstaller command inside our virtual environment, so lets get specific before we start building.
We would like the application be combined into a single file for easy distribution. Reading the documentation for pyinstaller this can be done with the `--onefile` flag. lets try that from the command line:

```shell
c:\Code> pyinstaller todo.py --onefile
```

After the process of building the application has finished we can see that it adds some things to our project folder. It creates two new folders, called **build** and **dist** and it creates a todo.spec file. These are the outcomes of the build process and what we would like to end up with.

```shell
Project folder
    |-- build
    |-- dist
  |-- todo.py
  |-- todo.spec
```

In the **dist** folder we find our new windows program, all ready to hand over someone, who does not have python on their system. One thing to think about when building applications is that in order to build our program again after we have changed something in the python code, we need to delete the dist folder and run the `pyinstaller` command again with the same arguments to get the application compiled. What happens if we forget to add the `--onefile` argument to the command? What happens if we forget to delete the old artifact and should we do that manually? If only there were a way to package our application from a build script, where we could define all the settings once and for all. We are in luck, because the PyInstaller is just python code, so we can make a python build script, that we can use to automate the building of our applications, with the same configurations every time the application is run. Let us get started on making our lives a bit easier.

> **Note:** We will disregard the **build** folder and only focus on the **dist** folder for now since the purpose of the **build** folder is documented
in the Pyinstaller documentation and in several tutorials elsewhere, and is not essential for the solution.

## Automating the building of applications

Let us start of with creating a new python file called `build_automation.py`. Here we can write our new build automation so that the configuration is set once and controlled by our version control system. This gives the benefits of keeping track of any changes in the builds and we can go back and change the solution. From the [pyinstaller documentation](https://pyinstaller.readthedocs.io/en/stable/usage.html#running-pyinstaller-from-python-code) we can find a code snippet for running the installer from a python file.

```python
"""
build_automation.py
this is a script which is used to automate the process of the application ToDo.
"""
# according to the Pyinstaller documentation we must import the special __main__ module
# in the package to package up the application.

import PyInstaller.__main__
import os

# this is our package configuration and all the arguments we would like to add to the application
build_config = [
    "-n=todo",
    "--clean",
    "--onefile",
    os.path.join(".","todo.py"),
]

# calling the build function from the PyInstaller package
PyInstaller.__main__.run(build_config)
```

First we need to import the python file in PyInstaller, which contains the `run()` function we need to automate the build process. Additionally we need to import the builtin `os` module for later usage.

We have chosen the following arguments to keep in our `build_config` list:

* `--onefile` results in our package is build into a single file. 
* `-n=` renames the resulting build output, in our case to `todo`
* `--clean` makes sure that the previous build output is deleted before building the next part.
* `os.path.join()` is used to format the path to our `todo.py`. We could also have written `"./todo.py"` which is the outcome of the join function.

In the end of the file we call the `run()` function with the argument `build_config` to start the packaging process every time the build script is called.

> **Note:** The import of the module and subsequent function call may seem a bit strange, but is just because the file that contains the run function is stored in the `__main__.py` file inside the Pyinstaller package, and has a special meaning. If you chose to run the module using `python -m pyinstaller` this would be the file that was called by the python interpreter. Try to look for other packages which have a `__main__.py` in their package folder in some of the packages you have installed. 

Now we can build the application as many times as we like using and make sure we test on the latest changes in the application:
```shell

c:\Code> python build_automation.py

```

## Testing the application

In order to perform the same test of the application we start the application from the command line by executing the following command.

```shell

C:\Code\>.\dist\todo.exe
Welcome to the TODO application, Type Q to Quit

ToDo>

Exiting ToDo
```

Another thing we could need to look into was what if we started the application from the explorer instead of the command line? The result of this would be that the program launches its own python interpreter window and starts up the application, and is ready for input.


## Final notes

Through this article we have automated part of a solid application foundation for packaging our desktop applications for people who do not have Python installed. From here we can start to add all the customer requirements and develop all the features that the customer needs. We no longer have to worry about forgetting to set the build parameters right and we can focus on the process of writing the code. Additionally we can easily perform our tests on the actual product and not skip any steps when performing the tests. 

## Additional Inspiration