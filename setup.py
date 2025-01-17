#!/usr/bin/env python

from setuptools import setup, find_packages


def main():
    with open('README.md') as f:
        readme = f.read()

    with open('LICENSE') as f:
        license = f.read()

    metadata = dict(
        name='Open-Burnup',
        version='0.1.0',
        description='Open Source depletion code',
        long_description=readme,
        author='Julien de Troullioud de Lanversin',
        author_email='jdtdl@princeton.edu',
        url='http://jdtdl.mycpanel.princeton.edu/',
        license=license,
        packages=find_packages(exclude=('docs', 'graphs', 'notes', 'papers', 'test', 'test_nouveau')),
        package_data = {'openbu':['data/default_libs/*', 'data/other_libs/argonne/*', 'data/other_libs/ENDFVIII/*','data/other_libs/jeff33/*','data/isomeric_data/eaf-2010-multiplicities/*']}

    )

    setup(**metadata)


if __name__ == '__main__':
    main()

