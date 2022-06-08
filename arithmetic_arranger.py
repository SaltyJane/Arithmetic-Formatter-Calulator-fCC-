import sys

def arithmetic_arranger(problems: list, show_ans=False):
    line1, line2, line3, line4 = "", "", "", ""
    # if more than 5 problems, error
    if len(problems) > 5:
        return "Error: Too many problems."
        sys.exit()
    else:
        # for each problem, split into components
        for index, prob in enumerate(problems):
            separated_str = prob.split()
            number1 = separated_str[0]
            operator = separated_str[1]
            number2 = separated_str[2]
            # error handling
            if (operator != '+') and (operator != '-'):
                return "Error: Operator must be '+' or '-'."
                sys.exit()
            if len(number1) > 4 or len(number2) > 4:
                return "Error: Numbers cannot be more than four digits."
                sys.exit()
            if (not number1.isnumeric()) or (not number2.isnumeric()):
                return "Error: Numbers must only contain digits."
                sys.exit()
            # error handling complete
            # start actual function

            # find the max string length
            max_len = max([len(number1), len(number2)])

            # calculate result
            if operator == '+':
                result = int(number1) + int(number2)
                # result needs to be a string in order to use it later
                result = str(result)
            elif operator == '-':
                result = int(number1) - int(number2)
                result = str(result)

            # first line is just the first number right-aligned with an extra 2 spaces of padding (to make up for the operator and space on line2)
            line1 += number1.rjust(max_len + 2)
            line2 += operator + ' ' + number2.rjust(max_len)
            # third line is just hyphens
            line3 += ''.rjust(max_len + 2, '-')
            # if result is negative, get rid of minus sign so that it's inline with the operator vertically (visually more pleasing but fails the tests)
            # if int(result) < 0:
            #     result = result[1:]
            #     line4 += '-' + ' ' + result.rjust(max_len)
            # else:
            #     line4 += result.rjust(max_len + 2)
            line4 += result.rjust(max_len + 2)
            # add a padding-right for the next operation if not the last problem to solve
            if(index < len(problems) - 1):
                line1 += ''.rjust(4)
                line2 += ''.rjust(4)
                line3 += ''.rjust(4)
                line4 += ''.rjust(4)
    # add new lines at the end (this block of code must come AFTER the for statement ends)
    line1 += '\n'
    line2 += '\n'
    # if the answers should be shown, add in line4, and add a newline char to line3
    if show_ans == True:
        line3 += '\n'
        arranged_problems = line1 + line2 + line3 + line4
    else:
        arranged_problems = line1 + line2 + line3

    return arranged_problems
    
