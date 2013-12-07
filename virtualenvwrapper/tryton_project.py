# -*- coding: utf-8 -*-
'''

    Create Tryton projects automatically with virtualenvwrapper.

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Ltd.
    :license: BSD, see LICENSE for more details

'''
import logging
import os
import subprocess

log = logging.getLogger('virtualenvwrapper.tryton')

template30 = lambda args: template(args, '3.0')
template28 = lambda args: template(args, '2.8')
template26 = lambda args: template(args, '2.6')
template24 = lambda args: template(args, '2.4')
template22 = lambda args: template(args, '2.2')
template20 = lambda args: template(args, '2.0')
template18 = lambda args: template(args, '1.8')
template16 = lambda args: template(args, '1.6')
template14 = lambda args: template(args, '1.4')
template12 = lambda args: template(args, '1.2')
template10 = lambda args: template(args, '1.0')


def template_develop(args):
    """
    Install the latest development version of tryton
    """
    project, project_dir = args

    os.chdir(project_dir)

    subprocess.check_call([
        'hg', 'clone', 'http://hg.tryton.org/trytond'
    ])
    os.chdir(os.path.join(project_dir, 'trytond'))
    subprocess.check_call(['git', 'checkout', 'develop'])
    subprocess.check_call(['python', 'setup.py', 'install'])

    os.chdir(project_dir)
    subprocess.check_call(['mkdir', 'etc'])
    os.chdir(os.path.join(project_dir, 'etc'))
    subprocess.check_call(
        ['cp', '../trytond/etc/trytond.conf', 'trytond.conf']
    )

    os.chdir(project_dir)
    return


def template_invoke(args):
    """
    Install based on an invoke template
    """
    subprocess.check_call([
            'hg', 'clone', 'ssh://hg@bitbucket.org/nantic/tryton-utils',
            'tasks'
    ])
    subprocess.check_call(['invoke', 'bs'])
    return


def template(args, version):
    """
    * Installs Tryton
    * Creates an etc folder with the tryton config file
    """
    project, project_dir = args

    os.chdir(project_dir)

    major_version, minor_version = version.split('.', 2)
    major_version = int(major_version)
    minor_version = int(minor_version)

    subprocess.check_call([
        'pip',
        'install',
        'trytond >= %s.%s, < %s.%s' % (
            major_version, minor_version, major_version, minor_version + 1
        )
    ])
    log.info('Creating trytond.conf')
    subprocess.check_call(['mkdir', 'etc'])
    os.chdir(os.path.join(project_dir, 'etc'))
    subprocess.check_call([
        'curl',
        '-O',
        'https://raw.github.com/tryton/trytond/%s.%s/etc/trytond.conf' % (
            major_version, minor_version
        )
    ])

    os.chdir(project_dir)
    return
