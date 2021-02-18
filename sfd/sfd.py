#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details)
# https://github.com/mysmarthub/sfd/
# Copyright © 2020-2021 Aleksandr Suvorov
# -----------------------------------------------------------------------------
"""CLI utility for destroying, zeroing, and deleting files"""
import os

import click

from mycleaner import smart, cleaner

TITLE = 'Smart Files Destroyer'
VERSION = '1.0.5'
DESCRIPTION = 'CLI utility for destroying, zeroing, and deleting files'
AUTHOR = 'Aleksandr Suvorov'
URL = 'https://github.com/mysmarthub/sfd/'
COPYRIGHT = 'Copyright © 2020-2021 Aleksandr Suvorov'
YANDEX = 'https://yoomoney.ru/to/4100115206129186'
PAYPAL = 'https://paypal.me/myhackband'
README_URL = 'https://github.com/mysmarthub/sfd/blob/master/README.md'


def open_url(url):
    click.launch(url)


class SmartCleaner:
    """Managing the operation of the utility"""

    def __init__(self, paths: set, method: str = 'destroy', num=30, del_dirs=False):
        """
        When creating an object, it takes as parameters:

        :param paths: <set> a variety of paths to files and folders
        :param method: <str> method to work with - currently available [destroy, zeroing, delete, test]
        :param method: <int> number of overwrites of a file before deleting it
        :param method: <bool> Delete folders True - empty folders will be deleted - False - will not be deleted
        """
        self.__paths = paths
        self.method = method
        self.num = num
        self.del_dirs = del_dirs
        self.__count = 0

    def prompt_path(self):
        """Getting path input from the user and adding them"""
        while 1:
            user_path = click.prompt('Enter the path (0 - back)')
            smart.smart_print()
            if user_path == '0':
                break
            if self.add_path(user_path):
                click.echo('Path added successfully!')
            else:
                click.echo('Error! Invalid path or path was added earlier!')

    def prompt_remove_path(self):
        """User's choice of paths to exclude"""
        while 1:
            path_num_list = {n: path for n, path in enumerate(self.__paths, 1)}
            if not path_num_list:
                click.echo('There is no way to remove...')
                break
            click.echo('Added paths: ')
            smart.smart_print()
            for n, path in path_num_list.items():
                click.echo(f'{n}. Path{path}')
            user_input = click.prompt('Enter the path number to delete (0 - back)', type=int)
            smart.smart_print()
            if user_input == 0:
                break
            if user_input not in path_num_list:
                click.echo('Input Error!')
            else:
                if self.remove_path(path_num_list[user_input]):
                    click.echo('The path was successfully deleted!')
                else:
                    click.echo('Error while deleting route!')

    def add_path(self, path: str) -> bool:
        """Adding a path"""
        if path not in self.__paths and os.path.exists(path):
            self.__paths.add(path)
            return True
        return False

    def remove_path(self, path: str) -> bool:
        """Deleting a path"""
        if os.path.exists(path) and path in self.__paths:
            self.__paths.remove(path)
            return True
        return False

    def show_info(self):
        """Displaying paths, the number of folders and files they contain"""
        if self.__paths:
            for n, path in enumerate(self.__paths, 1):
                msg = f'{n} Path[{path}]' \
                      f' Files[{smart.get_count_files(path)}] ' \
                      f'Folders[{smart.get_count_dirs(path)}]'
                click.echo(msg)
        else:
            click.echo('There is no way to display...')

    def show(self):
        """Displays all folders and files that are contained in the added paths"""
        if self.__paths:
            for path in self.__paths:
                click.echo()
                click.echo(f'Path[{path}]')
                smart.smart_print()
                if os.path.isdir(path):
                    click.echo('Folders:')
                    for n, folder in enumerate(smart.get_folders_gen(path), 1):
                        click.echo(f'{n} Path[{folder}]')
                    click.echo()
                    click.echo('Files:')
                    for n, file in enumerate(smart.get_files_gen(path), 1):
                        click.echo(f'{n} Path[{file}]')
        else:
            click.echo('There is no way to display...')

    def update_method(self):
        """Getting user input to change the way the utility works"""
        while 1:
            method_dict = {n: m for n, m in enumerate(['destroy', 'zeroing', 'delete', 'test'], 1)}
            click.echo('0. Cancel')
            for n, m in method_dict.items():
                msg = f'{n}: {m}'
                if self.method == m:
                    msg += ' [x]'
                click.echo(msg)
            user_method = click.prompt(f'Select a method', type=int)
            if not user_method:
                break
            smart.smart_print()
            if user_method not in method_dict:
                click.echo('Input Error!')
                continue
            else:
                self.method = method_dict[user_method]
                click.echo(f'The method is successfully changed to {self.method}!')
            break

    @property
    def paths(self):
        """All the way"""
        return self.__paths

    @property
    def count_paths(self):
        """Number of paths"""
        return len(self.__paths)

    def clear(self):
        """Clearing data"""
        self.__paths.clear()
        self.__count = 0

    def __work(self, obj, file):
        """Destroying, zeroing, and deleting files"""
        if self.method == 'destroy':
            status = obj.shred_file(file)
        elif self.method == 'zeroing':
            status = obj.zero_file(file)
        elif self.method == 'delete':
            status = obj.del_file(file)
        else:
            status = True
        return status

    def __str__(self):
        return f'Paths[{self.count_paths}] Method[{self.method}]'

    def start(self):
        """Working with paths destroying, zeroing, and deleting files"""
        if self.__paths:
            smart.smart_print()
            click.echo(f'The selected method: {self.method}')
            count_files = 0
            count_dirs = 0
            obj_data = smart.DataObj()
            smart_cleaner = cleaner.Cleaner(shreds=self.num)
            for path in self.__paths:
                obj_data.add_path(path)
            for file in obj_data.get_files():
                count_files += 1
                smart.smart_print()
                click.echo(f'[{count_files}][{self.method}] File: {file}')
                status = self.__work(smart_cleaner, file)
                smart.print_status(status)
            smart.smart_print()
            if self.del_dirs:
                for path in obj_data.get_dirs():
                    click.echo(f'Delete folder: {path}')
                    if self.method != 'test':
                        status = smart_cleaner.del_dir(path)
                    else:
                        status = True
                    smart.print_status(status)
                    count_dirs += 1
                smart.smart_print()
            click.echo(f'The work has been completed:\n'
                       f'Processed files: [{count_files - len(smart_cleaner.errors)}]\n'
                       f'Deleted folders: [{count_dirs}]\n'
                       f'Errors: [{len(smart_cleaner.errors)}]')
            if smart_cleaner.errors:
                smart.smart_print(f' Errors: [{len(smart_cleaner.errors)}]')
                for err in smart_cleaner.errors:
                    click.echo(err)
            self.clear()
        else:
            click.echo('There is no way to work...')


