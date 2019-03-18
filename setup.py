
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mtl_to_xml",
    version="0.1",
    packages=find_packages(),
    scripts=['mtl_to_xml.py'],
    author="Adam Russnogle",
    author_email="adamrussnogle@gmail.com",
    description="Convert Landsat MTL metadata to XML.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/and-viceversa/mtl_to_xml",
    license=open('UNLICENSE').read(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Unlicense',
        'Topic :: Landsat :: data conversion']

)
