            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
             ONELOGIN CODING CHALLENGE FRACTIONS ARITHMETIC


                             Donnie Cameron
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


Table of Contents
─────────────────

1 Problem
.. 1.1 Example 1
.. 1.2 Example 2
2 Interpretation
3 Running the Example
4 Implementation
5 Tests





1 Problem
═════════

  Write a command line program in the language of your choice that will
  take operations on fractions as an input and produce a fractional
  result.

  ‣ Legal operators shall be *, /, +, - (multiply, divide, add,
    subtract).
  ‣ Operands and operators shall be separated by one or more spaces.
  ‣ Mixed numbers will be represented by
    whole_numerator/denominator. e.g. "3_1/4"
  ‣ Improper fractions and whole numbers are also allowed as operands


1.1 Example 1
─────────────

  ┌────
  │ ? 1/2 * 3_3/4
  │ = 1_7/8
  └────


1.2 Example 2
─────────────

  ┌────
  │ ? 2_3/8 + 9/8
  │ = 3_1/2
  └────


2 Interpretation
════════════════

  I've interpreted the problem description not so much as a
  specification, but rather as a set of constraints on expected
  functionality. Therefore, because the problem description doesn't
  address negative numbers or provide a limit to the number of operators
  and operands that can form an expression, I've included support for
  both negative numbers and for unlimited operators and operands.
  Similarly, given that the description contains no mention of operator
  precedence, I've incorporated operator precedence according to the
  standard rules of mathematics.

  I've also included code to check the syntax of the expression that you
  want to evaluate.


3 Running the Example
═════════════════════

  To run the example, copy the project to your computer, change into the
  project's directory, and run the program /FractionalArithmetic.py/
  with a single string representing the expression that you want to
  evaluate.  Here's an example of how to do all of that:
  ┌────
  │ git clone git@github.com:macnod/fa.git
  │ cd fa
  │ ./FractionsArithmetic.py '10_3/2 - 1/2 * 3 - 4_1/4'
  └────
  The above /FractionsArithmetic.py/ command should give you the
  following result: '5_3/4'

  Here are some more examples (results in commented lines):
  ┌────
  │ ./FractionsArithmetic.py '5 * 5'
  │ # 35
  │ 
  │ ./FractionsArithmetic.py '0 / 1_1/4'
  │ # 0
  │ 
  │ ./FractionsArithmetic.py '5 * 5 + 25 + 50 / 10 - 4_21/42'
  │ # 50_1/2
  └────


4 Implementation
════════════════

  I've implemented the solution in Python 3.

  The /ASList/ class implements all of the functionality needed to solve
  the problem.  You create an /ASList/ object using a string
  representing the expression that you want to evaluate.  The /ASList/
  object checks the syntax of the expression and raises an exception if
  the object finds syntax errors.  The exception includes a clear
  description of the specific syntax error.

  Here's an example of how to create and use an /ASList/ object:
  ┌────
  │ try:
  │     # Parse the expression
  │     asl = ASList('1_1/2 * 2')
  │ except ValueError as e:
  │     print("Error: {}".format(str(e)))
  │     exit(1)
  │ 
  │ # Evaluate the expression and print the result
  │ print(asl.compute())
  └────

  I've implemented most of the functionality of the program using a
  doubly-linked list.  This allows me to easily obtain the values for an
  operator (previous node and next node) and to remove the associated
  nodes when I've computed the result.  Removing a node of a
  doubly-linked list is an O(1) operation, so the program progresses
  efficiently computing sub-expressions in the list.

  The program is implemented as a Python module that can be easily
  imported, but can run as a stand-alone command-line utility as well.

  For an example of how to import the module and use it in another
  program, see the code in /FractionsArithmeticTests.py/.


5 Tests
═══════

  I've included tests with this implementation.  You can run them by
  changing to the project's directory and typing the following command:
  ┌────
  │ ./FractionArithmeticTests.py -v
  └────
