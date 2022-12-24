def solution(arr):
    c = arr[0] #символ, с которого мы начинаем
    cur_seq = 0 #current sequence
    result = 0

    for i in arr:
        if i == c:
            cur_seq += 1
        else:
            result = max(result, cur_seq)
            cur_seq = 1
            c = i
    result = max(result, cur_seq)

    return result
