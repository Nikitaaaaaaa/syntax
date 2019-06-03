#алгебрическая прогресия 

#снизу включение библиотек
#сверху включение библиотек

#снизу константы
first_number = 0
last_number = 0
increase = 0 
procces =0
#сверху констаньы

#снизу функции
def enter():
	global first_number,last_number,increase,procces
	print ('Введите первое число: ')
	first_number = int(input())
	procces = first_number 
	print ('Введите последние число:')
	last_number = int(input())
	print ('Введите увеличение:')
	increase = int(input())
def alpro():
	global first_number,last_number,increase,procces
	procces +=increase
	print (procces)
#сверху функции

#main
def main():
	global last_number,procces
	enter()
	while procces<last_number:
		alpro()
main()
#main
