
An Antlr4/Jython Proof of Concept.
==================================

Setup
-----
The following steps assume:
 1. jython is in your system's execution path - Jython 2.77b1 was used.
 2. The ANTLR v4 library (jar file) is in the CLASSPATH.
 3. a4 command invokes the ANTLR v4 Tool.

Steps
-----
 1. cd to the repository directory
 2. a4 R.g4
 3. javac *.java
 4. jython TestR.py t.R

