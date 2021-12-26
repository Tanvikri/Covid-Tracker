

for i in range (0, 100): 
    print (" ")
    
from covid import Covid

covid = Covid()
covid.get_data()

print ("Covid Tracker")

#Predefined functions and allocated variables to the predefined function yielded global results.

act = cv.get_total_active_cases ()  #Get Total Active cases

rec = cv.get_total_recovered ()  #Get Total Recovered cases

death = cv.get_total_deaths ()  #Get Total Deaths

con = cv.get_total_confirmed_cases ()  #Get Total Confirmed cases

print ("1. Global Count")   #Get all of the latest covid news from around the world.

print("2.Active Cases")  #Get the total number of active cases

print("3.Confirmed Cases")  #Get the total number of confirmed instances

print("4.Recovered Cases")  #Get the total number of cases that have been recovered.

print ("5.Deceased")  #Get Total Deaths

print("6.Get Covid Updates By Country Name")

choice = input ("Enter a number of your choice :")

#if-elif-else statements used

if choice == '1':
    print("Active Cases ", act, "\nConfirmed Casos: ", con, "\nRecovered Cases :", rec, "\nDeceased :", death)

elif choice == '2':
    print("Active Cases :",act)

elif choice == '3':
    print ("Confirmed Cases :", con)

elif choice =='4':
    print ("Recovered Cases :", rec)

elif choice == '5':
    print ("Deceased :", death)

elif choice == '6':
    str = i = input ("Enter Country Name:")#Get the Status of Covid19 in a particular country
    cname = covid.get_status_by_country_name (i)
    print (cname)
                   
else :
    print("Invalid Option")
