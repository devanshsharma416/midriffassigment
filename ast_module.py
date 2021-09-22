
# import ast

# code = ast.parse("print('Hello Learner ! Welcome to JavaTpoint')")
# print(code)

# exec(compile(code, filename="", mode="exec"))


# import ast

# expression = '6 + 8'
# code = ast.parse(expression, mode='eval')

# print(eval(compile(code, '', mode='eval')))
# print(ast.dump(code))


# import ast


# ast_tree_ast = ast.parse('''
# subjects = ['computer science', 'alorithm']
# name = 'Ricky'

# for fruit in fruits:
#     print('{} learn {}'.format(name, subjects))
# ''')

# print(ast.dump(ast_tree_ast))

# list1 = ['abc', 'xyzaad', '22', 'K', '2dk']

# str1 = input("Enter the string")
# str2 = str1[::-1]
# if str1 == str2:
#     print("The given string is a palindrom")
# else:
#     print("The given string is not a palindrom")

# sentence = "This is a cat"
# sen = sentence.split(' ')
# for i in sen:
#     rev_str = i[::-1]
#     print(rev_str, end = ',')

# import ast
# class Visitor(ast.NodeVisitor):
#     def visit_Str(self, node):
#         print('String Node: "' + node.s + '"')

# class MyTransformer(ast.NodeTransformer):
#     def visit_Str(self, node):
#         return ast.Str('str: ' + node.s)

# parsed = ast.parse("print('Welcome to the Javatpoint')")
# MyTransformer().visit(parsed)
# Visitor().visit(parsed)

import ast
from pprint import pprint


def main():
    with open("ast_module.py", "r") as source:
        ast_tree = ast.parse(source.read())

    analysis = Analyzer()
    analysis.visit(ast_tree)
    analysis.report()


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {"import": [], "from": []}

    def node_visit(self, node):
        for alias in node.names:
            self.stats["import"].append(alias.name)
        self.generic_visit(node)

    def node_visitFrom(self, node):
        for alias in node.names:
            self.stats["from"].append(alias.name)
        self.generic_visit(node)

    def report(self):
        pprint(self.stats)


if __name__ == "__main__":
    main()


