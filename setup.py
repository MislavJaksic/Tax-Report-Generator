from setuptools import setup, find_packages


with open("README.rst") as f:
  readme = f.read()

setup(
  name="sample_package",
  version="0.1.0",
  description="Tax Report Generator",
  long_description=readme,
  
  author="Mislav Jaksic",
  author_email="jaksicmislav@gmail.com",
  url="https://github.com/MislavJaksic/Tax-Report-Generator",
  
  packages=find_packages(exclude=("tests", "docs")),
  
  entry_points={"console_scripts" : ["project_name = src.big_package.runner:Run"]} 
)

