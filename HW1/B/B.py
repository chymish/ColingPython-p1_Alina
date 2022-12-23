def solution(n):
    if n == 0:
        return ''
    else:
        line_1 = '   _~_   '
        line_2 = '  (o o)  '
        line_3 = ' /  V  \\ '
        line_4 = '/(  _  )\\'
        line_5 = '  ^^ ^^  '
        result = line_1*n + '\n'
        result += line_2*n + '\n'
        result += line_3*n + '\n'
        result += line_4*n + '\n'
        result += line_5*n
        return result
