#A car dealership is developing a website in order to automatically estimate
#the value of the vehicle a user hands in. They buy SUVs, Sedans, and
#Sports-cars and want the code to allow for adjusting the car types if the
#dealership wants to add/remove a new car-type to the list of vehicles they buy.

#The dealership also buys motorcycles.

#The method in which they value each vehicle is:
#if the vehicle is a car, specifically an SUV, the vehicle is valued at $20k 
#and eligible for a 10% bonus if the car's model is after 2017.
#otherwise if the vehicle is another type of car, it is valued at $15k.
#if the vehicle is a bike, it is valued at $8k, and is eligible for a 20%
#bonus if it is a sport-bike whose model is 2020 or after.
#Finally,
#if the vehicle has more than 100k miles, it loses 20% of the original value
#if the vehicle is uninsured, it loses 10% of the original value
#if the vehicle has been in an accident, it loses 10% of the original value

cars=["SUV","Sedan","Sports-car"]
bikes=["Motorcycle", "Sport-bike"]
def find_vehicle(List): #This helps identify if the users' input is valid or not
    isfound=False
    for x in range(0,len(List)):
        if List[x]==vType:
            isfound=True
    if isfound:
        print("We have a few questions about your",vType,"before we determine its price")
    else:
        print("Sorry, your input is invalid.")
        exit()
def vDamages(price):
    value=1 #this is the ratio the initial price will be multiplied by in order to calculate final price
    accident=input('Has your vehicle been in an accident?(answer "yes" or "no"):\n')
    insurance=input('Is your vehicle insured?(answer "yes" or "no"):\n')
    miles=int(input("Enter your vehicle's mileage:\n"))
    if accident=="yes":
        value=value-0.1
    elif accident!="no":
        print("Sorry, your accident input is invalid.")
        exit()
    if insurance=="no":
        value=value-0.1
    elif insurance!="yes":
        print("Sorry, your insurance input is invalid.")
        exit()
    if miles>100000:
        value=value-0.2
    elif miles<0:
        print("Sorry, your mileage input is invalid.")
        exit()
    final=int(price*value)
    print("After reviewing your input, we have concluded that your",vType,"is valued at $",final,".\nPlease bring your vehicle to our dealership for us to perform a final review your vehicle.\nThank you for dealing with us!")

vehicle=input('Welcome, is your vehicle a car or a bike?(enter "car" or "bike"):\n')
if vehicle == "car":
    print(cars)
    vType=input("Above are the cars we buy, which is yours?:\n")
    find_vehicle(cars)
    if vType== "SUV":
        model=int(input("Enter the year of your SUV's model:\n"))
        if model>2017:
            price=20000*(1.1)
            vDamages(price)

        else:
            price=20000
            vDamages(price)

    else:
        price=15000
        vDamages(price)
elif vehicle == "bike":
    print(bikes)
    vType=input("Above are the bikes we buy, which is yours?:\n")
    find_vehicle(bikes)
    if vType=="Sport-bike":
        model=int(input("Enter the year of your sport-bike's model:\n"))
        if model>=2020:
            price=8000*(1.2)
            vDamages(price)

        else:
            price=8000
            vDamages(price)
    else:
        price=8000
        vDamages(price)

else:
    print("Sorry, your input is invalid.")
    exit()

    
