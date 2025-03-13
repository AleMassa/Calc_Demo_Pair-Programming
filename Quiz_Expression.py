import random as rand
import time	
from sys import exit

N = 10

def Menu():
	r = input("If you want to continue the test press every button, if you want to QUIT press \'q\':\t")
	if(r.lower() == "q"):
		exit()
	return r

def Statistics(w_ans,time,num_err):
	print("\nTotal Time\t\t",round(time, 2),"seconds\nCorrect Answers:\t", str(N-num_err) + "/"+ str(N))
	if num_err>0:
		print("\nAnswers reviewed:\n")
		for i in w_ans:
			print(i)

def Number_Generator():
	num = rand.randint(0, 100)
	return num

def Operation_Generator():
	operation = {
			1: "+",
			2: "-",
			3: "*",
			4: "/"
		}
	choice = rand.randint(1,4)
	return operation[choice]

def Channel_Operation_Gen():
	n_operation = rand.randint(3,5)
	nums = [Number_Generator() for i in range(1,n_operation+1)]
	operations = [Operation_Generator() for i in range(1,n_operation)]
	string = ""
	count = 0
	for num,op in zip(nums,operations):
		count +=1
		string += str(num) + " "
		string += op + " "	
	string += str(nums[count])
	return string

def start(): 
	menu = ""
	
	while menu != "q":
		answers = []
		count_err = 0
		start_t = time.time()

		for i in range(N):
			channel = Channel_Operation_Gen()
			flag = True
			while flag:
				try:
					res = float(eval(channel))
					flag = False
				except Exception as e:
					#exception due to 0 error
					channel = Channel_Operation_Gen()

			fAns = str(channel +" = ")
			tol = 1.0e-1
			try:
				user_ans = float(input(fAns))
				if (abs(user_ans - res)>tol):
					#Wrong Answer
					answers.append(fAns + str(round(res,2))+"\n")
					count_err +=1
			except Exception as e:
				#non-numerical answer inserted by the user
				answers.append(fAns + str(round(res,2))+"\n")
				count_err +=1

		end_t = time.time()
		Statistics(answers,end_t-start_t,count_err)
		menu = Menu()
		
start()
