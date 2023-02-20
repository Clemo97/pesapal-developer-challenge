from __future__ import print_function
from pathlib import Path

import difflib
import re
import sys
import argparse


_no_eol = "\ No newline at end of file"
_hdr_pat = re.compile("^@@ -(\d+),?(\d+)? \+(\d+),?(\d+)? @@$")


def apply_patch(old_file: Path, new_file: Path, revert=False):
  """
  Apply patch to string 's' to recover newer string.
  If revert is True, treat 's' as the newer string, recover older string.
  """
  file_1 = open(old_file).read()
  file_2 = open(new_file).read()


  s = file_1.splitlines(True)
  p = file_2.splitlines(True)
  t = ''
  i = sl = 0
  (midx,sign) = (1,'+') if not revert else (3,'-')
  while i < len(p) and p[i].startswith(("---","+++")): i += 1 # skip header lines
  while i < len(p):
    m = _hdr_pat.match(p[i])
    if not m: raise Exception("Bad patch -- regex mismatch [line "+str(i)+"]")
    l = int(m.group(midx))-1 + (m.group(midx+1) == '0')
    if sl > l or l > len(s):
      raise Exception("Bad patch -- bad line num [line "+str(i)+"]")
    t += ''.join(s[sl:l])
    sl = l
    i += 1
    while i < len(p) and p[i][0] != '@':
      if i+1 < len(p) and p[i+1][0] == '\\': line = p[i][:-1]; i += 2
      else: line = p[i]; i += 1
      if len(line) > 0:
        if line[0] == sign or line[0] == ' ': t += line[1:]
        sl += (line[0] != sign)
  t += ''.join(s[sl:])
  return t

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("old_file_version")
    parser.add_argument("new_file_version")

    args = parser.parse_args()

    old_file = Path(args.old_file_version)
    new_file = Path(args.new_file_version)

    some_diff = apply_patch(old_file, new_file)
    sys.stdout.writelines(some_diff)


if __name__ == '__main__': main()
