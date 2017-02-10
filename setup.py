import os
from setuptools import setup, find_packages


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name='rest_bootstraptable_pagination',
    version='1.0.1',
    description='Django RestFramework pagination For bootstrap-table.',
    long_description=__doc__,
    author='Justin Chen',
    author_email='songhuagao@gmail.com',
    url='https://github.com/songhuagao/rest-bootstraptable-pagination',
    license='MIT',
    platforms='any',
    packages=find_packages(),
    install_requires=read('requirements.txt').splitlines(),
    zip_safe=False,
)
