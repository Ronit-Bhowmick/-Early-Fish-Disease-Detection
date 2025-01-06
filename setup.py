import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "0.0.1"

REPO = "-Early-Fish-Disease-Detection"
AUTHOR_NAME = "Ronit Bhowmick"
AUTHOR_EMAIL = "ronitbhowmick506@gmail.com"
PROJECT_NAME = "Early Fish Disease Detection"


setuptools.setup(
    name=PROJECT_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Early Fish Disease Detection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com{AUTHOR_NAME}{REPO}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),  
)
