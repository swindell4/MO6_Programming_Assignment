import datetime 

file = open("today.txt", "w") 
currentDate = datetime.datetime.now().date() 
currentDate = currentDate.strftime("%Y-%m-%d") 
file.write(currentDate) 