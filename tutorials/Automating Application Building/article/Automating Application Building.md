# Automating the Desktop Applications Building process with Python

Most python code is developed for other python users or web applications and not for desktop users who do not have Python installed. Therefore packaging your application up for delivery to non-python users is a grey area in the world of Python. This is why tools like Pyinstaller was created. It improves the packaging process for developing applications that can be distributed to non-python users. This comes with another set of challenges where getting consistent outcomes is dependent on remembering command-line arguments when invoking the packaging function.

This tutorial will focus on automating the process of packaging desktop applications with Pyinstaller, so you easily can run the **packaging** automation as a normal python script. Additionally, your script can track the settings in your version control system, such as Git.

**In this tutorial, you will learn**:

* When is it the best time to implement the **packaging** process.
* How to implement the basics of **packaging** for delivering to non-python users.
* How to call PyInstaller with consistent arguments from a simple Python script

Here are some of the reasons why packaging up applications for the end-user below is important.

* Packaging up an application to be installed on a system solves many problems with regards to environments and system compatibility.
* There is **no** need to install Python to use the application features because the application is packaged with all the requirements.
* There is **no** need to know the Python language or even know that the application is even written in python. It is just a normal application performing its features.

Additionally, it makes you think about testing and using your end product in the same way as the end-user, instead of running a script through an interpreter. If the usage of the application end product is sub-optimal for you, it will also be sub-optimal for your users. The good solution is to catch this early in the process, so let's get started.

## Setting up the Development Environment

Before you develop the application, let's make sure that your environment is set up correctly, so you have all the tools for building the application. If you are unsure about how to proceed, the links provide access to additional information on the specific topics to install and work with:

