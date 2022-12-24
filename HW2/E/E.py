def solution(a, b):
    return a + 1 if b == 1 else solution(a, b - 1) + 1
