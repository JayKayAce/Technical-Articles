import PyInstaller.__main__

install_config = [
    "todo.py",
    "-n todo",
    "--clean",
    "--onefile",
]

PyInstaller.__main__.run(install_config)