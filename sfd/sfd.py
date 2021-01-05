#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details)
# https://github.com/mysmarthub
# Copyright © 2020-2021 Aleksandr Suvorov
# -----------------------------------------------------------------------------
"""Smart Console utility for destroying (shred), zeroing, and deleting files."""
import argparse
import datetime
import os
import shlex
import shutil

from pathlib import Path

COLUMNS, _ = shutil.get_terminal_size()
VERSION = '0.0.7'


def smart_print(text='', char='-'):
    columns, _ = shutil.get_terminal_size()
    print(f'{text}'.center(columns, char))


class PathObj:
    """Creates a path object for the file or folder."""

    @staticmethod
    def files_path_gen(path):
        return (os.path.join(p, file) for p, _, files in os.walk(path) for file in files)

    @staticmethod
    def dirs_path_gen(path):
        return (os.path.join(p, d) for p, dirs, _ in os.walk(path) for d in dirs)

    @staticmethod
    def get_num_of_dirs(path):
        return sum([len(dirs) for _, dirs, _ in os.walk(path)])

    @staticmethod
    def get_num_of_files(path):
        return sum([len(files) for _, _, files in os.walk(path)])

    def __init__(self, path: str):
        """When creating an object, you must specify a path that is checked for existence."""
        self.__path = path

    @property
    def path(self):
        """Path to the file or folder"""
        return self.__path

    def get_files(self) -> iter:
        """Returns the file path generator"""
        if os.path.isfile(self.__path):
            return [self.__path]
        elif os.path.isdir(self.__path):
            return (os.path.join(p, file) for p, _, files in os.walk(self.__path) for file in files)
        else:
            return []

    def get_dirs(self) -> iter:
        """Returns the folder path generator"""
        if os.path.isdir(self.path):
            return self.dirs_path_gen(self.__path)
        return []

    @property
    def num_of_files(self):
        return 1 if os.path.isfile(self.__path) else self.get_num_of_files(self.__path)

    @property
    def num_of_dirs(self):
        return self.get_num_of_dirs(self.__path)

    def __str__(self):
        return f'PathObj({self.__path})'


class DataObj:

    def __init__(self):
        self.__objects = {}

    def get_obj_gen(self):
        return (obj for obj in self.__objects.values())

    def get_obj_dict(self):
        return self.__objects

    def add_path(self, path: str) -> bool:
        if os.path.exists(path) and not self.search_for_duplicates(path) and not os.path.islink(path):
            self.__objects[path] = PathObj(path)
            return True
        return False

    def search_for_duplicates(self, path: str) -> bool:
        """Checking for duplicates"""
        return True if path in self.__objects else False

    def del_path(self, path: str) -> bool:
        """Deleting a path object"""
        if self.search_for_duplicates(path):
            del self.__objects[path]
            return True
        return False

    def get_files(self) -> iter:
        """Returns a generator with file paths from all objects"""
        return (file for obj in self.__objects.values() for file in obj.get_files())

    def get_dirs(self) -> iter:
        """Getting folders"""
        return reversed(sorted(path for obj in self.__objects.values() for path in obj.get_dirs()))

    @property
    def is_any_data(self) -> bool:
        """Checking for data in repositories"""
        return True if self.__objects else False

    def clear_data(self) -> None:
        """Clearing storage"""
        self.__objects.clear()


