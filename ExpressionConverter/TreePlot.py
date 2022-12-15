from treelib import Node, Tree


def generate(postfix):
    tree = Tree()
    stack = []
    operators = '+-*/^'
    counter = 0
    for ch in postfix:
        if ch in operators:
            right = stack.pop()
            left = stack.pop()

            tree = Tree()
            id = ch+str(counter)
            tree.create_node(ch, id)
            tree.paste(id, right)
            tree.paste(id, left)
            counter += 1
            stack.append(tree)

        else:
            tree = Tree()
            id = ch+str(counter)
            tree.create_node(ch, id)
            counter += 1
            stack.append(tree)

    return stack[-1]
