import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weather-terminal", # Replace with your own username
    version="1.2.1",
    author="TheProgrammingArchive",
    author_email="TheProgrammingArchive@gmail.com",
    license="MIT",
    description="terminalWeather",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheProgrammingArchive/weather-terminal",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
