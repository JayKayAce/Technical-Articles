import PyInstaller.__main__

install_config = [
    "-n=todo",
    "--clean",
    "--onefile",
    "./todo.py",
]

PyInstaller.__main__.run(install_config)