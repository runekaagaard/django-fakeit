# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-fakeit',
    version='0.1.0',
    author=u'Rune Kaagaard',
    author_email='rumi.kg@gmail.com',
    packages=find_packages(),
    url='https://github.com/runekaagaard/django-fakeit',
    license='BSD licence, see LICENCE',
    description='Anonymizes a Django database. Fast.' ,
    long_description=open('README.md').read(),
    zip_safe=False,
)