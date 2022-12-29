from TreePlot import generate
import converter as c
from sys import exit


def main():
    expression = input("Please enter you expression: ")
    operators = "+-*/^"
    postfix = ""

    if (expression[0] in operators) and (expression[-1] in operators):
        print("Invald Error")
        exit()
    elif expression[0] in operators:
        result_expressoins = (c.pre_to_in(expression), c.pre_to_post)
        postfix = c.pre_to_post(expression)
    elif expression[-1] in operators:
        result_expressoins = (c.post_to_pre(expression),
                              c.post_to_in(expression))
        postfix = expression
    else:
        result_expressoins = (c.in_to_post(expression),
                              c.in_to_pre(expression))
        postfix = c.in_to_post(expression)

    print(result_expressoins[0])
    print(result_expressoins[1])
    print()
    print("Infix expression Tree: ")
    tree = generate(postfix)
    tree.show()


if __name__ == '__main__':
    main()
