from setuptools import setup, find_packages

VERSION = '0.0.4' 
DESCRIPTION = 'Hashtag to text'
LONG_DESCRIPTION = 'The package is made for twitter, it add hashtag to know word in text'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="pyHashtag", 
        version=VERSION,
        author="Loan MAEGHT",
        author_email="qypol342@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['unidecode','requests','importlib_resources'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'

        # static file
        package_data = {
            '': ['*.json'],
        },
        
        keywords=['python', 'hashtag'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: Linux",
            "Operating System :: Microsoft :: Windows",
        ]
)