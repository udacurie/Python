try:
	from setuptools import setup
	
except ImportError: #Raised when an import statement fails.
	from distutils.core import setup
	
config = {
	'description': 'My Project',
	'author':'NT',
	'url': 'URL to get it at.',
	'download_url' : 'Where to download it',
	'author_email' : 'My email.',
	'version' : '0.1',
	'install_requires' : ['nose'],
	'packages' : ['ex47'],
	'scripts' : [],
	'ex47': 'projectex47'	
	}
	
setup(**config)
	
