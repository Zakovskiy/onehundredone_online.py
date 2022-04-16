from setuptools import setup, find_packages

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name = "onehundredone_online.py",
    version = "2.0.0",
    url = "https://github.com/Zakovskiy/onehundredone_online.py",
    download_url = "https://github.com/Zakovskiy/onehundredone_online.py/tarball/master",
    license = "MIT",
    author = "Zakovskiy",
    author_email = "gogrugu@gmail.com",
    description = "A library to create 101 Online bots.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords = [
        "durak",
        "online",
        "onehundredone_online.py",
        "onehundredone.py",
        "101-bot",
        "101.py",
        "rstgame",
        "rstgames",
        "api",
        "socket",
        "python",
        "python3",
        "python3.x",
        "zakovskiy",
        "official"
    ],
    install_requires = [
        "setuptools",
        "requests",
        "loguru",
    ],
    setup_requires = [
        "wheel"
    ],
    packages = find_packages()
)
