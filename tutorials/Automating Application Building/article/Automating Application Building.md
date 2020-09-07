# Automating the Desktop Applications Building process with Python

Most python code is developed for other python users or web applications and not for desktop users who do not have Python installed. Therefore packaging your application up for delivery to non-python users is a grey area in the world of Python. This is why tools like Pyinstaller was created. It improves the packaging process for developing applications that can be distributed to non-python users. This comes with another set of challenges where getting consistent outcomes is dependent on remembering command-line arguments when invoking the packaging function.

This tutorial will focus on automating the process of packaging desktop applications with Pyinstaller, so you easily can run the **packaging** automation as a normal python script. Additionally, your script can track the settings in your version control system, such as Git.

**In this tutorial, you will learn**:

* When is it the best time to implement the **packaging** process.
* How to implement the basics of **packaging** for delivering to non-python users.
* How to call PyInstaller with consistent arguments from a simple Python script

Here are some of the reasons why packaging up applications for the end user below is important.

* Packaging up an application to be installed on a system solves many problems with regards to environments and system compatibility.
* There is **no** need to install Python to use the application features, because the application is packaged with all the requirements.
* There is **no** need to know the Python language or even know that the application is even written in python. It is just a normal application performing its features.

Additionally it makes you think about testing and using your end product in the same way as the end user, instead of running a script through an interpreter. If the usage of the application end product is sub-optimal for you, it will also be sub-optimal for your users. The good solution is to catch this early in the process, so let's get started.

## Setting up the Development Environment

Before you develop the application, let's make sure that your environment is setup correctly, so you have all the tools for building the application. If you are unsure about how to proceed, the links provide access to additional information on the specific topics to install and work with:

