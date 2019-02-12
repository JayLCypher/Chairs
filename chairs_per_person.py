import os, sys

f = open(os.path.join(sys.path[0],'reservations.csv'), 'r')

for reservation in f:
    name, number = reservation.split(",")

    try:
        chairs_per_person = 50 / int(number)

    except ValueError:
        print("{} won't get squat because {} is not an integer number".format(name, number.rstrip("\r,\n")),"\n")
    
    except ZeroDivisionError:
        print("Don't divide by zero you dimwit","\n")

    else:
        print("{} will get {} chairs per person".format(name, chairs_per_person),"\n")

print("End of file reached. Closing file...")
f.close()
