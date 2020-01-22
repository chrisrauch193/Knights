
from setuptools import setup, find_packages

setup(
    name='Knights',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Knights Game',
    long_description=open('README.md').read(),
    url='https://github.com/chrisrauch193/Knights',
    author='chrisrauch193',
    author_email='chrisrauch193@gmail.com'
)
