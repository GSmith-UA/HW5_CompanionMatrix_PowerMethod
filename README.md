This is a set of files that should solve M589A Assignment 5.
The driver file contains two functions: construct companion matrix and main()
The first is self explanatory. The second runs the code necessary to solve/print the answers to Q2.1,Q2.2,Q2.3.
Inside main() these should be indicated with comments.

The file powerMethod contains a function for finding the leading eigenvalue.
Since there is a chance we return a value out of spec (max iterations reached) I also return a boolean so that downstream you can check whether or not that eigenvalue is out of spec.
For this assignment it is probably overkill
The file also contains powerMethod_deflation() which runs the original powerMethod() multiple times to get the leading eigenvalues.
As it stands this method only returns the eigenvalues and a list of whether they are in spec

Finally synthDiv performs synthetic division.
There is a function called synthDiv_multiple() that allows you to pass in multiple roots
I had a little trouble with typing and ended up with nested lists/arrays so there is some weirdness in formatting at the end.
This file also contains the quadSolve() which just runs the quadratic formula.
There is probably a better, safer, more stable, etc. way to do this but I don't think it matters for this assignment.

Should be able to open the terminal and run "python3 driver.py" and it should return all the answers to screen shot for assignment.
