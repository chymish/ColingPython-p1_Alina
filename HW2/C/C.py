def solution(arr):
    a = []
    while arr:
        a.extend(list(arr.pop(0)))
        arr = list(zip(*arr))
        arr.reverse()
    return a