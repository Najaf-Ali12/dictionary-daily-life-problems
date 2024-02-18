#2. Grade Calculator:
# Create a program that asks the user for their scores in different subjects
#and calculates their overall grade based on a grading scale stored in a dictionary.
grade={
    90:"A",
    80:"B",
    70:"C",
    60:"D",
    50:"E",
    40:"FAIL"

}
n=int(input("enter how many subjects do you have"))
count=0
for i in range(n):
    sub=int(input(f"enter the marks in subject{i+1} from 100"))
    count+=sub
average=count/n   
print(average)
if average in grade.keys():
    print("your grade is ",grade[average])




