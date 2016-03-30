#!/usr/bin/python
"""
ST Pipeline is a toolkit of Spatially resolved RNA-Seq data analysis for the Spatial Transcriptomics data.
"""

import os
import io
import glob
from setuptools import setup, find_packages
from stpipeline.version import version_number

# Get the long description from the relevant file
here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'stpipeline',
  version = version_number,
  description = __doc__.split("\n", 1)[0],
  long_description = long_description,
  keywords = 'rna-seq analysis spatial transcriptomics toolkit',
  author = 'Jose Fernandez Navarro',
  author_email = 'jose.fernandez.navarro@scilifelab.se',
  license = 'MIT',
  url = 'http://',
  packages = find_packages(exclude=('tests*', 'dependencies', 'utils')),
  include_package_data = False,
  package_data = {'': ['RELEASE-VERSION']},
  zip_safe = False,
  install_requires = [
    'HTSeq>=0.6.0',
    'setuptools',
    'pysam>=0.8.2',
    'invoke',
    'argparse',
    'scipy',
    'numpy',
    'taggd>=0.2.9',
    'pandas',
    'sqlitedict'
  ],
  test_suite = 'tests',
  scripts = glob.glob('scripts/*.py'),
  classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'Topic :: Software Development',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
    'License :: MIT :: Copyright Jose Fernandez Navarro',
    'Programming Language :: Python :: 2.7',
    'Environment :: Console',
  ],
)