#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details)
# https://github.com/mysmarthub
# Copyright © 2020-2021 Aleksandr Suvorov
# -----------------------------------------------------------------------------
"""CLI utility for destroying, zeroing, and deleting files"""
import os
import shutil

import click

from mycleaner import smart, cleaner

__version__ = '1.0.1'
__author__ = 'Aleksandr Suvorov'
__url__ = 'https://githib.com/mysmarthub/sfd'
__donate__ = 'Donate: https://yoomoney.ru/to/4100115206129186'
__copyright__ = 'Copyright © 2020-2021 Aleksandr Suvorov'


def smart_print(text='', char='-'):
    columns, _ = shutil.get_terminal_size()
    print(f'{text}'.center(columns, char))


def get_files_gen(path):
    if path and os.path.exists(path):
        for p, _, files in os.walk(path):
            for f in files:
                yield os.path.join(p, f)


def get_folders_gen(path):
    if path and os.path.exists(path):
        for p, folders, _ in os.walk(path):
            for f in folders:
                yield os.path.join(p, f)


def get_count_files(path: str) -> int:
    """
    Counting the number of files recursively nested in a directory

    :param path: <str> Path to the directory
    :return: <int> Counting the number of files recursively nested in a directory
    """
    if os.path.isfile(path):
        return 1
    elif os.path.isdir(path):
        return sum([len(files) for _, _, files in os.walk(path)])
    else:
        return 0


def get_count_dirs(path: str) -> int:
    """
    Counting the number of folder recursively nested in a directory

    :param path: <str> Path to the directory
    :return: <int> Counting the number of folders recursively nested in a directory
    """
    if os.path.isdir(path):
        return sum([len(folders) for _, folders, _ in os.walk(path)])
    else:
        return 0


def logo_start():
    smart_print('', '*')
    smart_print(f' Smart Files Destroyer ', '=')
    smart_print('', '*')
    smart_print(' CLI utility for destroying, zeroing, and deleting files ', ' ')
    smart_print()


def logo_finish():
    smart_print('', '=')
    smart_print(f' {__author__} | {__url__} ', ' ')
    smart_print(f'{__donate__}', ' ')
    smart_print('The program is complete', '-')


def paths_print(paths):
    print('Added paths...')
    print('Counting files and folders...')
    count = 0
    for path in paths:
        count += 1
        smart_print()
        print(f'[{count}]: {path} | Folders[{get_count_dirs(path)}] | Files[{get_count_files(path)}]')
    smart_print()


def get_action(paths):
    while 1:
        count = 0
        print()
        print('To continue, select an action: ')
        smart_print()
        print('1. Get started')
        print('2. Show files')
        print('3. Show folders')
        print('4. Count files and folders')
        print('0. Exit')
        smart_print()
        user_input = click.prompt('Enter: ', type=int)
        if user_input == 1:
            return True
        elif user_input == 2:
            for path in paths:
                smart_print()
                print(f'    {path}:')
                for file in get_files_gen(path):
                    count += 1
                    print(f'{count} [{file}]')
        elif user_input == 3:
            for path in paths:
                smart_print()
                print(f'    {path}:')
                for folder in get_folders_gen(path):
                    count += 1
                    print(f'{count} [{folder}]')
        elif user_input == 4:
            paths_print(paths)
        else:
            return False


def get_paths():
    paths = set()
    while 1:
        smart_print()
        print('Path entry mode. (0 - cancel)')
        path = click.prompt('Enter the path: ')
        if os.path.exists(path):
            paths.add(path)
            print('The path is added!')
        else:
            if path == '0':
                return paths
            else:
                print('There is no path!')
                continue


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'Smart Files Destroyer {__version__} | {__copyright__}')
    ctx.exit()


def print_status(status):
    if status:
        print('[Successfully!]')
    else:
        print('[Error!]')


def start(paths, num=30, method='destroy', del_dirs=False, test=False):
    count_files = 0
    count_dirs = 0
    obj_data = smart.DataObj()
    my_cleaner = cleaner.Cleaner(shreds=num)
    for path in paths:
        obj_data.add_path(path)
    for file in obj_data.get_files():
        count_files += 1
        smart_print()
        print(f'[{count_files}][{method}] File: {file}')
        if not test:
            if method == 'destroy':
                status = my_cleaner.shred_file(file)
            elif method == 'zeroing':
                status = my_cleaner.zero_file(file)
            else:
                status = my_cleaner.del_file(file)
        else:
            status = True
        print_status(status)
    smart_print()
    if del_dirs:
        for path in obj_data.get_dirs():
            print(f'Delete folder: {path}')
            if not test:
                status = my_cleaner.del_dir(path)
            else:
                status = True
            print_status(status)
        smart_print()
    print(f'The work has been completed:\n'
          f'Processed files: [{count_files - len(my_cleaner.errors)}]\n'
          f'Deleted folders: [{count_dirs}]\n'
          f'Errors: [{len(my_cleaner.errors)}]')
    if my_cleaner.errors:
        smart_print(f' Errors: [{len(my_cleaner.errors)}]')
        for err in my_cleaner.errors:
            print(err)


@click.command()
@click.argument('paths', nargs=-1, type=click.Path(exists=True))
@click.option('--version', '-v', is_flag=True, callback=print_version,
              help='Displays the version of the program and exits.',
              expose_value=False, is_eager=True)
@click.option('--yes', '-y',
              is_flag=True,
              help='Auto Mode, be very careful with this parameter, if you specify it, '
                   'the program will start and start destroying files automatically.')
@click.option('--num', '-n',
              default=30,
              help='Number of overwrites. If you use the shred method, '
                   'each file will be overwritten the specified number of '
                   'times before being destroyed.')
@click.option('--shred', 'method',
              flag_value='destroy',
              default=True,
              help='Overwrites random data, renames and deletes the file, used by default.')
@click.option('--zero', 'method', flag_value='zeroing', help='Resets and does not delete the file.')
@click.option('--del', 'method', flag_value='delete', help='Resets and deletes the file.')
@click.option('--del-dirs', '-dd',
              is_flag=True,
              help='Delete the folders?')
@click.option('--test', '-t',
              is_flag=True,
              help='Working in test mode, files and folders will not be destroyed.')
def cli(paths, yes, num, method, del_dirs, test):
    """Smart Files Destroyer - CLI utility for destroying, zeroing, and deleting files.

    PATHS - these are the paths to files and folders with files separated by a space,
    if there are spaces in the path name, escape them, or put them in quotation marks.

    - Console utility for destruction,
    zeroing, and deleting files.

    - The utility allows you to destruct files,
    reset them to zero and delete them,
    for complete or partial difficulty in
    restoring them after deletion.

    - Be careful! When adding folders, all files from all subfolders
    will be added recursively.
    """
    logo_start()
    if test:
        msg = f'The selected method: [Test mode]'
    else:
        msg = f'The selected method: [{method}]'
    click.echo(msg)
    paths = set(paths) if paths else get_paths()
    click.echo(f'Added paths: [{len(paths)}]')
    smart_print()
    for path in paths:
        click.echo(path)
    smart_print()
    action_status = True if yes else get_action(paths)
    if action_status:
        start(paths=paths, num=num, method=method, test=test, del_dirs=del_dirs)
    else:
        print('Exit...')
    logo_finish()


if __name__ == '__main__':
    cli()
