import pathlib
from setuptools import setup, find_packages
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

VERSION = '0.1.5' 
DESCRIPTION = 'API Wrapper for 5b5t.org'


setup(
       # the name must match the folder name 'verysimplemodule'
        name="stats5b5t", 
        version=VERSION,
        author="ScobraScope",
        url="https://github.com/ScobraScope/stats5b5t",
        description=DESCRIPTION,
        long_description=README,
        packages=find_packages(),
        long_description_content_type='text/markdown',
        install_requires=[  
            "requests"
        ],
        keywords=['python', 'api', '5b5t', 'minecraft', 'wrapper'],
        classifiers= [
            "Operating System :: Microsoft :: Windows",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Natural Language :: English",
            "Programming Language :: Python :: 3.9",
            "Topic :: Games/Entertainment", 
        ]
)