from csv import reader,DictReader
from StuData import info 
import csv

data = [] #Creates a list for courses
course = [] #Creates list for section
present = [] #number of present students
MyDict = {} # Will hold the dictionary for (course, teacher, number present)
total = []
percent =[]
FileName = input("Enter File Name: ") # Read user input
print("Data is read as so : \nSection Name: ['Teacher Name' , 'Total Present For Week', 'Total Students For Week', 'Attendance Percentage For Week']\n")
with open(FileName,'r') as read_ojb:
    dict_reader = DictReader(read_ojb)
    list_of_dict = list(dict_reader) #Created list form the DictReader
    for key in list_of_dict: #Reads in the key for each list
        MyDict[key['Section Name']] = key['Teacher Name'] #Creates dictionary with course and teacher
        if key['Section Name'] not in course: #adds each course into a list   
            course.append(key['Section Name'])
            data.append(key['Course Name'])

    for x in range(len(course)): #Will grab students present in a class
        i = 0 #Keep track of present
        j = 0 #Keep track of total
        for key in list_of_dict:
            if course[x] == key['Section Name'] and key['Attendance'] == 'present': #Checks if course of x is equal to course in excel, then checks if attendenace is present
                i+=1 #increment if present
                j+=1 #increment for total
            elif course[x] == key['Section Name'] and key['Attendance'] == 'absent':
                j+=1 #Total students for week
            elif course[x] == key['Section Name'] and key['Attendance'] == 'late':
                j+=1 #Total students for week
                i+=1 #increment if present
            elif course[x] == key['Section Name'] and key['Attendance'] == 'unmarked':
                j+=1 #Total students for week
        total.append(j) #Keeps track of total
        present.append(i) #total number of users present for the week

for x in range(len(present)):
    percent.append((present[x]/total[x]))
#Note each number is represented as "Number Present","Total","Attendance percent"
i = 0#Used to keep count of looping
for key in MyDict:
    MyDict[key] = [data[i],key,MyDict[key],present[i],total[i],"{:.2%}".format(percent[i])] #Changing dictionary
    i+=1
    #print ("{}: {}".format(key,MyDict[key])) #Printing out the dictionary
  
with open('Output.csv','w') as output: #Opens output file
    output_data = csv.writer(output, delimiter=',')
    output_data.writerow(['Course','Section','Teacher Name', 'Total Present For Week', 'Total Students For Week', 'Attendance Percentage For Week'])
    for key in MyDict:
        output_data.writerow(MyDict[key])
        


    


