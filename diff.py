from __future__ import print_function
from pathlib import Path

import difflib
import re
import sys
import argparse


_no_eol = "\ No newline at end of file"
_hdr_pat = re.compile("^@@ -(\d+),?(\d+)? \+(\d+),?(\d+)? @@$")

def get_diff(old_file: Path, new_file: Path, output_file: Path = None):
  """
  Get unified string diff between two strings. Trims top two lines.
  Returns empty string if strings are identical.
  """
  file_1 = open(old_file).read()
  file_2 = open(new_file).read()

  diffs = difflib.unified_diff(file_1.splitlines(True),file_2.splitlines(True),n=0)
  try: _,_ = next(diffs),next(diffs)
  except StopIteration: pass
  # diffs = list(diffs); print(diffs)
  return ''.join([d if d[-1] == '\n' else d+'\n'+_no_eol+'\n' for d in diffs])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("old_file_version")
    parser.add_argument("new_file_version")
    args = parser.parse_args()

    old_file = Path(args.old_file_version)
    new_file = Path(args.new_file_version)

    some_diff = get_diff(old_file, new_file)
    sys.stdout.writelines(some_diff)


if __name__ == '__main__':
  main()
