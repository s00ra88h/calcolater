#input we need form user
#total rent
#total food order
#electicity  units speed
#charge per units

#personliving in room/flat

##output
#total amountyou've to pay

rent= int(input("enter your hostel/flat rent="))
food = int(input("enter the amount of food ordered ="))
electicity_speed = int(input("Enter the total of electircity speed ="))
charger_per_unit=int(input("Enter thechargper unit ="))
person+int(input("Enter the number of persons living in room/flat = "))


total_bill= electicity_speed*charger_per_unit

output = (food +rent + total_bill)// persons

print("Each person will pay =",output)
