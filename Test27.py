print('Подсчет повторений элементов списка - от 0 до 5')
a = [1,4,0,3,4,2,5,1,0,3,2,4,5,2,0,5,4,1,3,4]
# создаем нулевой результирующий список из 5 элементов - по кол-ву
count = [0,0,0,0,0,0]
#count = [0]*6
for i in a:
    count[i] +=1
print('Результат')
print(count)
for i in range(6):
   print('Элемент ' + str(i) + ' втретился ' +str(count[i]) + ' раз')
#   print(str(i) + ' ' +str(count[i]))

print ('Отсортируем')
for i in range(6):
   print ((str(i) +' ' )*count[i], end = '')

print('Подсчет сколько раз встречается каждый символ в строке')   
my_s = 'abcz jndel HGY fhMkCed 45&129 ()?heo*'
letters = [0]*26  #в латинском алфавите 26 букв
diff = 97   # код а = 97, поэтому для подсчета от 0 смещение = 97
for i in my_s.lower():
   nomer = ord(i) - diff
   if i >='a' and i<='z':
#      print(i,nomer)
      letters[nomer]+=1
print('[' + my_s + ']')      
print(letters)      
for i in range(26):
   print('Символ [' + chr(i+diff) +'] = встречается ' + str(letters[i]) + ' раз' )

print('Пример 3, заполняем список случайным образом')
a =[]
import random
for i in range(20):
   a.append(random.randint(-10,10))
count = [0]*21 # диапазон элементов от -10 до 10
diff = 10 # смещение =10
for i in a:
   count[i+diff]+=1
ncount = len(count)   
print(a)
for i in range(ncount):
   if count[i] > 0:
      print(i-diff, count[i])




    