#!/bin/env/python  
#filename:setup.py  
  
try:  
        from setuptools import setup  
except ImportError:  
        from distutils.core import setup  
  
config = {  
        'description': 'project name',  
        'author': 'ower name',  
        'url': 'URL to get it at.',  
        'download_url': 'Where to download it.',  
        'author_email': 'My email.',  
        'version': 'o.1',  
        'install_requires': ['nose'],  
        'packages': ['NAME'],  
        'scripts': [],  
        'name': 'projectname'  
}  
  
setup(**config)  