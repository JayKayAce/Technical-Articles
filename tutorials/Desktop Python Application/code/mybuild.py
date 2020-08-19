import PyInstaller.__main__
#import os

install_config = [
    "-n=todo",
    "--clean",
    "--onefile",
    "./todo.py",
]

PyInstaller.__main__.run(install_config)