1. Install Python 3.5 or above. I use [Python 3.8](https://www.python.org/downloads/release/python-385/) while writing the tutorial
2. Create and activate a [Virtual Environment](https://realpython.com/python-virtual-environments-a-primer/)
3. Install [pyinstaller](https://realpython.com/pyinstaller-python/) in the activated environment using [pip](https://realpython.com/what-is-pip/)

After all these steps you're ready to build your application.

## Creating the application skeleton

The application will be called **Todo** and takes the user input in the form of a text command. It is not vitally important that you have the same version but as long as you use Python 3 on Windows, this should be enough. Open a text editor and start by creating a python file named `todo.py` for your main application functionality with the following content:

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

* Startup without errors
* Print the welcome message
* Shut down when you send the `Q` command
* Print the exit message

> **Tip**: Using the `print(__doc__)` at the beginning of the code is a nifty feature that makes sure that anything you put into the todo.py documentation in the top will be printed when the program starts. There are other options, but these are outside the scope of the article.

This is the absolute bare bones of any application, which can be tested.

## Test, Verify and Increment

**Testing at this step before packaging is important** because you now know that the application does not have any syntactical errors or strange behavior, and reacts to user inputs. The reason for doing this test so early in the process, where the application still really simple and easy to understand, is to eliminate the complications of building the application. This is key to building applications in general, that you make small increments and solve the problems you run into in before moving on to implementing the next feature.

Consider the opposite case where you write more than 1000 lines of application code before testing. How do you know the code works and how much of it works? Another bad solution is to package the application as the last part of the delivery of the application, and then you discover a bug in the packaged application. This is not fun and is the straight road to stress and bad solutions.

## Building from the command line

It's time to get specific before you start building. Your end-user would like the application to be combined into a single file for easy distribution and easy deployment for your users. Reading the documentation for Pyinstaller this can be done with the `--onefile` flag. Let's try that from the command line for now:

```shell
c:\Code> pyinstaller todo.py --onefile
```

After the process of building the application has finished you can see that it adds some things to your project folder. It creates two new folders, called **build** and **dist** and it creates a `todo.spec` file. These are the outcomes of the build process, and the folder structure changes can be seen below:

```shell
Project folder
    |-- build
    |-- dist
  |-- todo.py
  |-- todo.spec
```

In the **dist** folder you find your new Windows program, all ready to hand over someone, who does not have Python on their system.

> Note: Packaged files and outcomes of a build process are often referred to as **build artifacts** or just **artifacts**.

One thing to think about when building applications is that in order to build your program again after you have changed something in the python code, you need to delete the **dist** folder and run the `pyinstaller` command again with the same arguments to get the application compiled. This may bring some questions to your mind such as:

* What happens if you forget to add the `--onefile` argument to the command?
* What happens if you forget to delete the old artifact and should you do that manually?

If only there were a way to package our application from a build script, where we could define all the settings once and for all. We are in luck because the PyInstaller is just python code, so we can make a python build script, that we can use to automate the building of our applications, with the same configurations every time the application is run. Let us get started on making our lives a bit easier.

> **Note:** We will disregard the **build** folder and only focus on the **dist** folder for now since the purpose of the **build** folder is documented in the Pyinstaller documentation and in several tutorials elsewhere, and is not essential for the solution.

## Automating the building of applications

Let's start by creating a new python file called `build_automation.py` in the project folder next to the `todo.py`. This is your new build automation script. Here the configuration is set once and controlled by your version control system. This gives the benefits of keeping track of any changes in the builds and you can go back and change the solution. From the [pyinstaller documentation](https://pyinstaller.readthedocs.io/en/stable/usage.html#running-pyinstaller-from-python-code) you can find a code snippet for running the installer from a python file. An implementation of the build process has been implemented below:

```python
"""
build_automation.py
This is a script that is used to automate the process of the application ToDo.
"""
# according to the Pyinstaller documentation you must import the special __main__ module
# in the package to package up the application.

import PyInstaller.__main__
import os

# This is our package configuration and all the arguments we would like to add to the application
build_config = [
    "-n=todo",
    "--clean",
    "--onefile",
    os.path.join(".","todo.py"),
]

# calling the build function from the PyInstaller package
PyInstaller.__main__.run(build_config)
```

First, you need to import the `__main__.py` python file from the PyInstaller package, which contains the `run()` function needed to automate the build process. Additionally you need to import the builtin `os` module to match the [pyinstaller documentation](https://pyinstaller.readthedocs.io/en/stable/usage.html#running-pyinstaller-from-python-code) for calling Pyinstaller from python code.

We have chosen the following arguments to keep in your `build_config` list:

* `--onefile` results in your package is build into a single file
* `-n=` renames the resulting build output, in your case to `todo`
* `--clean` makes sure that the previous build artifact is deleted before building the next artifact.
* `os.path.join()` is used to format the path to your `todo.py`. You could also have written `"./todo.py"` which is the outcome of the join function.

At the end of the file, the `run()` function is called with the argument `build_config` to start the packaging process every time the build script is run.

The import of the module and subsequent function call may seem a bit strange but is just because the file that contains the run function is stored in the `__main__.py` file inside the Pyinstaller package, and has a special meaning. If you chose to run the module using `python -m pyinstaller` this would be the file that was called by the python interpreter. Try to look for other packages that have a `__main__.py` in their package folder in some of the packages you have installed. Having the `run`-function being executed like this in the script means that if you at some point import `build_automation.py` into another python script the installer will run during import. This is easily solved by wrapping the function call in a main function and calling this specifically but has been left out intentionally for the sake of brevity.

Now you can build the application as many times as you like using and make sure you test on the latest changes in the application:

```shell

c:\Code> python build_automation.py

```

The packaging process begins and with the settings from the `build_config` list in the `build_automation.py`.From this point on your application will be packaged with the same settings each time you run the script. To perform the functional test of the application you launch the **todo.exe** from the **dist** folder either from the command line or from the Windows File Explorer. You test that the application works the same way as when you tested the python script. The only difference is that you now can move it to any Windows computer, without having to install python.

## Start packaging

> "Begin with the end in mind" - Stephen Covey, author of "7 Great Habits of Highly Effective People"

Early in the development process, it is important to consider how the final delivery of the product is supposed to be. This is imperative for you as a software developer and particularly important for developing desktop applications for non-python users. Choosing the right path for the end product as early as possible reduces the development time significantly.

> In the `todo.py` example, the final product was a single executable file text-based interface with a prompt to deliver to customers on a Windows PC without the need for a Python interpreter.

Given that problem statement for the application, you can derive the following requirements:

* The end product must be a single executable file and run without the Python interpreter
* It must run on Windows
* The usage of the application is text-based and not GUI-based
* The application must prompt the user for input commands

These four things set the earliest requirements for the application. The first part is solved by solving the packaging problem. The second part is done by using PyInstaller for packaging on a Windows PC. This produces a binary executable file for Windows only. Narrowing the application deployment scope to a single platform will simplify much code later in the development of the application. The disregard for the need for a graphical user interface reduces complexity for the development process.

Keep in mind that the user can only use any version of the application, when the packaging has been solved, so solve this as early as possible. Automating the packaging makes the whole process run consistently for you and simplifies your development process.

## Improve the user experience early on

Do you remember the trick with using the `print(__doc__)` in the application? This is sort of a hidden requirement, but any good software solution should be able to start and stop without errors. There should be a simple and intuitive way to do so. Just as starting Python from the command line and exiting this again using `CTRL-Z` or `exit()`. The first feature to implement is how to close the application properly. At some point, the intro message to the application can be exchanged with a list of commands which can be distributed from a configuration file.

## Conclusion

Congratulations on finishing this article. You have now learned how to get started with automating the building of Python-based Windows applications, using PyInstallers Python API. The article forms a basis for easing the packaging process of Python applications, and to alleviate the stress of packaging application by automation as early in the process as possible. You have additionally learned:

* How to package a python module into an executable from the command line
* When to implement packaging and what to consider when building applications
* How to setup consistent build settings and how to control the PyInstaller API with these

The source code for the provided examples is available on [Github](https://github.com/JayKayAce/Technical-Articles/tree/master/tutorials/Automating%20Application%20Building/code).

Start practicing the new superpowers of application building automation today. This will help you focus on the delivery and quality of the features you implement. Good luck!
