from setuptools import setup, find_packages

setup(
  name="NAME",
  version="1.0.0",
  license="MIT",
  author="Bailey de Villiers",
  author_email="bailey.devilliers@gmail.com",
  packages=find_packages("scripts"),
  package_dir={'': "scripts"},
  url='https://github.com/itchysnake/NAME',
  keywords="",
  install_requires=[
  ],
)