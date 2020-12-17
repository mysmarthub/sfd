#!/usr/bin/env python
# -----------------------------------------------------------------------------
# Copyright © 2020 Aleksandr Suvorov
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
# Aleksandr Suvorov
# Email: myhackband@yandex.ru
# Github: https://github.com/mysmarthub/sfd/
# -----------------------------------------------------------------------------
"""Smart Console utility for destroying, zeroing, and deleting files."""
import argparse
import sys
import shutil
import os
from pathlib import Path
from mycleaner import smart
from mycleaner import cleaner
import datetime


COLUMNS, _ = shutil.get_terminal_size()
VERSION = 'v0.0.3'


def get_num_files(path):
    if Path(path).is_dir():
        return sum([len(files) for _, _, files in os.walk(path)])
    elif Path(path).is_file():
        return 1
    else:
        return 0


def logo_start():
    print('SmartTerminal Files Destroyer'.center(COLUMNS, '='))
    print('Aleksandr Suvorov | myhackband@ya.ru'.center(COLUMNS, '-'))
    print('Utility for mashing, zeroing, deleting files'.center(COLUMNS, '='))


def logo_end():
    print(''.center(COLUMNS, '='))
    print('The program is complete'.center(COLUMNS, '-'))


def get_path():
    if len(sys.argv) > 1:
        return [path for path in sys.argv[1:] if Path(path).exists() and (Path(path).is_file() or Path(path).is_dir())]


def logo_dec(func):
    def deco():
        print('Smart Terminal Files Destroyer'.center(COLUMNS, '='))
        print('Aleksandr Suvorov | myhackband@ya.ru'.center(COLUMNS, '-'))
        print('Utility for mashing, zeroing, deleting files'.center(COLUMNS, '='))
        func()
        print(''.center(COLUMNS, '='))
        print('The program is complete'.center(COLUMNS, '-'))
    return deco


def make_error_log(error_list):
    name = 'sfd_err_log.txt'
    with open(name, 'w') as f:
        print(f'Errors {datetime.datetime.now()}'.center(COLUMNS, '='), file=f)
        for err in error_list:
            print(err, file=f)
    print(f'Save {name}')


def createParser():
    parser = argparse.ArgumentParser(
        description='Console utilities for destroying, zeroing, and deleting files',
        prog='SmartTerminal Files Destroyer',
        epilog="""https://githib.com/mysmarthub/sfd""",
    )
    parser.add_argument('paths', nargs='+', help='Paths to files and folders')
    parser.add_argument('--log', help='Save errors log',
                        action='store_const', const=True, default=False)
    parser.add_argument('--version', action='version', help='Program version', version='%(prog)s {}'.format(VERSION))
    return parser


def status_print(status):
    print(''.center(COLUMNS, '-'))
    if status:
        print('Done!')
    else:
        print('Error!')


def work(obj_dict, method=1, log=False):
    my_cleaner = cleaner.Cleaner()
    while True:
        try:
            my_cleaner.shreds = int(input('Enter the number of overwrites for files: '))
        except ValueError:
            my_cleaner.shreds = 30
        break
    for obj in obj_dict.values():
        print(f'Working with: {obj.path}'.center(COLUMNS, '='))
        for file in obj.get_files():
            status = None
            if method == 1:
                print(f'Destroying the file: {file}')
                status = my_cleaner.shred_file(file)
            elif method == 2:
                print(f'Resetting the file: {file}')
                status = my_cleaner.zero_file(file)
            elif method == 3:
                print(f'Delete files: {file}')
                status = my_cleaner.del_file(file)
            status_print(status)
    print('The work has been completed'.center(COLUMNS, '='))
    print(f'Files were processed: {my_cleaner.count_del_files + my_cleaner.count_zero_files}')
    print(f'Errors: {len(my_cleaner.errors)}')
    if log and my_cleaner.errors:
        make_error_log(my_cleaner.errors)
    my_cleaner.reset_error_list()


def print_info(obj_dict):
    print(f'Counting files...')
    for val in obj_dict.values():
        print(f'path: {val.path} | files[{val.num_of_files}] | folders[{val.num_of_dirs}]')
    print(f''.center(COLUMNS, '-'))


def make_path_obj(path_list):
    return {n: smart.PathObj(path) for n, path in enumerate(path_list, 1)} if path_list else False


def make_path_list(path_list):
    return [path for path in path_list if Path(path).exists()]


def get_user_input(obj_dict):
    while True:
        num_files = sum(obj.num_of_files for obj in obj_dict.values())
        if not num_files:
            print('No files found...')
            break
        print('Select the desired action:\n0. Exit\n1. Destruction and delete\n2. '
              'Zeroing not delete\n3. Zeroing and delete')
        print(''.center(COLUMNS, '-'))
        try:
            user_input = int(input('Input: '))
            if user_input not in [0, 1, 2, 3]:
                raise ValueError
        except ValueError:
            print(''.center(COLUMNS, '-'))
            print('Input error!')
            continue
        else:
            return user_input


def main():
    parser = createParser()
    namespace = parser.parse_args()
    logo_start()
    path_list = make_path_list(namespace.paths)
    if path_list:
        print(f'Paths added: {len(path_list)}')
        obj_dict = make_path_obj(path_list)
        print_info(obj_dict)
        user_input = get_user_input(obj_dict)
        if user_input:
            work(obj_dict=obj_dict, method=user_input, log=namespace.log)
    else:
        print('Error! You haven\'t added a path...')
    logo_end()


if __name__ == '__main__':
    main()
