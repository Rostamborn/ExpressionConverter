from TreePlot import generate
from pick import pick
import converter as c


def main():
    expression = input("Please enter you expression: ")
    postfix = ""
    options = [
        "infix To Postfix",
        "infix To Prefix",
        "postfix To Prefix",
        "postfix To Infix",
        "prefix To Infix",
        "prefix To Postfix"
    ]
    title = "Select Method"
    option, index = pick(options=options, title=title, default_index=3)
    try:
        match index:
            case 0:
                result_expressoin = c.in_to_post(expression)
                postfix = c.in_to_post(expression)
            case 1:
                result_expressoin = c.in_to_pre(expression)
                postfix = c.in_to_post(expression)
            case 2:
                result_expressoin = c.post_to_pre(expression)
                postfix = expression
            case 3:
                result_expressoin = c.post_to_in(expression)
                postfix = expression
            case 4:
                result_expressoin = c.pre_to_in(expression)
                postfix = c.pre_to_post(expression)
            case 5:
                result_expressoin = c.pre_to_post(expression)
                postfix = c.pre_to_post(expression)
            case _:
                print("No index provided!")
    except Exception:
        print("Invalid expression!!")

    print(f"Result Expression: {result_expressoin}")
    print("Infix expression Tree: ")
    tree = generate(postfix)
    tree.show()


if __name__ == '__main__':
    main()
