def solution(x):
#    result = ''
#    h_first = x.find('h')
#    h_last = x.rfind('h')
#    for i in range(len(x)):
#        if i % 3 == 0 and i != 0:
#            result = ''.join([x[i] for i in range(len(x))])
#            i += 1
#            continue
#        elif x[i] == '1':
#            result.replace('1', 'one')
#        elif x[i] == 'h':
#            result = x[h_first + 1:h_last].replace('h', 'H') + x[h_last:]
#        else:
#            result += x[i]
#        i += 1
#
#    return result

##Напишите функцию, принимающую строку x и возвращает строку после некоторых трансформаций:
##1) Из строки удалены все символы с индексом кратным 3
##2) Все символы 'h' заменены на 'H', кроме первого и последнего вхождения
##3) Все символы '1' заменены на 'one'


##Пример:

##>>> '1+1=2'
##>>> solution(x)
##'one+one2'

##>>> solution('In the hole in the ground there lived 1 hobbit')
##>>> solution(x)
##'In heHoe n Hegrun ter lve onehobi'