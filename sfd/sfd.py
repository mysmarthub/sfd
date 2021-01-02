#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE.txt.txt for details)
# Copyright © 2020 Aleksandr Suvorov
# -----------------------------------------------------------------------------
"""Smart Console utility for destroying (shred), zeroing, and deleting files."""
import argparse
import datetime
import shutil

from pathlib import Path

from mycleaner import smart
from mycleaner import cleaner


COLUMNS, _ = shutil.get_terminal_size()
VERSION = '0.0.6'


def check_path(path):
    return True if Path(path).exists() else False


def make_error_log(error_list):
    name = 'sfd_err_log.txt'
    with open(name, 'w') as file:
        print(f'Errors {datetime.datetime.now()}'.center(COLUMNS, '='), file=file)
        for err in error_list:
            print(err, file=file)
    print(f'Save {name}')


def status_print(status):
    if status:
        print('Done!')
    else:
        print('Error!')
    print(''.center(COLUMNS, '-'))


def work(obj_dict, method=1, log=False, shreds=30):
    my_cleaner = cleaner.Cleaner()
    my_cleaner.shreds = shreds
    path_count = 0
    for obj in obj_dict.values():
        path_count += 1
        print(f'{path_count} Working with: {obj.path}'.center(COLUMNS, '='))
        count = 0
        for file in obj.get_files():
            count += 1
            status = None
            if method == 1:
                print(f'{count} Destroying the file: {file}')
                status = my_cleaner.shred_file(file)
            elif method == 2:
                print(f'{count} Resetting the file: {file}')
                status = my_cleaner.zero_file(file)
            elif method == 3:
                print(f'{count} Delete files: {file}')
                status = my_cleaner.del_file(file)
            status_print(status)
    print('The work has been completed'.center(COLUMNS, '='))
    print(f'Files were processed: {my_cleaner.count_del_files + my_cleaner.count_zero_files}')
    print(f'Errors: {len(my_cleaner.errors)}')
    if log and my_cleaner.errors:
        make_error_log(my_cleaner.errors)
    my_cleaner.reset_error_list()
    my_cleaner.reset_count()


def make_path_obj(path_list):
    if path_list:
        return {n: smart.PathObj(path) for n, path in enumerate(path_list, 1)}
    return False


def make_path_list(path_list):
    path_list = set(path_list)
    return [path for path in path_list if Path(path).exists()]


def createParser():
    parser = argparse.ArgumentParser(
        description='Smart Console utility for destroying (shred), zeroing, and deleting files',
        prog='Smart Files Destroyer',
        epilog="""https://github.com/mysmarthub/sfd""",
    )
    parser.add_argument('--p', '--paths', nargs='+', help='Paths to files and folders')
    parser.add_argument('--o', '--overwrites', type=int, help='Number of overwrites', default=0)
    parser.add_argument('--s', help='Shredding and delete file', action='store_const', const=True, default=False)
    parser.add_argument('--z', help='Zeroing no delete file', action='store_const', const=True, default=False)
    parser.add_argument('--d', help='Zeroing and delete file', action='store_const', const=True, default=False)
    parser.add_argument('--log', help='Save errors log', action='store_const', const=True, default=False)
    parser.add_argument('--version', action='version', help='Program version', version='%(prog)s v{}'.format(VERSION))
    return parser


def get_paths():
    path_list = []
    while True:
        print(''.center(COLUMNS, '-'))
        user_path = input('Enter the path to the file or folder or "q" + Enter to continue: ')
        if user_path in ['q', 'й']:
            if path_list:
                break
            else:
                print('\nError! You didn\'t add any paths.')
                continue
        elif check_path(user_path):
            path_list.append(user_path)
            print('Path added successfully')
            continue
        else:
            print('Error! The wrong way!')
            continue
    return path_list


def get_method():
    while True:
        print(''.center(COLUMNS, '-'))
        print('Select the desired action (Ctrl+C to exit):\n'
              '1. Destruction (shred) and delete\n'
              '2. Zeroing not delete\n'
              '3. Zeroing and delete')
        print(''.center(COLUMNS, '-'))
        try:
            user_input = int(input('Input: '))
            if user_input not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print(''.center(COLUMNS, '-'))
            print('Input error!')
            continue
        else:
            return user_input


def get_shreds():
    while True:
        try:
            shreds = int(input('Enter the number of file overwrites: '))
        except ValueError:
            print(''.center(COLUMNS, '-'))
            print('Input error!')
        else:
            return shreds


def get_args(func):
    parser = createParser()
    namespace = parser.parse_args()

    def deco():
        print(f'Smart Files Destroyer {VERSION}'.center(COLUMNS, '='))
        print(' Aleksandr Suvorov | https://githib.com/mysmarthub/sfd '.center(COLUMNS, '-'))
        print('Donate: 4048 4150 0400 5852 | 4276 4417 5763 7686'.center(COLUMNS, ' '))
        print('Utility for mashing, zeroing, deleting files'.center(COLUMNS, '='))
        func(namespace)
        print(''.center(COLUMNS, '='))
        print('The program is complete'.center(COLUMNS, '-'))
        print('Donate: 4048 4150 0400 5852 | 4276 4417 5763 7686'.center(COLUMNS, ' '))

    return deco


@get_args
def main(namespace):
    try:
        if not namespace.p:
            print('To work, specify the path/paths to the file/files folder/folders...')
            namespace.p = get_paths()
        path_list = make_path_list(namespace.p)
        if path_list:
            print(f'Paths added: {len(path_list)}')
            print(''.center(COLUMNS, '-'))
            obj_dict = make_path_obj(path_list)
            print(f'Counting files...')
            for val in obj_dict.values():
                print(f'path: {val.path} | files[{val.num_of_files}] | folders[{val.num_of_dirs}]')
            if not namespace.s and not namespace.z and not namespace.d:
                method = get_method()
                if method == 1:
                    namespace.s = True
                elif method == 2:
                    namespace.z = True
                else:
                    namespace.d = True
            if namespace.s:
                if not namespace.o:
                    namespace.o = get_shreds()
                method = 1
            elif namespace.z:
                method = 2
            else:
                method = 3
            work(obj_dict=obj_dict, method=method, log=namespace.log, shreds=namespace.o)
        else:
            print('Error! You haven\'t added a path...')
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