class Cleaner:
    """Creates an object for working with file and folder paths

    for further destruction, zeroing, deleting files. Delete a folder.
    """
    def __init__(self, root=False, shreds=30):
        """Accepts an optional parameter when creating an object shred:

        the number of passes to overwrite the file. By default, 30 passes.
        """
        self.errors = []
        self.root = root
        self.shreds = shreds
        self.count_zero_files = 0
        self.count_del_files = 0
        self.count_del_dirs = 0

    @staticmethod
    def replace_path(path: str) -> str:
        return shlex.quote(path)

    @staticmethod
    def check_exist(path):
        if os.path.exists(path):
            return True
        return False

    def zero_file(self, file: str) -> bool:
        """Resets the file to the specified path"""
        try:
            with open(file, 'wb') as f:
                f.write(bytes(0))
        except OSError:
            self.errors.append(f'Zeroing error: {file}')
            return False
        else:
            self.count_zero_files += 1
            return True

    def shred_file(self, path: str) -> bool:
        """Overwrites and deletes the file at the specified path"""
        rep_path = self.replace_path(path)
        if os.name == 'posix':
            if self.root:
                status = os.system(f'sudo shred -zuf -n {self.shreds} {rep_path}')
            else:
                status = os.system(f'shred -zu -n {self.shreds} {rep_path}')
            if status:
                self.errors.append(f'Do not shred, os error: {path}')
                return False
        else:
            self.del_file(path)
        if self.check_exist(path):
            self.errors.append(f'Do not shred: {path}')
            return False
        else:
            self.count_del_files += 1
            return True

    def del_file(self, path: str) -> bool:
        """Deletes the file at the specified path using normal deletion"""
        try:
            if os.path.islink(path):
                os.unlink(path)
            else:
                self.zero_file(path)
                os.remove(path)
        except OSError:
            self.errors.append(f'Os error! Do not delete: {path}')
            return False
        if self.check_exist(path):
            self.errors.append(f'Do not delete: {path}')
            return False
        else:
            self.count_del_files += 1
            return True

    def del_dir(self, path: str) -> bool:
        """Deletes an empty folder at the specified path"""
        try:
            if os.path.islink(path):
                os.unlink(path)
            else:
                os.rmdir(path)
        except OSError:
            self.errors.append(f'Os error! Do not delete: {path}')
            return False
        else:
            if self.check_exist(path):
                self.errors.append(f'Do not delete: {path}')
                return False
            else:
                self.count_del_dirs += 1
                return True

    def reset_count(self) -> None:
        """Resetting counters"""
        self.count_zero_files = 0
        self.count_del_files = 0
        self.count_del_dirs = 0

    def reset_error_list(self):
        self.errors.clear()


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
    smart_print()


def work(obj_dict, method=1, log=False, shreds=30):
    my_cleaner = Cleaner()
    my_cleaner.shreds = shreds
    for obj in obj_dict.values():
        smart_print(f'Working with: {obj.path}', '=')
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
    smart_print('The work has been completed', '=')
    print(f'Files were processed: {my_cleaner.count_del_files + my_cleaner.count_zero_files}')
    print(f'Errors: {len(my_cleaner.errors)}')
    smart_print(' Error list: ', '=')
    for err in my_cleaner.errors:
        print(err)
    if log and my_cleaner.errors:
        make_error_log(my_cleaner.errors)
    my_cleaner.reset_error_list()
    my_cleaner.reset_count()


def make_path_obj(path_list):
    if path_list:
        return {n: PathObj(path) for n, path in enumerate(path_list, 1)}
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
        smart_print()
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
        smart_print()
        print('Select the desired action (Ctrl+C to exit):\n'
              '1. Destruction (shred) and delete\n'
              '2. Zeroing not delete\n'
              '3. Zeroing and delete')
        smart_print()
        try:
            user_input = int(input('Input: '))
            if user_input not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            smart_print()
            print('Input error!')
            continue
        else:
            return user_input


def get_shreds():
    while True:
        try:
            shreds = int(input('Enter the number of file overwrites: '))
        except ValueError:
            smart_print()
            print('Input error!')
        else:
            return shreds


def get_args(func):
    parser = createParser()
    namespace = parser.parse_args()

    def deco():
        smart_print(f' Smart Files Destroyer {VERSION} ', '=')
        smart_print(' Aleksandr Suvorov | https://githib.com/mysmarthub/sfd ', '-')
        smart_print('Donate: 4048 4150 0400 5852 | 4276 4417 5763 7686', ' ')
        smart_print(' Utility for mashing, zeroing, deleting files ', '=')
        print('To exit, press Ctrl+C')
        smart_print('', '=')
        func(namespace)
        smart_print('', '=')
        smart_print('The program is complete', '-')
        smart_print('Donate: 4048 4150 0400 5852 | 4276 4417 5763 7686', ' ')

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
            smart_print()
            obj_dict = make_path_obj(path_list)
            print(f'Counting files (Sometimes it can take a long time) ...')
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
        print()
        print('Exit...')
        pass


if __name__ == '__main__':
    main()
