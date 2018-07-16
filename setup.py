from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='AkidaSDK',
    version='0.0.1',
    packages=find_packages(exclude=("tests",)),
    url='',
    author='AkidaDev',
    author_email='',
    description='SDK for developing Akdia distributed apps',
    install_requires=required,
    include_package_data=True,
    package_data={},
    entry_points={}
)
