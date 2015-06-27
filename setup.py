from setuptools import setup

setup(name='mundipagg-python-api',
      version='1.1',
      description="Mundipagg API",
      long_description="",
      author='Gil Lessa',
      author_email='desenv@arcarius.com.br',
      license='Apache License v2.0',
      packages=['mundipagg'],
      zip_safe=False,
      install_requires=[
          'suds-jurko',
      ],
      )
