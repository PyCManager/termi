 
# termi
A small, lightweight terminal emulator written in Python and Gtk 3.

![screenshot](/images/screenshot.png)


## Features
- Lightweight, only a few hundred LOC (lines of code).
- Modern design that fits in well with Gnome and other Gtk 3 based applications.
- Supports multiple tabs straight out of the box.
- Configurable via Python by editing config.py.

## Usage
termi is written purely in Python, so it must be treated as any other Python application/script. Run it using `python src/termi.py`. If you wish to make your life a little easier, you can make a bash alias for it.

To make a bash alias, edit your `.bash_rc` file and add the following:
`alias termi=python src/termi.py`. Make sure that `termi.py` is copied into a folder on your path, like `/usr/bin/` and that it is executable, you can `chmod +x` it. Once done, make sure to save (`:wq` if using vim), and then restart your *inferior* terminal.