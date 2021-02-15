import os
import setuptools

folder_path = os.path.dirname(os.path.realpath(__file__))
requirements = folder_path + '/requirements.txt'
with open(requirements) as f:
      requires = f.read().splitlines()

setuptools.setup(name='bq2ff',
      version='0.2',
      description='Bigquery to flatfile',
      url='https://github.com/vernium42/bq2ff',
      author='Vernium42',
      license='MIT',
      install_requires=requires,
      packages=setuptools.find_packages())
