# i do a work collecting all the phones,brands for the web owner
# you need just to run the test and you get all the phone you need 
from instruments.models import Phone, Phonebrand, Phonetype


def read():
    with open ("basedata.csv", 'r') as a:
        i = 0
     
        while True:
            if i == 152:
                print(1)
                break
  
            elif i <= 3:
                print(2)
                line = a.readline()
                line = line.split(",")
                p = Phonebrand(brand=line[0], logo=line[1])
                p.save()
                i = i+1
        
            elif i >= 4 and i <=24 :
                line = a.readline()
                line = line.split(",")
                kind = Phonebrand.objects.get(id = str(line[0]))
                p = Phonetype (type=line[1] ,image=line[2],brand= kind)
                p.save()
                print(i)
                i=i+1

            elif i >= 25 and i <= 151:
                print(i)
                line = a.readline()
                line = line.split(",")
                kind = Phonetype.objects.get(id = str(line[0]))
                p = Phone(type = kind, device = line[1])
                print(2)
                p.save()
                i=i+1       

        
read()