1. Install Python 3.5 or above. I use [Python 3.8](https://www.python.org/downloads/release/python-383/) while writing the tutorial
2. Create and activate a [Virtual Environment](https://realpython.com/python-virtual-environments-a-primer/)
3. Install [pyinstaller](https://realpython.com/pyinstaller-python/) in the activated environment using [pip](https://realpython.com/what-is-pip/)

After all these steps you're ready to build your application.

## Creating the application skeleton

The application will be called **Todo** and takes the user input in the form of a text command. It is not vitally important that you have the same version but as long as you use Python 3 on Windows, this should be enough. Open a text editor and start out by creating a python file named `todo.py` for your main application functionality with the following content:

```python
"""
Welcome to the ToDo application, Type Q to Quit
"""

def main():
    print(__doc__)
    while True:
        command = input("ToDo>")
        if command == "Q":
            break
    print("Exiting ToDo")

if __name__ == "__main__":
    main()

```

This is the skeleton you are going to use for our application, and it is ready to test from the command line out using:

```shell
c:\Code> python todo.py
Welcome to the TODO application, Type Q to Quit
ToDo>Q
Exiting ToDo
```

If this succeeded thus far, you can see that the application can perform the following steps:

* Start up without errors
* Print the welcome message
* Shut down when you send the `Q` command
* Print the exit message

> **Tip**: Using the `print(__doc__)` in the beginning of the code is a nifty feature that makes sure that anything you put into the todo.py documentation in the top will be printed when the program starts. There are other options, but these are outside the scope of the article. 

This is the absolute bare bones of any application, which can be tested.

## Test, Verify and Increment

**Testing at this step before packaging is important**, because you now know that the application does not have any syntactical errors or strange behavior, and reacts to user inputs. The reason for doing this test so early in the process, where the application still really simple and easy to understand, is to eliminate the complications of building the application. This is key to building applications in general, that you make small increments and solve the problems you run into in before moving on to implementing the next feature.

Consider the opposite case where you write more than 1000 lines of application code before testing. How do you know the code actually works and how much of it works? Another bad solution is to package the application as the last part of the delivery of the application, and then you discover a bug in the packaged application. This is not fun, and is the straight road to stress and bad solutions.

## Building from command line

It's time to get specific before you start building. Your end user would like the application be combined into a single file for easy distribution and easy deployment for your users. Reading the documentation for Pyinstaller this can be done with the `--onefile` flag. Let's try that from the command line for now:

```shell
c:\Code> pyinstaller todo.py --onefile
```

After the process of building the application has finished you can see that it adds some things to your project folder. It creates two new folders, called **build** and **dist** and it creates a todo.spec file. These are the outcomes of the build process, and the folder structure changes can be seen below:

```shell
Project folder
    |-- build
    |-- dist
  |-- todo.py
  |-- todo.spec
```

In the **dist** folder you find your new Windows program, all ready to hand over someone, who does not have Python on their system. 

> Note: Packaged files and outcomes of a build process are often refered to as **build artifacts** or just **artifacts**.

One thing to think about when building applications is that in order to build your program again after you have changed something in the python code, you need to delete the **dist** folder and run the `pyinstaller` command again with the same arguments to get the application compiled. This may bring some questions to your mind such as:

* What happens if you forget to add the `--onefile` argument to the command?
* What happens if you forget to delete the old artifact and should you do that manually?

If only there were a way to package our application from a build script, where we could define all the settings once and for all. We are in luck, because the PyInstaller is just python code, so we can make a python build script, that we can use to automate the building of our applications, with the same configurations every time the application is run. Let us get started on making our lives a bit easier.

> **Note:** We will disregard the **build** folder and only focus on the **dist** folder for now since the purpose of the **build** folder is documented
in the Pyinstaller documentation and in several tutorials elsewhere, and is not essential for the solution.

## Automating the building of applications

Let us start of with creating a new python file called `build_automation.py`. Here we can write our new build automation so that the configuration is set once and controlled by our version control system. This gives the benefits of keeping track of any changes in the builds and we can go back and change the solution. From the [pyinstaller documentation](https://pyinstaller.readthedocs.io/en/stable/usage.html#running-pyinstaller-from-python-code) we can find a code snippet for running the installer from a python file:

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

First we need to import the `__main__.py` python file from the PyInstaller package, which contains the `run()` function we need to automate the build process. Additionally we need to import the builtin `os` module to match the [pyinstaller documentation](https://pyinstaller.readthedocs.io/en/stable/usage.html#running-pyinstaller-from-python-code) for calling Pyinstaller from python code.

We have chosen the following arguments to keep in our `build_config` list:

* `--onefile` results in our package is build into a single file
* `-n=` renames the resulting build output, in our case to `todo`
* `--clean` makes sure that the previous build output is deleted before building the next part.
* `os.path.join()` is used to format the path to our `todo.py`. We could also have written `"./todo.py"` which is the outcome of the join function.

In the end of the file we call the `run()` function with the argument `build_config` to start the packaging process every time the build script is called.

> **Note:** The import of the module and subsequent function call may seem a bit strange, but is just because the file that contains the run function is stored in the `__main__.py` file inside the Pyinstaller package, and has a special meaning. If you chose to run the module using `python -m pyinstaller` this would be the file that was called by the python interpreter. Try to look for other packages which have a `__main__.py` in their package folder in some of the packages you have installed. Having the `run`-function being executed like this in the script means that if you at some point import `build_automation.py` into another python script the installer will run during import. This is easily solved by wrapping the function call in a main function and calling this specifically, but has been left out intentionally for the sake of brevity.

Now we can build the application as many times as we like using and make sure we test on the latest changes in the application:

```shell

c:\Code> python build_automation.py

```

## Final notes

In order to perform the same test of the application we start the **todo.exe** from the **dist** folder either from the command line or from the Windows File Explorer. The application works the same way as when we tested the python script, the only difference is that we now can move it to any Windows computer, without having to install python. This reminds me of a quote from one of my favorite authors:

> "*Begin with the end in mind*" - Stephen Covey, author of "7 Great Habits of Highly effective People"

I think there is a lot of truth about delivering and developing software in this quote because the developer has to think of the end users and how they will be using the application. When I am developing applications, I consider the consequences of handing the resulting application to my parents, who by no means are considered computer savvy. It should be easy for them to use the application and the application should behave the way they would expect. This means that I cannot rely on them to remember to type command line incantation to start or run the application. This is a bar which they are never going to reach, let alone pass. Based on this I cannot just hand them a python script and expect them to know how to run this out of the box. Python scripts are for developers and applications are for all people.

Some may argue that it takes too long to get the build system setup and they would rather wait until the product is finished to package and build the application. This is a bad solution. The main reason is that if you as a developer do not introduce this as early as possible certain assumptions will be included in your code, such as user using a different decimal point, or does not have a specific folder you have on your PC, and so on. Additionally you know that your application is not going to change because the user installed a different version of a crucial dependency for your application. This is all packaged into the product application

Through this article we have automated a part of a solid application foundation for packaging our desktop applications with deployment in mind. From here we can start to add all the customer requirements and develop all the features that the customer needs. We no longer have to worry about forgetting to set the build parameters right and we can focus on the process of writing the code. Additionally we can easily perform our tests on the actual product and not skip any steps when testing. I have specifically kept the process of dependencies out of this article in order to keep the article light and compact, but if you run into the trouble I am sure that you are capable of automating that and extend the build automation script.
