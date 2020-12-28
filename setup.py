from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='weather-terminal',
   version='1.0',
   description='Daily weather on your temrinal!',
   license="MIT",
   long_description=long_description,
   author='TheProgrammingArchive',
   author_email='TheProgrammingArchive@gmail.com',
   url="",
   contributors="TheProgrammingArchive, memerememe",
   github_url = "https://github.com/TheProgrammingArchive/weather-terminal/",
   packages=['weather-terminal'],  #same as name
   install_requires=['bs4', 'lxml', 'requests', 'art', 'tableprint'], #external packages as dependencies
)
