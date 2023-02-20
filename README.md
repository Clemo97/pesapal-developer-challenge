# Pesapal Developer Challenge
This is a solution for [The Pesapal Developer Challenge](https://pesapal.freshteam.com/jobs/2OU7qEKgG4DR/junior-developer-23) *Problem 2: A diff and a patch.*, written in Python3.

## Problem Statement
The Unix tools diff and patch work in such a way that one can run a diff between file A and file B, and then use patch with the output of the diff and file A to produce file B.

Write a pair of programs, a diff and and a patch, which allow one to do this same operation, to compare two files and use the output and one of the files to produce the other file. Write them to work on the shell similarly to the POSIX manual descriptions (linked above), but you have freedom in terms of the algorithms used and the nature of the actual diff output. 

When your diff application is run on two files, it should be possible to use either file together with the diff output to produce the other. (Don't write a silly concatenating diff which simply concatenates the two files. We should be able to see that the diff output is actually the differences between the files.)


## Setup and running the solution
1. Clone or download this repository
2. Make sure python3 is installed and accessible from the terminal. At least version 3.8.10 is needed. [Installation Guide 1](https://wiki.python.org/moin/BeginnersGuide/Download), [Installation Guide 2](https://www.digitalocean.com/community/tutorials/install-python-windows-10)
3. Open a new terminal session and navigate to the solution folder

## "diff"

1. Run `python3 diff.py fileA.txt fileB.txt`, this will output the difference between `fileA.txt` and `fileB.txt`. The output will look like this:

```bash
@@ -1,7 +1,7 @@
-Hamlet: Do you see yonder cloud that's almost in shape of a camel?
-Polonius: By the mass, and 'tis like a camel, indeed.
-Hamlet: Methinks it is like a weasel.
-Polonius: It is backed like a weasel.
-Hamlet: Or like a whale?
-Polonius: Very like a whale.
--- Shakespeare
\ No newline at end of file
+Clement: Do you see the cloud over there that's almost the shape of a camel?
+Polonius: By golly, it is like a camel, indeed.
+Clement: I think it looks like a weasel.
+Polonius: It is shaped like a weasel.
+Clement: Or like a whale?
+Polonius: It's totally like a whale.
+-- Miguna Miguna
\ No newline at end of file

```

2. Copy the contents of the output and store them in the `diff.txt` file.

## "patch"

1. Run the script below to apply `patch` function to fileA.txt this will produce fileB.txt contents.

```bash 
python3 patch.py fileA.txt diff.txt"
```
### output

```bash
Clement: Do you see the cloud over there that's almost the shape of a camel?
Polonius: By golly, it is like a camel, indeed.
Clement: I think it looks like a weasel.
Polonius: It is shaped like a weasel.
Clement: Or like a whale?
Polonius: It's totally like a whale.
```


## Troubleshooting
- Error (on Windows OS): `python is not recognized`. This can occur if the python executable was not added to PATH during installation. Follow [this guide](https://www.digitalocean.com/community/tutorials/install-python-windows-10) and make sure `Add Python to PATH is checked`.
- Error (on Linux or macOS): `python is not found` or `python syntax error`. This might indicate that both python2 and python3 are installed side by side. Try running the scripts by substituting `python` with `python3`.
- Error (on Linux or macOS): `Error: Unrecognized diff format`. It means you did not copy output from the diff.py properly.

## Solution Overview
The solution consists of 2 scripts:
- `diff.py`, which produces the difference bewtween `fileA` and `fileB`
- `patch.py`, which takes `diff.txt` and `fileA` and produces `fileB` in order to do it vice verse the `revert` argument has to be changed to **True**, like so:

```python
def apply_patch(old_file: Path, new_file: Path, revert=True):
```
then `python3 patch.py fileA.txt diff.txt` will produce `fileA`.



## Code Overview
The `diff.py` script takes in two strings a and b, and returns a unified string diff between the two strings. It first uses the difflib library to compute the unified diff between the two strings, and then trims the top two lines from the resulting diff (which typically contain metadata about the files being diffed). If the two input strings are identical, an empty string is returned.

The `patch.py` takes in a `fileA` and `dfii.txt`, and returns the newer version of the string after applying the patch. If the `revert` flag is set to True, the function instead returns the older version (`fileB`) of the file. The function parses the patch string and applies the changes to the input string accordingly, returning the updated string.

The `patch.py`is implemented using the difflib.unified_diff function, which computes the differences between the two input strings using a **unified diff format**. The **apply_patch** function is implemented by parsing the patch string using regular expressions to extract information about the changes to be made, and then applying those changes to the input string.

Overall, this code provides a simple and lightweight way to compute and apply diffs and patches to text files.
