import sys
import os

print("foo.__main__ loaded")
print("RUNFILES_MANIFEST_FILE: {}".format(os.environ.get("RUNFILES_MANIFEST_FILE", "")))

from bar import baz

if __name__ == "__main__":
    sys.exit(0)
