'''
https://www.101computing.net/school-trip-bus-quote/
The school teacher would like a computer program that will:

Ask for the number of students taking part in the trip.
Ask for the number of teachers taking part in the trip.
Calculate the total number of participants (by adding the number of students and the number of teachers).
Find out and output the number of large coaches that will be required.
Find out and output the number of small coaches that will be required.
Calculate and output the total cost of hiring these coaches for a day.'''

students=int(input("Number students"))
teachers=int(input("Number teachers"))
participants=students+teachers
print(f'number of participants are : {participants}')

largebus=participants//46
print(f'the no.of largebuses required are {largebus}')

l_reminder=participants%46
smallbus=l_reminder//16
s_reminder=l_reminder%16

if s_reminder>0:
    smallbus=smallbus+1

print(f'the no.of smallbuses are required are {smallbus}')
totalcost=largebus*360 + smallbus*140
print(f'the total cost of buses are : {totalcost} ')

