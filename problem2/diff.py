import sys

def compareLines(lineA, lineB):
    if lineA == lineB:
        return " "
    else:
        return lineA + "|" + lineB

# Parser
option = 0
contextLines = 3
showLineNumbers = False
for i in range(1, len(sys.argv)):
    if sys.argv[i][0] == '-':
        if sys.argv[i][1] == 'c':
            option = 1
        elif sys.argv[i][1] == 'e':
            option = 2
        elif sys.argv[i][1] == 'f':
            option = 3
        elif sys.argv[i][1] == 'u':
            option = 4
        elif sys.argv[i][1] in ['C', 'U']:
            if len(sys.argv[i]) > 2:
                contextLines = int(sys.argv[i][2:])
            else:
                contextLines = int(sys.argv[i+1])
            option = 5 if sys.argv[i-1][1] == 'C' else 6
        elif sys.argv[i][1] == 'b':
            showLineNumbers = True
        elif sys.argv[i][1] == 'r':
            pass
        else:
            print("diff: illegal option -- {}".format(sys.argv[i][1]))
            print("Usage: diff [-c|-e|-f|-u|-C n|-U n] [-br] file1 file2")
            sys.exit(1)
    else:
        break

# Check for two input files are exact
if len(sys.argv) - option < 3:
    print("Usage: diff [-c|-e|-f|-u|-C n|-U n] [-br] file1 file2")
    sys.exit(1)

# Read both input files
with open(sys.argv[-2]) as fileA, open(sys.argv[-1]) as fileB:

    linesA = fileA.read().splitlines()
    linesB = fileB.read().splitlines()


    lines = max(len(linesA), len(linesB))
    for i in range(lines):
        if i >= len(linesA):
            print("+", linesB[i])
        elif i >= len(linesB):
            print("-", linesA[i])
        else:
            diff = compareLines(linesA[i], linesB[i])
            if diff[0] == ' ':
                print(" ", linesA[i])
            else:
                print("*", diff)

sys.exit(0)
