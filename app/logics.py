import math


def solution(string):
    equation = ''
    for i in range(len(string)):
        if string[i].isdigit() or string[i] in '.+-()*':
            equation += string[i]
        elif string[i] == '%':
            equation += '*0.01'
        elif string[i:i+2] == 'ln':
            equation += 'math.log1p'
        elif string[i] == '^':
            equation += '**'
        elif string[i] == '!':
            for k in range(len(equation)-2, 0, -1):
                if not equation[k].isdigit():
                    equation = equation[:k] + 'math.factorial(' + equation[k:-2] + ')'
        elif string[i] == u'\u03C0':
            equation += 'math.pi'
        elif string[i] == u'\u2236':
            equation += '/'
        elif string[i] == u'\u2217':
            equation += '*'
        elif string[i] == u'\u221a':
            equation += 'math.sqrt'
    # try:
    #     result = eval(equation)
    # except SyntaxError:
    #     result = 'Ошибка ввода'
    return equation, string


print(solution(''))

