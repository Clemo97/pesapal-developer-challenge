import sys
import getopt

def display_usage():
  print("Usage: patch [-blNR] [-c|-e|-n|-u] [-d dir] [-D define] [-i patchfile] [-o outfile] [-p num] [file]")

def apply_patch(file_path, patch_path):
  with open(file_path, "r") as file:
    linesA = file.readlines()

  with open(patch_path, "r") as diff:
    diff_lines = diff.readlines()

  line_num = 0
  for line in diff_lines:
    if line.startswith(' '):
      line_num += 1
    elif line.startswith('+'):
      linesA.insert(line_num, line[2:])
      line_num += 1
    elif line.startswith('-'):
      linesA.pop(line_num)
    elif line.startswith('*'):
      linesA[line_num] = line[2:].split("|")[0]
      line_num += 1
    else:
      print("Error: Unrecognized diff format")
      return 1

  with open(file_path, "w") as output:
    for line in linesA:
      output.write(line)

  return 0


def main():
  try:
    opts, args = getopt.getopt(sys.argv[1:], "blNRcenu:d:D:i:o:p:r:")
  except getopt.GetoptError as err:
    print(str(err))
    display_usage()
    sys.exit(1)

  num = 0
  patchfile = None
  outfile = None
  rejectfile = None
  bFlag = False
  lFlag = False
  NFlag = False
  RFlag = False
  mode = -1
  dir = ""

  for opt, arg in opts:
    if opt == '-b':
      bFlag = True
    elif opt == '-l':
      lFlag = True
    elif opt == '-N':
      NFlag = True
    elif opt == '-R':
      RFlag = True
    elif opt == '-c':
      mode = 0
    elif opt == '-e':
      mode = 1
    elif opt == '-n':
      mode = 2
    elif opt == '-u':
      mode = 3
    elif opt == '-d':
      dir = arg
    elif opt == '-D':
      pass
    elif opt == '-i':
      patchfile = arg
    elif opt == '-o':
      outfile = arg
    elif opt == '-p':
      num = int(arg)
    elif opt == '-r':
      rejectfile = arg
    else:
      print("Error: Unrecognized option")
      display_usage()
      sys.exit(1)

  if len(args) < 1:
    print("Error: Missing file argument")
    display_usage()
    sys.exit(1)

  file = args[0]

  if patchfile is None:
    print("Error: Missing -i option")
    display_usage()
    sys.exit(1)

  apply_patch(file, patchfile)


if __name__ == '__main__':
  main()
