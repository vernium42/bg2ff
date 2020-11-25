from setuptools import setup

setup(name='bq2ff',
      version='0.1',
      description='Bigquery to flatfile',
      url='https://github.com/vernium42/bq2ff',
      author='Vernium42',
      license='MIT',
      packages=['bq2ff', 'pandas', 'pyarrow', 'google-cloud-bigquery'])
