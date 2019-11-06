#!/usr/bin/python3

import sys, re, os
from fractions import Fraction

class ASListNode:
    """

    A node of ASList 

    """
    def __init__(self, value=None, prev_node=None, next_node=None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node


class ASList:
    """" 
    
    This is a syntax list that resembles the Abstract Syntax Tree
    (AST) that programming-language compilers and interpreteres use,
    but which is implemented as a Doubly Linked List, and coded
    specifically for reading and evaluating expressions like the ones
    in the OneLogin programming challenge "Fractions".

    """
    def __init__(self, expression=None):
        self.head = None
        self.tail = None
        self.length = 0
        if expression:
            self.from_list(expression.split())
        self.operations = self._operations()
        self.operators = []
        for precedence in self.operations:
            for operator in precedence.keys():
                self.operators.append(operator)
        self.re_valid_value = re.compile("^(-|\+)?(\d+_\d+/\d+|\d+/\d+|\d+)$")
        self.error = self.list_syntax_ok()
        if self.error:
            raise ValueError(self.error)

    def _operations(self):
        # List operations here, in groups of decreasing precedence.
        # For example, if the * operator has a higher precedence than
        # the + operator, they should be in different groups and the
        # group with the * operator should come before the group with
        # the + operator.
        return [
            {
                '*': (lambda f, x, y: f.multiply(x, y)),
                '/': (lambda f, x, y: f.divide(x, y))
            },
            {
                '+': (lambda f, x, y: f.add(x, y)),
                '-': (lambda f, x, y: f.subtract(x, y))
            }
        ]

    def from_list(self, values=[]):
        self.head = self.tail = None
        self.length = 0
        if values:
            prev_node = ASListNode(values[0])
            self.head = prev_node
            self.length = len(values)
            node = None
            for index in range(1, self.length):
                node = ASListNode(values[index])
                prev_node.next_node = node
                node.prev_node = prev_node
                prev_node = node
            self.tail = self.head if node is None else node
        return self

    def valid_value(self, value):
        return self.re_valid_value.search(value)

    def list_syntax_ok(self):
        expect_operator = True
        fail = ''
        for node in self.nodes():
            expect_operator = not expect_operator
            value = node.value
            if expect_operator:
                if value in self.operators:
                    continue
                else:
                    fail = "Expected operator in place of '{}'".format(
                        value)
                    break
            else:
                if value in self.operators:
                    fail = "Expected value in place of operator '{}'".format(
                        value)
                    break
                elif self.valid_value(value):
                    continue
                else:
                    fail = "Can't parse value '{}'".format(node.value)
                    break
        return fail

    def remove_node(self, node):
        if node is None or self.length == 0:
            return None
        if self.length == 1 and node is self.head:
            self.head = self.tail = None
            self.length = 0
            return node
        if node is self.head:
            self.head = node.next_node
            self.head.prev_node = None
            self.length -= 1
            return node
        if node is self.tail:
            self.tail = node.prev_node
            self.tail.next_node = None
            self.length -= 1
            return node
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node
        self.length -= 1
        return node

    def nodes(self):
        node = self.head
        while node:
            yield node
            node = node.next_node

    def print_nodes(self):
        values = []
        for node in self.nodes():
            values.append(node.value)
        print(values)
        print("")

    def compute(self):
        while self.length > 1:
            for precedence in self.operations:
                for node in self.nodes():
                    if node.value in precedence:
                        node.value = precedence[node.value](
                            self,
                            node.prev_node.value,
                            node.next_node.value)
                        self.remove_node(node.prev_node)
                        self.remove_node(node.next_node)
                        break
                    else:
                        continue
                    break
        return self.head.value if self.length else 0

    def integer_and_fraction(self, n):
        if re.search('_', n):
            integer, fraction = n.split('_')
            integer = int(integer)
        elif re.search('/', n):
            integer = 0
            fraction = n
        else:
            integer = int(n)
            fraction = 0
        if fraction:
            numerator, denominator = list(
                map(lambda x: int(x), fraction.split('/')))
        else:
            numerator, denominator = 0, 1
        return integer, Fraction(numerator, denominator)

    def format_result(self, result):
        if result >= 1:
            integer = int(result.numerator / result.denominator)
            numerator = result.numerator % result.denominator
        else:
            integer = 0
            numerator = result.numerator
        if result.denominator == 1 and integer == 0:
            integer = result.numerator
            numerator = 0
        if integer == 0 and result == 0:
            return "0"
        return "{}{}{}".format(
            "{}".format(integer) if integer else "",
            "_" if integer and numerator else "",
            "{}/{}".format(numerator, result.denominator) if numerator else "")

    def add(self, a, b):
        ai, af = self.integer_and_fraction(a)
        bi, bf = self.integer_and_fraction(b)
        result = ai + bi + af + bf
        return self.format_result(result)

    def subtract(self, a, b):
        ai, af = self.integer_and_fraction(a)
        bi, bf = self.integer_and_fraction(b)
        result = ai - bi + af - bf
        return self.format_result(result)

    def multiply(self, a, b):
        ai, af = self.integer_and_fraction(a)
        bi, bf = self.integer_and_fraction(b)
        result = (ai + af) * (bi + bf)
        return self.format_result(result)

    def divide(self, a, b):
        ai, af = self.integer_and_fraction(a)
        bi, bf = self.integer_and_fraction(b)
        a_imp = Fraction(ai * af.denominator + af.numerator, af.denominator)
        b_imp = Fraction(bi * bf.denominator + bf.numerator, bf.denominator)
        result = a_imp / b_imp
        return self.format_result(result)
                    

if __name__ == '__main__':
    def usage():
        script_name = os.path.basename(__file__)
        message = "\n".join(
            ["Usage: {} '{{expression}}'".format(script_name),
             "       | {} --help|-h".format(script_name),
             "       | {}".format(script_name),
             "           {expression}: {val} {op} {val} [{op} {val}]...",
             "           {op}:         + | - | * | /",
             "           {val}:        [+ | -]{int}_{int}/{int}",
             "                         | [+ | -]{int}",
             "                         | [+ | -]{int}/{int}",
             "           {int}:        a positive integer",
             "Examples:",
             "    {} '1 + 2 + 1_1/2 * -2 + 5/4'".format(script_name),
             "    => {}".format(ASList('1 + 2 + 1_1/2 * -2 + 5/4').compute()),
             "    {} '1/2 * 3_3/4'".format(script_name),
             "    {} '2_3/8 + 9/8'".format(script_name)])
        print(message)

    if len(sys.argv) > 2 or len(sys.argv) < 2:
        usage()
        exit(1)
    if (len(sys.argv) == 2 and (
            sys.argv[1] == '--help' or sys.argv[1] == '-h')):
        usage()
        exit(0)
    expression = sys.argv[1] if len(sys.argv) == 2 else '0'
    try:
        asl = ASList(expression)
    except ValueError as e:
        print("Error: {}".format(str(e)))
        exit(1)
    print(asl.compute())
