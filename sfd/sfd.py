#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE.txt for details)
# https://github.com/mysmarthub/sfd/
# Copyright © 2020-2021 Aleksandr Suvorov
# -----------------------------------------------------------------------------
"""CLI utility for shredding, erasing, and deleting files."""
import click

from mycleaner import smart, cleaner, settings


def get_action(title):
    while 1:
        click.echo(f'{title} [y/n]?: ')
        char = click.getchar()
        if char == 'y':
            return True
        elif char == 'n':
            return False
        else:
            continue


def get_num():
    num = click.prompt('Enter the number of passes',
                       type=click.IntRange(4, 1000, clamp=True))
    return num


def get_paths():
    """Getting path input from the user and adding them"""
    paths = set()
    while 1:
        user_path = click.prompt('Enter the path', type=click.Path(exists=True))
        smart_print()
        paths.add(user_path)
        if user_path in paths:
            click.echo('Path added successfully!')
        else:
            click.echo('Error! Invalid path or path was added earlier!')
        action = get_action('Add one more path')
        if action:
            continue
        smart_print()
        return paths


def smart_print(text='', char='-'):
    if not char:
        char = ' '
    columns, _ = click.get_terminal_size()
    if text:
        click.echo(f' {text} '.center(columns, char))
    else:
        click.echo(f''.center(columns, char))


def open_url(url):
    click.launch(url)


def logo_start():
    """Output of the welcome logo"""
    smart_print('', '*')
    smart_print(f'{settings.TITLE} v{settings.VERSION}', '=')
    smart_print(f'{settings.DESCRIPTION}', ' ')


def logo_finish():
    """Output of the completion logo"""
    smart_print(f'{settings.URL}', '-')
    smart_print(f'{settings.YANDEX}', '=')
    smart_print(f'{settings.COPYRIGHT}', '*')


def print_version(ctx, value):
    """Print Version"""
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'{settings.TITLE} {settings.VERSION} | {settings.COPYRIGHT}')
    ctx.exit()


def work(method='shred', num=30, paths=None, yes=False, del_dirs=False):
    if paths is None:
        paths = set()
    if method == 'shred' and not num:
        num = get_num()
    if not paths:
        paths = get_paths()
    my_cleaner = cleaner.Cleaner(shreds=num)
    click.echo('File search...')
    path_objects = [smart.PathObj(path) for path in paths]
    for obj in path_objects:
        count = 1
        click.echo(f'[path]:[{obj.path}]:[dirs={obj.num_of_dirs}]:[files:{obj.num_of_files}]')
        if not obj.num_of_files and not obj.num_of_dirs:
            click.echo('Ways to work not found...')
            continue
        if not yes:
            action = get_action(f'Start')
            if not action:
                smart_print()
                continue
        for path in obj.get_files():
            smart_print(f'{obj.path}')
            click.echo(f'[{count}]:[{method}]:[{path}]')
            if not yes:
                action = get_action(f'[{method}]')
                if not action:
                    click.echo('Skipped...')
                    continue
            click.echo('Processing...')
            if method == 'shred':
                status = my_cleaner.shred_file(path, verbose=False)
            elif method == 'erase':
                status = my_cleaner.zero_file(path)
            else:
                status = my_cleaner.del_file(path)
            smart.print_status(status)
            count += 1
        smart_print()
        if not yes and not del_dirs and method != 'erase':
            action = get_action('Delete folders')
            if action:
                del_dirs = True
        if del_dirs:
            smart_print('Del Folders')
            for src in obj.get_dirs():
                click.echo(f'[del folder]:[{src}]')
                if not yes:
                    action = get_action(f'Delete')
                    if not action:
                        click.echo('Skipped...')
                        continue
                    else:
                        click.echo('Processing...')
                status = my_cleaner.del_dir(src)
                smart.print_status(status)
    smart_print('Work completed!')
    click.echo(f'Errors:[{len(my_cleaner.errors)}], '
               f'{method}:[{my_cleaner.count}], '
               f'Del folders:[{my_cleaner.count_del_dirs}]')
    my_cleaner.reset_count()
    my_cleaner.reset_error_list()


def main_menu(yes=False, del_dirs=False):
    while 1:
        smart_print('Main menu')
        click.echo('s: shredding files')
        click.echo('e: erasing files')
        click.echo('d: deleting files')
        click.echo('q: quit')
        char = click.getchar()
        if char == 'q':
            break
        elif char == 's':
            method = 'shred'
        elif char == 'e':
            method = 'erase'
        elif char == 'd':
            method = 'delete'
        else:
            click.echo('Input Error!')
            continue
        work(method=method, yes=yes, del_dirs=del_dirs)


@click.group(invoke_without_command=True)
@click.option('--version', '-v', is_flag=True, callback=print_version,
              help='Displays the version of the program and exits.',
              expose_value=False, is_eager=True)
@click.option('--yes', '-y',
              is_flag=True,
              help='Auto Mode')
@click.option('--del-dirs', '-dd',
              is_flag=True,
              help='Delete the folders?')
@click.pass_context
def cli(ctx, yes, del_dirs):
    """Smart Files Destroyer - CLI utility for shredding, erasing, and deleting files.

    [ARGS]... - Paths to files and/or folders with files
    cli.py -y -dd shred /path/ /path2/ /pathN/file.file

    sfd.py -y -dd shred /path/ -n 100
    sfd.py -y -dd erase /path/
    sfd.py -y -dd delete /path/

    """

    ctx.ensure_object(dict)
    ctx.obj['yes'] = yes
    ctx.obj['dd'] = del_dirs
    logo_start()
    if ctx.invoked_subcommand == 'shred':
        smart_print('Shredding files')
    elif ctx.invoked_subcommand == 'erase':
        smart_print('Erasing files')
    elif ctx.invoked_subcommand == 'delete':
        smart_print('Deleting files')
    else:
        main_menu(yes=yes, del_dirs=del_dirs)
        logo_finish()


@cli.resultcallback()
def process_result(result, **kwargs):
    logo_finish()


@cli.command()
@click.argument('paths', nargs=-1, type=click.Path(exists=True))
@click.option('--num', '-n',
              prompt='Number of passes',
              help='Number of passes',
              type=click.IntRange(4, 1000, clamp=True))
@click.pass_context
def shred(ctx, paths, num):
    """Shredding files"""
    method = 'shred'
    work(method=method, num=num, paths=paths, yes=ctx.obj['yes'], del_dirs=ctx.obj['dd'])


@cli.command()
@click.argument('paths', nargs=-1, type=click.Path(exists=True))
@click.pass_context
def erase(ctx, paths):
    """Erasing files"""
    method = 'erase'
    work(method=method, paths=paths, yes=ctx.obj['yes'], del_dirs=ctx.obj['dd'])


@cli.command()
@click.argument('paths', nargs=-1, type=click.Path(exists=True))
@click.pass_context
def delete(ctx, paths):
    """Deleting files"""
    method = 'delete'
    work(method=method, paths=paths, yes=ctx.obj['yes'], del_dirs=ctx.obj['dd'])


if __name__ == '__main__':
    cli()
