import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Chest-Disease-Classification-from-Chest-CT-Scan-Image"
AUTHOR_USER_NAME = "hariravikumar"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "harik76@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    #package_dir : The value of this option is a dictionary rather than a list. 
    #              Use it when your source code is not located directly in the same folder as setup.py. 
    #              The values you provide here will affect the way the values in the two previous arguments are used.
    #packages : Use this option to specify entire packages of code that should be part of your source. 
    #           When a package is included, any modules or packages inside it will also be part of the distribution 
    #           The value should be a list containing the name(s) of filesystem folder(s). 
    #           The named folders are expected to contain an __init__.py file.
)