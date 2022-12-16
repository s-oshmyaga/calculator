import math


def to_factorial(equation):
    if equation.isdigit():
        equation = 'math.factorial(' + equation + ')'
    else:
        for sign in range(len(equation) - 2, -1, -1):
            if not equation[sign].isdigit():
                equation = equation[:sign + 1] + 'math.factorial(' + equation[sign + 1:] + ')'
    return equation


def solution(string):
    equation = ''
    for i in range(len(string)):
        if string[i].isdigit() or string[i] in '.+-()*':
            equation += string[i]
        elif string[i:i+2] == 'ln':
            equation += 'math.log1p'
        elif string[i] == '^':
            equation += '**'
        elif string[i] == '!':
            equation = to_factorial(equation)
        elif string[i] == u'\u03C0':
            equation += 'math.pi'
        elif string[i] == u'\u2236':
            equation += '/'
        elif string[i] == u'\u2217':
            equation += '*'
        elif string[i] == u'\u221a':
            equation += 'math.sqrt'
    try:
        result = eval(equation)
    except SyntaxError:
        result = 'Ошибка ввода'
    except TypeError:
        result = 'Вы ввели недопустимое значение'
    return result



