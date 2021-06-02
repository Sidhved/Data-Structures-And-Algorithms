'''An expression is called prefix, if the operator appears in the expression before the operands. (operator oparand operand)
An expression is called postfix, if the operator appears after the operands. (operand operand operator)
The program below accepts an expressin in prefix and outputs the corresponding postfix expression
Time complexity : O(n) Space Complexity : O(n)'''

def prefixtopostfix(exp):
    stack = []
    n = len(exp)
    for i in range(n-1, -1, -1):
        if exp[i].isalpha():
            stack.append(exp[i])
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1+op2+exp[i])

    print("The postfix expression is : " + stack.pop())

if __name__ == "__main__":
    exp = input("Enter the prefix expression: ")
    prefixtopostfix(exp)