"""
termi

A small, lightweight terminal emulator written in Python and Gtk 3.
Copyright (c) 2019 dhilln.
"""

import gi
gi.require_version("Gtk", "3.0")

import os
import config

from vte import VTETerminal
from shutil import which
from gi.repository import Gtk, Gio, GLib, Vte

class MainWindow(Gtk.Window):
  """
  Main window for the application
  """

  def __init__(self):
    Gtk.Window.__init__(self, title="termi")
    self.set_default_size(640, 480)
    self.tab_count = 0

    self.setup_window()

  def setup_window(self):
    # Create the header bar
    header = Gtk.HeaderBar(title="termi")
    header.props.show_close_button = True
    self.set_titlebar(header)

    # Add the Notebook
    self.notebook = Gtk.Notebook()
    self.notebook.set_scrollable(True)
    self.notebook.props.tab_pos = Gtk.PositionType.BOTTOM
    self.create_tab()

    self.add(self.notebook)

    # Add a button for creating tabs
    new_tab_button = Gtk.Button()
    new_tab_icon = Gio.ThemedIcon(name="tab-new-symbolic")
    new_tab_button.add(Gtk.Image.new_from_gicon(new_tab_icon, Gtk.IconSize.BUTTON))
    new_tab_button.connect("clicked", self.on_create_tab_clicked)
    #self.create_tab()

    # Add a button for configuring termi
    configure_button = Gtk.Button()
    configure_icon = Gio.ThemedIcon(name="applications-system-symbolic")
    configure_button.add(Gtk.Image.new_from_gicon(configure_icon, Gtk.IconSize.BUTTON))
    configure_button.connect("clicked", self.on_configure_clicked)

    header.pack_start(new_tab_button)
    header.pack_start(configure_button)

  def create_vte(self, shell="/bin/bash"):
    """
    Create a new VTE (terminal) using the specified shell.
    
    :shell: The shell to use, defaults to /bin/bash
    """
    self.vte = VTETerminal()
    self.vte.configure(
    {
      "shell": config.shell,
      "fallback_shell": config.fallback_shell,
      "working_directory": config.working_directory,
      "audible_bell": config.audible_bell,
      "editor": config.editor
    })

    return self.vte.spawn_session()

  def create_err_dialog(self, title, message):
    dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, title)
    dialog.format_secondary_text(message)
    return dialog

  def create_tab(self):
    """
    Create a new tab with a terminal inside it
    """
    terminal = self.create_vte()

    # Create the label and close button
    tab_hbox = Gtk.Box(spacing=4)
    tab_label = Gtk.Label(label=f"Termi ({self.tab_count})")
    tab_hbox.pack_start(tab_label, True, True, 0)

    close_tab_icon = Gio.ThemedIcon(name="window-close-symbolic")
    close_tab_button = Gtk.Button()
    close_tab_button.add(Gtk.Image.new_from_gicon(close_tab_icon, Gtk.IconSize.MENU))
    close_tab_button.connect("clicked", self.on_close_tab_clicked)

    tab_hbox.pack_start(close_tab_button, True, True, 0)
    tab_hbox.show_all()

    self.notebook.append_page(terminal, tab_hbox)
    self.tab_count = self.notebook.get_n_pages()

  def on_close_tab_clicked(self, button):
    """
    Close the current tab if there is one open. Otherwise, exit the application.
    """
    page = self.notebook.get_current_page()
    if self.tab_count > 1:
      self.notebook.remove_page(page)
      self.tab_count -= 1
    else:
      Gtk.main_quit()

    
  def on_create_tab_clicked(self, button):
    """
    Create a new tab.
    """
    self.create_tab()
    self.notebook.show_all()

  def on_configure_clicked(self, button):
    """
    Opens config.py up in Visual Studio Code/Atom/Sublime if it is installed.
    """

    if which(self.vte.options.editor) != None:
      os.system(f"{self.vte.options.editor} config.py")
    else:
      dialog = self.create_err_dialog("No editor found", f"Please make sure that {self.vte.options.editor} is installed and in your path!")
      dialog.run()
      dialog.destroy()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
