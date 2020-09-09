from csv import reader, DictReader
import csv

filename1 = input("The oldest file: ") #Read oldest attendance report
filename2 = input("The newest file: ") #Read newest attendance report


MyDict = {}
with open(filename1,'r') as read_obj, open(filename2,'r') as read_obj2:
    dict_reader = csv.reader(read_obj)
    dict_reader2 = csv.reader(read_obj2)#To be able to read
    listOfDict = list(dict_reader) #creates list form the dicreader of file 1
    listOfDict2 = list(dict_reader2) #creates list form the dicreader of file 2
    for key in listOfDict:
        for key2 in listOfDict2:
            if key[0] == key2[0] and key[1] == key2[1] and key[0]!= 'Course':
                key2[6] = (float(key2[5].strip('%')) - float(key[5].strip('%')))/100 #Sees the attendance change
                key2[6] = "{:%}".format(key2[6]) #adds the percent
                with open('Output2.csv','w') as outfile: #opens the outfile ro write in
                    outfile = csv.writer(outfile, delimiter=',',lineterminator='\r')
                    for key in listOfDict2: 
                        if key[6] == ' ':
                            key[6] = "No Data"
                        outfile.writerow(key)#writes to the file








    