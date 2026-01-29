"""Check if the script is running inside a virtual environment."""

import sys

if getattr(sys, "base_prefix", sys.prefix) != sys.prefix:
    print("You are running inside a virtual environment!")
else:
    print("You are NOT in a virtual environment.")
