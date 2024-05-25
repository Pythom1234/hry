#!/usr/bin/python3

import os

if os.name == 'posix':
    try:
        os.chdir(os.path.expanduser('~')+'/.pydownload')
    except:
        os.system('mkdir ~/.pydownload')
        os.system('python3 -m venv ~/.pydownload/venv')
        os.system(f'source ~/.pydownload/venv/bin/activate; python3 -m pip install --upgrade pip')
        os.chdir(os.path.expanduser('~')+'/.pydownload')

    os.system('rm -rf program')
    os.system('git clone -qb program https://github.com/Pythom1234/projects.git')
    os.system('mv projects program')
    os.system('python3 program/main.py')
