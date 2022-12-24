def solution(a, b):
    i, j = 0, 0
    result = []
    while i < len(a) or j < len(b):
        if i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            elif b[j] == a[i]:
                j += 1
            else:
                result.append(b[j])
                j += 1
        elif i < len(a):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    return result
