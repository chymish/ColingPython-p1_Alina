def solution(total_n):
    total_n = total_n % 1440 #отстаток от деление на число минут в сутках
    hours = total_n // 60
    minutes = total_n % 60
    return hours.__str__() + ' ' + minutes.__str__()
