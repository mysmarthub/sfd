Smart Files Destroyer
===
    
>CLI utility for destroying, zeroing, and deleting files.

>Author and developer: Aleksandr Suvorov

```
-----------------------------------------------------------------------------
Licensed under the terms of the BSD 3-Clause License
(see LICENSE for details)
https://github.com/mysmarthub
Copyright © 2020-2021 Aleksandr Suvorov
-----------------------------------------------------------------------------

```

----

[![PyPI](https://img.shields.io/pypi/v/sfd)](https://pypi.org/project/sfd)
[![PyPI - Format](https://img.shields.io/pypi/format/sfd)](https://pypi.org/project/sfd)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/sfd?label=pypi%20downloads)](https://pypi.org/project/sfd)
[![GitHub repo size](https://img.shields.io/github/repo-size/mysmarthub/sfd)](https://github.com/mysmarthub/sfd/)
[![GitHub all releases](https://img.shields.io/github/downloads/mysmarthub/sfd/total?label=github%20downloads)](https://github.com/mysmarthub/sfd/)
[![GitHub Repo stars](https://img.shields.io/github/stars/mysmarthub/sfd?style=social)](https://github.com/mysmarthub/sfd/)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/mysmarthub/sfd)](https://github.com/mysmarthub/sfd/)
![GitHub](https://img.shields.io/github/license/mysmarthub/sfd?style=flat-square)
---
[![Download Smart Files Destroyer](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/smart-files-destroyer/files/latest/download)

[![Download Smart Files Destroyer](https://img.shields.io/sourceforge/dt/smart-files-destroyer.svg)](https://sourceforge.net/projects/smart-files-destroyer/files/latest/download)

---

![Smart Files Destroyer](https://github.com/mysmarthub/sfd/raw/master/images/sfd_logo.png)

---

Help the project financially:
---
>[Yandex Money](https://yoomoney.ru/to/4100115206129186)

    Visa:    4048 4150 0400 5852

>[Paypal](https://paypal.me/myhackband)

---
Termux support:
---

> You can easily use the utility with Termux 
> on mobile phones and tablets.

    1. Download and install Termux https://play.google.com/store/apps/details?id=com.termux&hl=ru&gl=US
    2. pkg install python
    3. pip install sfd
    4. sfd --help
    5. To access the file storage: 
        termux-setup-storage
        cd ~/storage
    
    Files are destroyed even without root access and sudo.
    Read more about how to use the utility.
---

Description:
---
>Console utility for destruction,
> zeroing, and deleting files.
>
>The utility allows you to destruct files, 
> reset them to zero and delete them, 
> for complete or partial difficulty in 
> restoring them after deletion.
> 
> >Be careful! When adding folders, all files from all subfolders 
will be added recursively.
> 
> >When you run the program with all the parameters, 
> all files located at the specified path will be destroyed, 
> including those nested in other folders,
> if you specify all the arguments, then after 
> starting the utility will start working without 
> confirmation, so be very careful!

---

Help:
---

    Pass the path/paths to the file/folder as 
    parameters at startup using --p, specify the 
    number of overwrites for the file using --n 
    (30 by default), specify --d if you want the 
    utility to delete empty folders after destroying 
    files, use --y to run the program automatically, 
    use --shred for destructions (used by default), 
    --zero for zeroing, --del for zeroing and deleting.

```text
Usage: sfd [OPTIONS]

  Smart Files Destroyer - CLI utility for destroying, zeroing, and deleting
  files.

Options:
  --paths, --p TEXT   Paths to a files or folder with files, all attached
                      files and folders will be taken into account! Be
                      extremely careful and attentive when adding.

  --num, --n INTEGER  Number of overwrites. If you use the shred method, each
                      file will be overwritten the specified number of times
                      before being destroyed.

  --dirs, --d         Delete the folders?
  --yes, --y          Auto Mode, be very careful with this parameter, if you
                      specify it, the program will start and start destroying
                      files automatically.

  --shred             Overwrites random data, renames and deletes the file,
                      used by default.

  --zero              Resets and does not delete the file.
  --del               Resets and deletes the file.
  --version, --v      Displays the version of the program and exits.
  --help              Show this message and exit.


```

---
Use:
---

>Package installation:

`pip install sfd`

`sfd --paths /path/ --paths /path2/ --num 100 --dirs --yes --shred`

>Git Clone:

`git clone https://github.com/mysmarthub/sfd.git`

`cd sfd`

`pip install -r requirements.txt`

`python sfd/sfd.py --paths /path/ --p /path2/ --n 100 --d --yes --shred`


---

>To delete some files, you may need administrator rights. 
To do this, install the package with the command:

`sudo pip install sfd`

`sudo sfd --paths /path/ --paths /path2/ --num 100 --dirs --yes --shred`

>or:

`git clone https://github.com/mysmarthub/sfd.git`

`cd sfd`

`sudo pip install -r requirements.txt`

`sudo python sfd/sfd.py --paths /path/ --p /path2/ --n 100 --d --yes --shred`

---
Links:
---
>[GitHub](https://github.com/mysmarthub/sfd)

>[PyPi](https://pypi.org/project/sfd/)
 
>[Sourceforge](https://sourceforge.net/projects/smart-files-destroyer/files/latest/download)
---

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
    Email: myhackband@yandex.ru
    Copyright © 2020 Aleksandr Suvorov
