** start of main.py **

def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes = ""
    answers = ""

    for i, problem in enumerate(problems):
        parts = problem.split()
        left = parts[0]
        operator = parts[1]
        right = parts[2]

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."

        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(left), len(right)) + 2
        top = left.rjust(width)
        bottom = operator + " " + right.rjust(width - 2)
        line = "-" * width

        if operator == "+":
            result = str(int(left) + int(right))
        else:
            result = str(int(left) - int(right))
        res = result.rjust(width)

        if i < len(problems) - 1:
            space = "    "
        else:
            space = ""

        first_line += top + space
        second_line += bottom + space
        dashes += line + space
        answers += res + space

    if show_answers:
        arranged_problems = first_line + "\n" + second_line + "\n" + dashes + "\n" + answers
    else:
        arranged_problems = first_line + "\n" + second_line + "\n" + dashes

    return arranged_problems

** end of main.py **
