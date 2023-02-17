<h1>Problem 2: A diff and a patch</h1>

<h2>Problem Statement</h2>

The Unix tools diff and patch work in such a way that one can run a diff between file A and file B, and then use patch with the output of the diff and file A to produce file B.

Write a pair of programs, a diff and and a patch, which allow one to do this same operation, to compare two files and use the output and one of the files to produce the other file. Write them to work on the shell similarly to the POSIX manual descriptions (linked above), but you have freedom in terms of the algorithms used and the nature of the actual diff output. 

When your diff application is run on two files, it should be possible to use either file together with the diff output to produce the other. (Don't write a silly concatenating diff which simply concatenates the two files. We should be able to see that the diff output is actually the differences between the files.)

<h2>Solution</h2>

<h3>Requirements</h3>

* Have latest version of Python installed in your computer.
* Move into the directory **/problem2**.

<h3>Diff</h3>
Diff: Diff, short for "difference", refers to the process of comparing two files or pieces of text and identifying the differences between them. The result of a diff operation is usually a list of changes, which can include additions, deletions, and modifications. The most common algorithm used for computing diffs is the Myers algorithm, which is widely used in version control systems like Git.

<br/>
To find the "diff" open command line interface within the directory and type

```bash
python3 diff.py file1.txt file2.txt
```

The ouput will resemble this:

```bash
* Hamlet: Do you see yonder cloud that's almost in shape of a camel?|Hamlet: Do you see the cloud over there that's almost the shape of a camel?
* Polonius: By the mass, and 'tis like a camel, indeed.|Polonius: By golly, it is like a camel, indeed.
* Hamlet: Methinks it is like a weasel.|Hamlet: I think it looks like a weasel.
* Polonius: It is backed like a weasel.|Polonius: It is shaped like a weasel.
  Hamlet: Or like a whale?
* Polonius: Very like a whale.|Polonius: It's totally like a whale.
  -- Shakespeare

```

Take the output and save it in the **"diff.txt"** file.

<h3>Patch</h3>

Patch: Patch refers to the process of applying changes to a file or piece of text based on the results of a diff or match operation. A patch file typically contains the changes needed to convert the original file to the updated version, based on the differences identified in the diff operation. Patches can be applied manually or automatically using software tools like patch or diffutils.

<br/>

To find the "patch" open command line interface within the directory and type

```bash
python3 patch.py -i diff.txt file2.txt
```

diff.txt contains the difference between file1 and file2, the -i connotation indicates that diff.txt is the difference file.
After this command the the changes will be applied to the contents of file2.txt which will transform to resemble that of file1.txt.

<h3> Error Handling </h3>
If you get the error:

```bash
Error: Unrecognized diff format
```

It means you did not copy output from the diff.py properly.
