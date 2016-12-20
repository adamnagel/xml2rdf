from setuptools import setup

kwargs = {
    'author': 'Adam Nagel',
    'author_email': 'adam.nagel+git@gmail.com',
    'classifiers': ['Intended Audience :: Science/Research',
                    'Topic :: Scientific/Engineering'],
    'description': 'RDF converter package for XML files',
    'download_url': '',
    'entry_points': '',
    'include_package_data': True,
    'install_requires': ['rdflib'],
    'keywords': ['rdf, xml'],
    'license': 'MIT',
    'maintainer': 'Adam Nagel',
    'maintainer_email': 'adam.nagel+git@gmail.com',
    'name': 'xml2rdf',
    'package_dir': {'xml2rdf': 'xml2rdf'},
    'packages': ['xml2rdf'],
    'url': '',
    'version': '0.1',
    'zip_safe': False}

setup(**kwargs)