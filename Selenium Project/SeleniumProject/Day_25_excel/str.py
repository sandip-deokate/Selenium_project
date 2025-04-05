
def MathChallenge(equation):
    lhs, rhs = equation.split('=')
    rhs = rhs.strip()
    lhs = lhs.replace(' ', '')
    rhs = rhs.replace(' ', '')

    operators = ['+', '-', '*', '/']

    def eval_expression(num1, operator, num2):
        if operator == '+':
            return num1 + num2

        elif operator == '-':
            return num1 - num2

        elif operator == '*':
            return num1 * num2

        elif operator == '/':
            return num1 // num2 if num2 != 0 else None

        return None


    def solve(lhs, rhs):
        for operator in operators:
            if operator in lhs:
                num1, num2 = lhs.split(operator)
                num1 = num1.replace(' ', '')
                num2 = num2.replace(' ', '')
                if 'x' in num1:
                    for digit in range(10):
                        candidate_num1 = num1.replace('x', str(digit))
                        if candidate_num1.isdigit():
                            if eval_expression(int(candidate_num1), operator, int(num2)) == int(rhs):
                                return digit

                elif 'x' in num2:
                    for digit in range(10):
                        candidate_num2 = num2.replace('x', str(digit))
                        if candidate_num2.isdigit():
                            if eval_expression(int(num1), operator, int(candidate_num2)) == int(rhs):
                                return digit

        return None


    def solve_rhs(lhs, rhs):
        for digit in range(10):
            candidate_rhs = rhs.replace('x', str(digit))
            if candidate_rhs.isdigit():
                if eval(lhs) == int(candidate_rhs):
                    return digit

        return None


    if 'x' in lhs:
        return solve(lhs, rhs)
    elif 'x' in rhs:
        return solve_rhs(lhs, rhs)
    else:
        return None


# Example usage:
input_equation1 = "3x + 12 = 46"
print(MathChallenge(input_equation1))  # Should output 4


input_equation2 = "4 - 2 = x"
print(MathChallenge(input_equation2))  # Should output 2


input_equation3 = "5 * 3 = 15"
print(MathChallenge(input_equation3))  # Should output None


input_equation4 = "4 / 2 = x"
print(MathChallenge(input_equation4))  # Should output 2


input_equation5 = "12 = 3 * x"
print(MathChallenge(input_equation5))  # Should output 4
