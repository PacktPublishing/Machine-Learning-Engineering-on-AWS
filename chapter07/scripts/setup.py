from setuptools import setup, find_packages

setup(name='distillbert',
      version='1.0',
      description='distillbert',
      packages=find_packages(exclude=('tests', 'docs')))