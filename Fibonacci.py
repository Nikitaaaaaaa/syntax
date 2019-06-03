#числа Фибоначчи мы может задать количество цифр, можем узнать сумму. 

#снизу включение библиотек
#сверху включение библиотек

#снизу константы
k=0
j=1
i=2
#сверху констаньы

#снизу функции
def enter ():
	global k
	print ('Введите количество числ Фибоначчи')
	k=int (input())
def fibonacci ():
	global j,i
	x=i+j
	j=i
	i=x
	print (x)
#сверху функции

#main
def main():
	enter ()
	print (j)
	print (i)
	y=3
	global k 

	while y<=k:
		fibonacci ()
		y+=1

main()
#main
