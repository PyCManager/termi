import os

# The custom shell for termi to use.
# Default: os.environ["SHELL"]
shell = os.environ["SHELL"]

# The fallback shell for termi to use incase the normal shell breaks.
fallback_shell = "/bin/sh"

# The working directory for the terminal to use when creating new VTEs.
# Default: os.environ["HOME"]
working_directory = os.environ["HOME"]

# Whether or not termi should use an audible bell. Default is False
audible_bell = False

# The default editor for termi to open the configuration file in 
# when the configure button is pressed.
editor = "mousepad"
