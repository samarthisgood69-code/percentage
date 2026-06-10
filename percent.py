#take marks as input from the users
print("enter the marks obtained in 4 subjects: ")
math = int(input("math :"))
english = int(input("english :"))
social = int(input("social :"))
science = int(input("science :"))
#let's calculate the percentage of marks
sum = math+english+social+science
print("sum of math,english,social and science = ", sum)
perc = (sum/400)*100
print(end = "percentage mark = ")
print(perc)