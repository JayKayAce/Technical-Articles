import PyInstaller.__main__
import os

install_config = [
    "name=todo",
    "--clean",
    "--onefile",
    "scriptname todo.py"
]

PyInstaller.__main__.run(pyi_args=install_config)