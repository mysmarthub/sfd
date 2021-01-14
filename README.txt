Smart Files Destroyer
=============================================================================

CLI utility for destroying, zeroing, and deleting files.

Author and developer: Aleksandr Suvorov

-----------------------------------------------------------------------------
Licensed under the terms of the BSD 3-Clause License
(see LICENSE for details)
https://github.com/mysmarthub
Copyright © 2020-2021 Aleksandr Suvorov
-----------------------------------------------------------------------------


Help the project financially:
-----------------------------------------------------------------------------
https://yoomoney.ru/to/4100115206129186

Visa:    4048 4150 0400 5852

https://paypal.me/myhackband

-----------------------------------------------------------------------------
Termux support:
---------------

You can easily use the utility with Termux
on mobile phones and tablets.

    1. Download and install Termux https://play.google.com/store/apps/details?id=com.termux&hl=ru&gl=US
    2. pkg install python
    3. pip install sfd
    4. sfd --help
    5. To access the file storage:
        termux-setup-storage
        cd ~/storage

    Files are destroyed even without root access and sudo.
    Read more about how to use the utility.
------------------------------------------------------------------------------

Description:
------------
Console utility for destruction,
zeroing, and deleting files.

The utility allows you to destruct files,
reset them to zero and delete them,
for complete or partial difficulty in
restoring them after deletion.

Be careful! When adding folders, all files from all subfolders
will be added recursively.

When you run the program with all the parameters,
all files located at the specified path will be destroyed,
including those nested in other folders,
if you specify all the arguments, then after
starting the utility will start working without
confirmation, so be very careful!

-------------------------------------------------------------------

Help:
-----

    Pass the path/file path/folder
    parameters at startup, enter
    the number of rewrites of the file by using the-n
    (30 by default), enter -dd If you want
    to utility delete empty folder after the destruction
    files, use -y to automatically launch the program
    use --shred for destruction (this is the default),
    --zero for zeroing, --del for zeroing and deleting.


============================================================================
Usage: sfd [OPTIONS] [PATHS]...

  Smart Files Destroyer - CLI utility for destroying, zeroing, and deleting
  files.

  PATHS - these are the paths to files and folders with files separated by a
  space, if there are spaces in the path name, escape them, or put them in
  quotation marks.

  - Console utility for destruction, zeroing, and deleting files.

  - The utility allows you to destruct files, reset them to zero and delete
  them, for complete or partial difficulty in restoring them after deletion.

  - Be careful! When adding folders, all files from all subfolders will be
  added recursively.

Options:
  -v, --version      Displays the version of the program and exits.
  -y, --yes          Auto Mode, be very careful with this parameter, if you
                     specify it, the program will start and start destroying
                     files automatically.

  -n, --num INTEGER  Number of overwrites. If you use the shred method, each
                     file will be overwritten the specified number of times
                     before being destroyed.

  --shred            Overwrites random data, renames and deletes the file,
                     used by default.

  --zero             Resets and does not delete the file.
  --del              Resets and deletes the file.
  -dd, --del-dirs    Delete the folders?
  -t, --test         Working in test mode, files and folders will not be
                     destroyed.

  --help             Show this message and exit.


================================================================================


Use:
====

Package installation:
---------------------

pip install sfd

Use:
----

sfd /path/ /path2/ /path/file.file --shred -n 100 -dd -y

Git Clone:
----------

git clone https://github.com/mysmarthub/sfd.git

cd sfd

pip install -r requirements.txt

python sfd/sfd.py /path/ /path2/ /path/file.file --shred -n 100 -dd -y


To delete some files, you may need administrator rights.
To do this, install the package with the command:

sudo pip install sfd

sudo sfd /path/ /path2/ /path/file.file --shred -n 100 -dd -y

or:

git clone https://github.com/mysmarthub/sfd.git

cd sfd

sudo pip install -r requirements.txt

sudo python sfd/sfd.py /path/ /path2/ /path/file.file --shred -n 100 -dd -y


Links:
------
https://github.com/mysmarthub/sfd

https://pypi.org/project/sfd/

https://sourceforge.net/projects/smart-files-destroyer/files/latest/download


Disclaimer of liability:
------------------------
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

Support:
---
    Email: mysmarthub@ya.ru
    Copyright © 2020 Aleksandr Suvorov