def logo_start():
    """Output of the welcome logo"""
    smart.smart_print('', '*')
    smart.smart_print(f'{TITLE} v{VERSION}', '=')
    smart.smart_print(f'{DESCRIPTION}', ' ')


def logo_finish():
    """Output of the completion logo"""
    click.echo()
    click.echo('Exit...')
    smart.smart_print(f'{URL}', '-')
    smart.smart_print(f'{YANDEX}', '-')
    smart.smart_print(f'{COPYRIGHT}', '=')
    smart.smart_print('The program is complete', '*')


def print_version(ctx, value):
    """Print Version"""
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'{TITLE} {VERSION} | {COPYRIGHT}')
    ctx.exit()


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
@click.option('--shred', '-s', 'method',
              flag_value='destroy',
              default=True,
              help='Overwrites random data, renames and deletes the file, used by default.')
@click.option('--zero', '-z', 'method', flag_value='zeroing', help='Resets and does not delete the file.')
@click.option('--del', '-d', 'method', flag_value='delete', help='Resets and deletes the file.')
@click.option('--test', '-t', 'method', flag_value='test',
              help='The test method, files and folders will remain unchanged.')
@click.option('--del-dirs', '-dd',
              is_flag=True,
              help='Delete the folders?')
def cli(paths, yes, num, method, del_dirs):
    """
    Smart Files Destroyer - CLI utility for destroying, zeroing, and deleting files.

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

    -Use:
    sfd /path1 /path2 /pathN/file.file --shred -n 30 -dd -y

    https://github.com/mysmarthub/sfd/
    mysmarthub@ya.ru
    """
    work = True
    logo_start()
    my_cleaner = SmartCleaner(paths=set(paths), method=method, num=num, del_dirs=del_dirs)
    if not yes or not my_cleaner.paths:
        while 1:
            smart.smart_print()
            click.echo(f'Main Menu. {my_cleaner}:')
            smart.smart_print()
            click.echo(f'1. Start')
            click.echo(f'2. Add Path')
            click.echo(f'3. Remove Path')
            click.echo(f'4. Information about paths')
            click.echo(f'5. Show files and folders')
            click.echo(f'6. To change the method [{my_cleaner.method}]')
            click.echo(f'7. Open help url')
            click.echo(f'0. Exit')
            smart.smart_print()
            action = click.prompt('Enter', type=int)
            smart.smart_print()
            if action == 1:
                if not my_cleaner.paths:
                    click.echo("Error! You didn't add a path!")
                    continue
                work = True
                break
            elif action == 2:
                my_cleaner.prompt_path()
            elif action == 3:
                my_cleaner.prompt_remove_path()
            elif action == 4:
                my_cleaner.show_info()
            elif action == 5:
                my_cleaner.show()
            elif action == 6:
                my_cleaner.update_method()
            elif action == 7:
                open_url(README_URL)
            elif action == 0:
                work = False
                break
            else:
                click.echo('Invalid input!')
            if action not in (2,):
                input('Enter for continue...')
    if work:
        my_cleaner.start()
    logo_finish()
    if os.name != 'posix':
        input('Enter for exit...')


if __name__ == '__main__':
    cli()
