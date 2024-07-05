def readtxt(): 
   file = open("today.txt", "r") 
   today_string = file.read() 
   return today_string 
readtxt() 