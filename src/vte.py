import gi
gi.require_version("Gtk", "3.0")

import os, config
from shutil import which
from gi.repository import Gtk, Gio, GLib, Vte


class VTETerminal:
  """
  Wrapper around Gtk 3's Vte.Terminal class
  """

  def __init__(self):
    self.terminal = Vte.Terminal()
    self.options = {}

  def configure(self, options):
    """
    Configure the terminal with the given options.
    """

    if options != None:
      self.options = options
    else:
      raise ValueError("Cannot configure a VTETerminal with NoneType as the options.")

  def spawn_session(self):
    """
    Spawn a session with the given options and return the terminal.
    """
    self.terminal.spawn_sync(
      Vte.PtyFlags.DEFAULT, self.options["working_directory"],
      [self.options["shell"]], [],
      GLib.SpawnFlags.DO_NOT_REAP_CHILD, None, None,
    )

    return self.terminal