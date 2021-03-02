=====================
Smart Files Destroyer
=====================
CLI utility for destroying,
zeroing, and deleting files.
Author and developer: Aleksandr Suvorov
BSD 3-Clause License

Help the project financially:
=============================
https://yoomoney.ru/to/4100115206129186
Visa:    4048 4150 0400 5852
https://paypal.me/myhackband


Warninig!
========
You can see information about earlier versions on the release page:
https://github.com/mysmarthub/sfd/releases.

---
What's news?
-----
A new interface!

Termux support:
===============

You can easily use the utility with Termux
on mobile phones and tablets.

    1. Install Termux
    2. pkg install python
    3. pip install sfd
    4. sfd --help
    5. To access the file storage:
        termux-setup-storage
        cd ~/storage

    Files are destroyed even without root access and sudo.
    Read more about how to use the utility.

------------
Description:
============
CLI utility for shredding, erasing, and deleting files.

---
The utility allows you to shred files,
erase files, for complete or partial difficulty
their recovery after removal.

Be careful! When adding folders, all files from all subfolders
will be added recursively.

We recommend that you run the program on Linux, mount the disks,
and work with them, because then you will have access to
the destroy method with the function of overwriting files.

Help:
-----

    Usage: sfd.py [OPTIONS] COMMAND [ARGS]...

      Smart Files Destroyer - CLI utility for shredding, erasing, and deleting files.

      [ARGS]... - Paths to files and/or folders with files cli.py -y -dd
      shred /path/ /path2/ /pathN/file.file

      sfd.py -y -dd shred /path/ /path2/ /pathN/file.file -n 100
      sfd.py -y -dd erase /path/ /path2/ /pathN/file.file
      sfd.py -y -dd delete /path/ /path2/ /pathN/file.file

    Options:
      -v, --version    Displays the version of the program and exits.
      -y, --yes        Auto Mode
      -dd, --del-dirs  Delete the folders?
      --help           Show this message and exit.

    Commands:
      delete  Deleting files
      erase   Erasing files
      shred   Shredding files


Use:
----

Package installation:
---------------------
    `pip install sfd`

To create applications:
-----------------------
    from sfd import smart, cleaner

Launch and use the ready-made utility:
--------------------------------------
    - After installation, you can run the utility using its name.
        sfd --help

    - See the help page to understand how to work with the utility

      sfd.py -y -dd shred /path/ /path2/ /pathN/file.file -n 100
      sfd.py -y -dd erase /path/ /path2/ /pathN/file.file
      sfd.py -y -dd delete /path/ /path2/ /pathN/file.file

    - To delete empty folders after work, use the parameter --del-dirs или -dd

    - You can also run the utility in automatic execution mode
        (for example, use it to start and run at a certain time
        using the task scheduler). To do this, you should send an additional message
        the --yes or -y parameter. Be careful using this parameter,
        after all, the utility will start working automatically.


To delete some files, you may need administrator rights.
To do this, install the package with the command:

sudo pip install sfd

sudo sfd -y -dd shred /path/ /path2/ /pathN/file.file -n 100
sudo sfd -y -dd erase /path/ /path2/ /pathN/file.file
sudo sfd -y -dd delete /path/ /path2/ /pathN/file.file


Git Clone:
----------

git clone https://github.com/mysmarthub/sfd.git
cd sfd
pip install -r requirements.txt
python sfd/sfd.py /path1 /path2 /pathN/file.file --shred -n 30 -dd


To delete some files, you may need administrator rights.
To do this, install the package with the command:

sudo pip install sfd
sudo sfd /path1 /path2 /pathN/file.file --shred -n 30 -dd

or:

git clone https://github.com/mysmarthub/sfd.git
cd sfd
sudo pip install -r requirements.txt
sudo python sfd/sfd.py /path1 /path2 /pathN/file.file --shred -n 30 -dd

Links:
======
https://github.com/mysmarthub/sfd
https://pypi.org/project/sfd
https://sourceforge.net/projects/sfd-package/files/latest/download

------------------------
Disclaimer of liability:
------------------------
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

-------------
Requirements:
-------------

[Click](https://github.com/pallets/click) by [license](https://github.com/pallets/click/blob/master/LICENSE.rst)

[My Cleaner](https://github.com/mysmarthub/mycleaner/)

[Python 3+](https://python.org)

--------
Support:
--------
    Email: mysmarthub@ya.ru
    Copyright © 2020 Aleksandr Suvorov

    -----------------------------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE.txt for details)
    https://github.com/mysmarthub
    Copyright © 2020-2021 Aleksandr Suvorov
    -----------------------------------------------------------------------------
