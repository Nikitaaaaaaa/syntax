#Выводит число на каждый итерации (цикл) увеличивается количество символов на 1.

#снизу включение библиотек
import random, time, os
#сверху включение библиотек

#снизу константы
k=0
x=0
start=0
lvl=start
#сверху констаньы

#снизу функции
def generation ():
	global k, lvl 
	k = int (random.randint (1*10**lvl,9*10**lvl))
	print (k)
	time.sleep (2)
	os.system('cls')
def inputt ():
	global x
	x = int(input())
def comparison ():
	global k, x, lvl, start
	if k==x:
		print ('True')
		lvl +=1
	else: 
		print ('False')
		lvl=start
#сверху функции

#main
def main():
	while True: 
		generation ()
		inputt ()
		comparison ()
		time.sleep (1)
		os.system('cls')
		
main()
#main
