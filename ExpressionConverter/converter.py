def priority(char):
    if char == '^':
        return 3
    elif char == '/' or char == '*':
        return 2
    elif char == '+' or char == '-':
        return 1
    else:
        return 0


def reverse(input):
    input_reversed = ''
    for i in range(len(input)-1, -1, -1):
        if input[i] == '(':
            input_reversed += ')'
        elif input[i] == ')':
            input_reversed += '('  # )
        else:
            input_reversed += input[i]

    return input_reversed


# infix to postfix conversion
def in_to_post(infix):
    postfix = ''
    stack = []
    operators = '+-*/^()'
    for char in infix:
        if char not in operators:
            postfix += char
        elif char == '(':
            stack.append('(')  # )
        elif char == '^':
            stack.append('^')
        elif char == ')':
            while (len(stack) > 0) and stack[-1] != '(':  # )
                operator = stack[-1]
                stack.pop()
                postfix += operator
            if len(stack) > 0:
                stack.pop()

        else:
            while (len(stack) > 0) and priority(char) <= priority(stack[-1]):
                operator = stack[-1]
                stack.pop()
                postfix += operator
            stack.append(char)

    while len(stack) > 0:
        operator = stack[-1]
        stack.pop()
        postfix += operator

    return postfix


# infix to prefix conversion
def in_to_pre(infix):
    infix_reversed = reverse(infix)
    reversed_pre = in_to_post(infix_reversed)
    return reverse(reversed_pre)


# postfix to infix conversion
def post_to_in(input):
    stack = []
    operators = '+-*/^'

    for i in input:
        if i in operators:
            a = stack.pop()
            b = stack.pop()
            c = '(' + b + i + a + ')'
            stack.append(c)
        else:
            stack.append(i)

    return stack[-1]


# postfix to prefix convesion
def post_to_pre(input):
    stack = []
    operators = '+-*/^'

    for i in input:
        if i in operators:
            a = stack.pop()
            b = stack.pop()
            c = i+b+a
            stack.append(c)
        else:
            stack.append(i)

    return stack[-1]


# prefix to infix conversion
def pre_to_in(input):
    stack = []
    operators = '+-*/^'
    input = input[::-1]

    for i in input:
        if i in operators:
            a = stack.pop()
            b = stack.pop()
            c = '(' + a + i + b + ')'
            stack.append(c)
        else:
            stack.append(i)

    return stack[-1]


# prefix to postfix conversion
def pre_to_post(input):
    stack = []
    operators = '+-*/^'
    input = input[::-1]

    for i in input:
        if i in operators:
            a = stack.pop()
            b = stack.pop()
            c = a+b+i
            stack.append(c)
        else:
            stack.append(i)

    return stack[-1]
