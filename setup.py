#!/usr/bin/env python
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

from setuptools import setup

setup(
    name='virtualenvwrapper.tryton',
    version='0.2',

    description="Tryton virtualenvwrapper plugin",
    long_description=open('README.rst').read(),

    author='Openlabs',
    author_email='support@openlabs.co.in',

    url='https://github.com/openlabs/virtualenvwrapper.tryton',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Framework :: Django',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    platforms=['Any'],

    provides=['virtualenvwrapper.tryton'],
    requires=[
        'invoke',
        'blessing',
        'hgapi',
        'virtualenv',
        'virtualenvwrapper (>=4.0)',
    ],

    namespace_packages=['virtualenvwrapper'],
    packages=['virtualenvwrapper'],
    include_package_data=True,
    entry_points={
        'virtualenvwrapper.project.template': [
            'tryton = virtualenvwrapper.tryton_project:template_develop',
            'tryton_invoke = virtualenvwrapper.tryton_project:template_invoke',
            'tryton30 = virtualenvwrapper.tryton_project:template30',
            'tryton28 = virtualenvwrapper.tryton_project:template28',
            'tryton26 = virtualenvwrapper.tryton_project:template26',
            'tryton24 = virtualenvwrapper.tryton_project:template24',
            'tryton22 = virtualenvwrapper.tryton_project:template22',
            'tryton20 = virtualenvwrapper.tryton_project:template20',
            'tryton18 = virtualenvwrapper.tryton_project:template18',
            'tryton16 = virtualenvwrapper.tryton_project:template16',
            'tryton14 = virtualenvwrapper.tryton_project:template14',
            'tryton12 = virtualenvwrapper.tryton_project:template12',
            'tryton10 = virtualenvwrapper.tryton_project:template10',
        ],
    },

    zip_safe=False,
)
