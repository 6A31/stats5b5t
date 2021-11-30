from setuptools import setup, find_packages

VERSION = '0.1.0' 
DESCRIPTION = 'API Wrapper for 5b5t.org'
LONG_DESCRIPTION = 'Automate and simplify api requests  for 5b5t.org'

setup(
       # the name must match the folder name 'verysimplemodule'
        name="stats5b5t", 
        version=VERSION,
        author="ScobraScope",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            "requests"
        ],
        keywords=['python', 'api', ''],
        classifiers= [
            "Operating System :: Microsoft :: Windows",
        ]
)