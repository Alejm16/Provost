from csv import reader,DictReader
from StuData import info 

data = [] #Creates a list
course = [] #Creates list for courses
teacher = [] #Creates list for teachers
present = [] #number of present students
#i = 0 #will keep track of people present
num = 0 # will check how many total attended class

with open('Attendence_example.csv','r') as read_ojb:
    dict_reader = DictReader(read_ojb)
    list_of_dict = list(dict_reader)
    for key in list_of_dict:
        if key['Course Name'] not in course: #adds each course into a list 
            course.append(key['Course Name'])
        if key['Teacher Name'] not in teacher:#adds teachers to a list
            teacher.append(key['Teacher Name'])
    for x in range(len(course)):
        i = 0
        for key in list_of_dict:
            if course[x] == key['Course Name'] and key['Attendance'] == 'present':
                i+=1
        present.append(i)



        


#Printing purposes
for x in range(len(course)):
    print(course[x])
for x in range(len(teacher)):
    print(teacher[x])
for x in range(len(present)):
    print(present[x])


  #      data.append(info(key['Course Name'],num, key['Teacher Name'])) #adds data to a list to go through
        #print(key['Course Name'],key['Teacher Name'],key['Student Name'],key['Attendance'])

#for x in range(len(data)): #prints out the 
 #   print(data[x].name,' | ',data[x].course,' | ',data[x].teacher,' | ',data[x].status)
    


