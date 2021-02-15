import setuptools

setuptools.setup(name='bq2ff',
      version='0.2',
      description='Bigquery to flatfile',
      url='https://github.com/vernium42/bq2ff',
      author='Vernium42',
      license='MIT',
      install_requires=['numpy==1.20.1', 'pandas==1.2.2', 'pyarrow==3.0.0', 'python-dateutil==2.8.1', 'pytz==2021.1', 'six==1.15.0'],
      packages=setuptools.find_packages())
