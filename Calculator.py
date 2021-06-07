import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)
        self.stack = ArrayStack.ArrayStack()
        self.expression = ""

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def matched_expression(self, s: str) -> bool:
        self.expression = s
        for i in s:
            if i == '(':
                self.stack.push(i)
            elif i == ')':
                if not self.stack:
                    return False
                else:
                    self.stack.pop()
        if not self.stack:
            return True
        else:
            return False

    def printExpression(self) -> str:
        s = []
        x = ""
        for i in range(len(self.expression)):
            s.append(self.expression[i])
        for j in range(len(s)):
            if s[j].isalpha():
                s[j] = self.dict.find(s[j])
        for k in range(len(s)):
            x += str(s[k])
        return x

    def build_parse_tree(self, exp: str):
        t = BinaryTree.BinaryTree()
        t.r = t.Node('')
        u = t.r
        operators = ["+", "-", "*", "/"]
        i = 0
        while i != len(exp):
            if exp[i] == '(':
                u.insert_left()
                u = u.left
            elif exp[i] in operators:
                u.x = exp[i]
                u.insert_right()
                u = u.right
            elif exp[i] == ')':
                u = u.parent
            else:
                u.x = exp[i]
                u = u.parent
            i += 1
        return t

    def _evaluate(self, root):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if root.left is not None and root.right is not None:
            m = op[root.x]
            return m(self._evaluate(root.left), self._evaluate(root.right))
        elif root.left is None and root.right is None:
            t = self.dict.find(root.x)
            if t is not None:
                return t
            return root.x
        else:
            if root.left is not None:
                return self._evaluate(root.left)
            else:
                return self._evaluate(root.right)

    def evaluate(self, exp):
        parseTree = self.build_parse_tree(exp)
        return round(self._evaluate(parseTree.r), 2)
