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

import click
from mycleaner import smart, cleaner


__version__ = '1.0.0'
__author__ = 'Aleksandr Suvorov'
__url__ = 'https://githib.com/mysmarthub/sfd'
__donate__ = 'Donate: 4048 4150 0400 5852 | 4276 4417 5763 7686'
__copyright__ = 'Copyright © 2020-2021 Aleksandr Suvorov'


def print_status(status):
    if status:
        print('[Successfully!]')
    else:
        print('[Error!]')


def logo_start():
    smart.smart_print('', '*')
    smart.smart_print(f' Smart Files Destroyer ', '=')
    smart.smart_print('', '*')
    smart.smart_print(' CLI utility for destroying, zeroing, and deleting files ', ' ')


def logo_finish():
    smart.smart_print('', '=')
    smart.smart_print('The program is complete', '-')
    smart.smart_print(f' {__author__} | {__url__} ', ' ')
    smart.smart_print(f'{__donate__}', ' ')


def print_paths(paths):
    print('Added paths...')
    print('Counting files and folders...')
    count = 0
    for path in paths:
        count += 1
        smart.smart_print()
        print(f'[{count}]: {path} | Folders[{smart.get_count_dirs(path)}] | Files[{smart.get_count_files(path)}]')
    smart.smart_print()


def start(paths, num=30, method='destroy', dirs=False):
    obj_data = smart.DataObj()
    my_cleaner = cleaner.Cleaner(shreds=num)
    for path in paths:
        obj_data.add_path(path)
    for file in obj_data.get_files():
        smart.smart_print()
        print(f'[{method}] File: {file}')
        if method == 'destroy':
            status = my_cleaner.shred_file(file)
        elif method == 'zeroing':
            status = my_cleaner.zero_file(file)
        else:
            status = my_cleaner.del_file(file)
        print_status(status)
    smart.smart_print()
    if dirs:
        for path in obj_data.get_dirs():
            print(f'Delete folder: {path}')
            status = my_cleaner.del_dir(path)
            print_status(status)
    if my_cleaner.errors:
        smart.smart_print(f' Errors: [{len(my_cleaner.errors)}]')
        for err in my_cleaner.errors:
            print(err)


def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'Smart Files Destroyer {__version__} | {__copyright__}')
    ctx.exit()


@click.command()
@click.option('--paths', '--p',
              multiple=True,
              help='Paths to a files or folder with files, all attached '
                   'files and folders will be taken into account! '
                   'Be extremely careful and attentive when adding.')
@click.option('--num', '--n',
              default=30,
              help='Number of overwrites. If you use the shred method, '
                   'each file will be overwritten the specified number of '
                   'times before being destroyed.')
@click.option('--dirs', '--d',
              is_flag=True,
              help='Delete the folders?')
@click.option('--yes', '--y',
              is_flag=True,
              help='Auto Mode, be very careful with this parameter, if you specify it, '
                   'the program will start and start destroying files automatically.')
@click.option('--shred', 'method',
              flag_value='destroy',
              default=True,
              help='Overwrites random data, renames and deletes the file, used by default.')
@click.option('--zero', 'method', flag_value='zeroing', help='Resets and does not delete the file.')
@click.option('--del', 'method', flag_value='delete', help='Resets and deletes the file.')
@click.option('--version', '--v', is_flag=True, callback=print_version,
              help='Displays the version of the program and exits.',
              expose_value=False, is_eager=True)
def main(paths, num, dirs, method, yes):
    """Smart Files Destroyer - CLI utility for destroying, zeroing, and deleting files.

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
    paths = [path for path in set(paths) if os.path.exists(path)]
    if paths:
        smart.smart_print()
        print_paths(paths)
        if yes or click.confirm('Do you want to continue?', default=True):
            start(paths=paths, num=num, method=method, dirs=dirs)
        else:
            print('Exit...')
    else:
        smart.smart_print()
        print('No paths found...')
    logo_finish()


if __name__ == '__main__':
    main()
