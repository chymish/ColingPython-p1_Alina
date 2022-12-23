def solution(n):
    result = []
    counter = 1
    while counter <= n:
        result.insert(len(result), counter)
        counter *= 2
    return result

#По данному числу N распечатайте все целые степени двойки, не превосходящие N, в порядке возрастания.