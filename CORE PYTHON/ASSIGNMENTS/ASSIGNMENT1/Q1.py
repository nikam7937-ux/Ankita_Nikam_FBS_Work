#Program to calculate the percentage of student based on marks 
s1=int(input("Enter the mark of subject 1 : "))
s2=int(input("Enter the mark of subject 2 : "))
s3=int(input("Enter the mark of subject 3 : "))
s4=int(input("Enter the mark of subject 4 : "))
s5=int(input("Enter the mark of subject 5 : "))

total_marks= s1 + s2 + s3 + s4 + s5

percentage= (total_marks/500)*100

print("Percentage is =",percentage,"%")
