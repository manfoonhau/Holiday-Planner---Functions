#intro
print (
"""                                     Welcome To Your Holiday Planner! 
We Plan Everything From Your Flight, 5* Hotel(prices differ from cities), Car Rental and Total Cost For Your Holiday!
                            You'll Have Four Great Destinations For You To Choose From! 
                
London  - £200   5* Hotel - £120(ppn)
Tokyo   - £550   5* Hotel - £80(ppn)
Italy   - £300   5* Hotel - £95(ppn)
Eygpt   - £350   5* Hotel - £70(ppn)

Car Rentals For All Destinations - £20(ppn)

ppn - price per night
""")
#saves a function, when ever its called upon uses the data inside of it.     
def hotel_cost (num_nights):  
    #variables for hotel costs
    hotel_london = 120
    hotel_tokyo = 80
    hotel_italy = 95
    hotel_eygpt = 70   
    #calculates hotel costs per night depending on which city was inputted.
    if city_flight == "london":
        return num_nights * hotel_london
    
    elif city_flight == "tokyo":
        return num_nights * hotel_tokyo
    
    elif city_flight == "italy":
        return num_nights * hotel_italy
    
    elif city_flight == "eygpt":
        return num_nights * hotel_eygpt
    else:
        return "Error, A City On Our List Was No Selected."
    
#saves a function, when ever its called upon uses the data inside of it.  
def plane_cost (city_flight): 
    #variables for city costs
    plane_london = 200
    plane_tokyo = 550
    plane_italy = 300
    plane_eygpt = 350
    
    #calculates flight price depending on which city
    if city_flight == "london":
        return plane_london
    elif city_flight == "tokyo":
        return plane_tokyo
    elif city_flight == "italy":
        return plane_italy
    elif city_flight == "eygpt":
        return plane_eygpt
    else:
        return "Error, A City On Our List Was No Selected."
          
#saves a function, when ever its called upon uses the data inside of it.      
def car_rental (rental_days):
    #variable for car rental per day
    car = 20
    #calculates car rental price depending on how many days its been rented by
    return car * rental_days

#saves a function, when ever its called upon uses the data inside of it.  
def holiday_cost (city_flight, num_nights, rental_days):
    #calculates total price for the holiday.
    total = hotel_cost (num_nights) + plane_cost (city_flight) + car_rental (rental_days)
    
    return total
    
#variable of cities we can choose from
city = ("london", "tokyo", "italy", "eygpt")
#asks user to input thier chose of destination, if a city inputted is not in our list output an error.
while True:
    city_flight = input("Which Holiday Destination Are You Interested In? ").lower()
    if city_flight in city:
        break
    else:
        print ("Error, A City On Our List Was No Selected.")
 
#asks user to input the number of nights they'll like to stay, if a negative number is inputted output an error.  
while True:
    num_nights = int(input("How Many Nights Will You Like To Stay For? "))
    if num_nights >= 0:
        break
    else:
        print ("Error, A Negative Number Cannot Be Inputted")

#asks user to input the number of days they'll like to rent a car for, if a negative number is inputted output an error. 
while True:
    rental_days = int(input("How Many Days Will You Be Hiring A Rental Car For? "))
    if rental_days >= 0:
        break
    else:
        print ("Error, A Negative Number Cannot Be Inputted")

#variable to change city inputted into uppercase.
upper_city_flight = city_flight.upper()

#prints out the users holiday details:
print (" ")
print ("____________________________________")
print ("\tHoliday Details:\n")
print (f"City:\t\t {upper_city_flight}")
print(f"Hotel Cost:\t £{hotel_cost (num_nights)} For {num_nights} Nights")
print (f"Flight Cost:\t £{plane_cost (city_flight)}")
print (f"Car Rental Cost: £{car_rental (rental_days)} For {rental_days} Days")
print(f"Total Cost:\t £{holiday_cost (city_flight, num_nights, rental_days)}")
print ("____________________________________")