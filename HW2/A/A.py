def solution(arr):
    if len(arr) == 0: #проверили, что непустая
        return 0

    c = arr[0] #символ, с которого мы начинаем
    cur_seq = 0 #current sequence
    max_seq = 0

    for x in arr:
        if x == c:
            cur_seq += 1

        else:
            max_seq = max(max_seq, cur_seq)
            cur_seq = 1
            c = x
    max_seq = max(max_seq, cur_seq)

    return max_seq

if __name__ == "__main__":
    solution(input())

#Напишите функцию, принимающую массив arr и возвращающую значение максимального количества
#подряд идущих одинаковых элементов.
#Ваше решение должно быть написано одним циклом.