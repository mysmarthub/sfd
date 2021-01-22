Smart Files Destroyer
==========
CLI utility for destroying,
zeroing, and deleting files.
Author and developer: Aleksandr Suvorov
BSD 3-Clause License

Help the project financially:
=============================
https://yoomoney.ru/to/4100115206129186
Visa:    4048 4150 0400 5852
https://paypal.me/myhackband

What's new?
===========
The program code has been completely redesigned.
The interface has been completely changed,
bugs have been fixed, new features have been added,
and work has been accelerated.

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


Windows support:
----------------
Download sfd and run sfd.exe

https://sourceforge.net/projects/smart-files-destroyer/

Since sfd.exe packed with pyinstaller,
some antivirus software may react to it.

Run sfd on Windows:

1. Download and install the latest version of Python
https://www.python.org/downloads/
when installing, check the box " Add Python to PATH"

2. Restart the system

3. Start the console (win + r keyboard shortcut)

4. Run the command:
pip install sfd

If the installation is successful and all the steps were performed correctly
you can run sfd in the console with the command:
sfd --help


You can also download the archive with the program,
unpack it to any convenient place, and if you have python installed:

1. Install dependencies with the command:
2. Find the file in the program folder requirements.txt
3. pip install -r full path to the file requirements.txt
Next, you can run the utility from the command line
by specifying the full path to the sfd.py using the command:
python sfd.py [arguments]

---

Description:
============
Console utilities for destroying,
zeroing, and deleting files.

---
With this package, you can develop graphical,
console , and cross-platform applications to destroy,
reset data in a file, and delete files
so that they are difficult or impossible to recover.

---
You can also use a ready-made console utility for destruction,
reset and delete files.

---
The utility allows you to destruct files,
reset them to zero and delete them,
for complete or partial difficulty in
restoring them after deletion.

---
Be careful! When adding folders, all files from all subfolders
will be added recursively.

---
- We recommend that you run the program on Linux, mount the disks,
and work with them, because then you will have access to
the destroy method with the function of overwriting files.
When running in Windows, the destroy method will reset the
files and then delete them without using multiple file overwrites!

Help:
=====

Usage: sfd.py [OPTIONS] [PATHS]...

  Smart Files Destroyer - CLI utility for destroying, zeroing, and deleting files.

  PATHS - these are the paths to files and folders with files separated by a
  space, if there are spaces in the path name, escape them, or put them in
  quotation marks.

  - Console utility for destruction, zeroing, and deleting files.

  - The utility allows you to destruct files, reset them to zero and delete
  them, for complete or partial difficulty in restoring them after deletion.

  - Be careful! When adding folders, all files from all subfolders will be
  added recursively.

  -Use:
    sfd /path1 /path2 /pathN/file.file --shred -n 30 -dd -y

  https://github.com/mysmarthub/sfd mysmarthub@ya.ru

Options:
  -v, --version      Displays the version of the program and exits.
  -y, --yes          Auto Mode, be very careful with this parameter, if you
                     specify it, the program will start and start destroying
                     files automatically.

  -n, --num INTEGER  Number of overwrites. If you use the shred method, each
                     file will be overwritten the specified number of times
                     before being destroyed.

  -s, --shred        Overwrites random data, renames and deletes the file,
                     used by default.

  -z, --zero         Resets and does not delete the file.
  -d, --del          Resets and deletes the file.
  -t, --test         The test method, files and folders will remain unchanged.
  -dd, --del-dirs    Delete the folders?
  --help             Show this message and exit.

Use:
====

Package installation:
---------------------
    `pip install sfd`

Launch and use the ready-made utility:
--------------------------------------
    - After installation, you can run the utility using its name.
        sfd

    - See the help page to understand how to work with the utility

    - After the name, specify the paths to files and folders separated by a space,
        on some systems if the path contains spaces or others
        forbidden characters, and the system itself does not escape such a path,
        either escape such a path or enclose it in quotation marks.
        sfd /path1 /path2 /pathN/file.file

    - Next, you should specify the method for the utility to work. At the moment
        there are 4 methods available: --shred, --zero, --del, --test.
    --shred: [destroy] - overwrites and deletes the file.
    --zero: [zeroing] - completely destroys the information inside the file,
        but does not delete the file.
    --del: [delete] - First applies [zeroing], then deletes the file.
    --test: [test] - Running the program in test mode, no
        files or folders will not be deleted
    sfd /path1 /path2 /pathN/file.file --shred

    - When using the method --shred ([destroy])
        you can specify the number of file overwrites
        using the parameter --num 100 или -n 100,
        with any number separated by a space.
    sfd /path1 /path2 /pathN/file.file --shred -n 30

    - To delete empty folders after work, use the parameter --del-dirs или -dd

    - You can also run the utility in automatic execution mode
        (for example, use it to start and run at a certain time
        using the task scheduler). To do this, you should send an additional message
        the --yes or-y parameter. Be careful using this parameter,
        after all, the utility will start working automatically.

        To start automatically, you must pass all the necessary parameters:
            be sure the existing path, and the method (if you do not pass default
            [destroy] is triggered, and the --yes or-y parameter is used.
            The parameters -dd and --num can be used as desired.
        sfd /path1 /path2 /pathN/file.file --shred -n 30 -dd -y

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

Disclaimer of liability:
========================
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

Support:
========
    Email: mysmarthub@ya.ru
    Copyright © 2020-2021 Aleksandr Suvorov
