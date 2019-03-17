
from setuptools import setup, find_packages

setup(
    name="mtl_to_xml",
    version="0.1",
    packages=find_packages(),
    scripts=['mtl_to_xml.py'],
    author="Adam Russnogle",
    description="Convert Landsat MTL metadata to XML.",
    license=open('UNLICENSE').read(),
    classifiers=['Topic :: Landsat :: data conversion']
)
