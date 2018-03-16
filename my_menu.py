#this is the sides menu
def sides():
  side_input = input("What sides would you like? We have extra fries or wings? ").upper()
  if side_input == "fries".upper():
    sizes = input("would you like small, medium, large? ").upper()
      
    if sizes == "small".upper():
      print("This will cost $4.39")
        
    elif sizes == "medium".upper():
      print("This will cost $5.39")
          
    elif sizes == "large".upper():
      print("This will cost $6.39")
        
  elif side_input == "wings".upper():
    sizes = input("Would you like 6 wings, 8 wings, or 12 wings? ").upper()
      
    if sizes == "6".upper():
      print("This will cost $6.50")
      print("Would you like teriyaki, BBQ, buffalo, or garlic? ")
          
    elif sizes == "8".upper():
      print("This will cost $7.80")
      print("Would you like teriyaki, BBQ, buffalo, or garlic? ")
          
    elif sizes == "12".upper():
      print("This will cost $10.90")
      print("Would you like teriyaki, BBQ, buffalo, or garlic? ")




#this is the breakfast menu
def breakfast_menu():
  morning_menu = ["Bacon and Eggs Sandwich", "Hash Browns"]
  print(morning_menu)
  answer = input("What meal would you like to order?").upper()
 
  if answer == "Bacon and Eggs Sandwich".upper():
    print("This sandwich will come with bacon, eggs, cheese, and mayo")
    print("This will cost $6.87")
    sides()
    
  elif answer == "Hash Browns".upper():
    print("Hash browns will come with .25 lbs of hash browns")
    print("This will cost $2.75")
    sides()
        

#this is the lunch menu  
def lunch_menu():
  lunch_menu = ["Ham burger", "Cheese burger", "Bacon Burger", "Bacon Cheese Burger", "BBQ Burger", "Guacamole Burger", "Double Burger", "Double Cheese Burger", "Chicken Burger", "Swiss Mushroom Burger"]
  print(lunch_menu)
  print("All burgers come with lettuce and tomatos")
  answer = input("What meal would you like to order?").upper()
  
  if answer == "Ham Burger".upper():
    print("Will come with ketchup, mustard, and pickles")
    print("This will cost $7.89")
    sides()
    
  elif answer == "Cheese Burger".upper():
    print("Will come with american cheese, ketchup, mustard, and pickles")
    print("This will cost $7.99")
    sides()
    
  elif answer == "Bacon Burger".upper():
    print("Will come with bacon, ketchup, mustard, and pickles")
    print("This will cost $8.89")
    sides()
    
  elif answer == "Bacon Cheese Burger".upper():
    print("Will come with bacon, cheese, ketchup, mustard, and pickles")
    print("This will cost $7.99")
    sides()
    
  elif answer == "BBQ Burger".upper():
    print("This will come with BBQ sauce, diced onions, bacon, pickles, american cheese.")
    print("This will cost $9.99")
    sides()
    
  elif answer == "Guacamole Burger".upper():
    print("This will come with guacamole, bacon, pickles, onions.")
    print("This will cost $10.30")
    sides()
    
  elif answer == "Double Burger".upper():
    print("Will come with ketchup, mustard, and pickles")
    print("This will cost $7.89")
    sides()
    
  elif answer == "Double Cheese Burger".upper():
    print("Will come with cheese, ketchup, mustard, and pickles")
    print("This will cost $10.89")
    sides()
    
  elif answer == "Chicken Burger".upper():
    print("Will come with mustard, pickles, chedder cheese")
    print("This will cost $11.79")
    sides()
    
  elif answer == "Swiss Mushroom Burger".upper():
    print("Will come with swiss cheese, mustard")
    print("This will cost $7.49")
    sides()
        
        
#this is the dinne menu    
def dinner_menu():
  dinner_menu = ["Ham burger", "Cheese burger", "Bacon Burger", "Bacon Cheese Burger", "BBQ Burger", "Guacamole Burger", "Double Burger", "Double Cheese Burger", "Chicken Burger", "Swiss Mushroom Burger", "Stake", "Lasagna"]
  print(dinner_menu)
  print("All burgers come with lettuce and tomatos")
  answer = input("What meal would you like to order?").upper()
  
  if answer == "Ham Burger".upper():
    print("Will come with ketchup, mustard, and pickles")
    print("This will cost $8.89")
    sides()
    
  elif answer == "Cheese Burger".upper():
    print("Will come with american cheese, ketchup, mustard, and pickles")
    print("This will cost $8.99")
    sides()
    
  elif answer == "Bacon Burger".upper():
    print("Will come with bacon, ketchup, mustard, and pickles")
    print("This will cost $9.89")
    sides()
    
  elif answer == "Bacon Cheese Burger".upper():
    print("Will come with bacon, cheese, ketchup, mustard, and pickles")
    print("This will cost $9.99")
    sides()
    
  elif answer == "BBQ Burger".upper():
    print("This will come with BBQ sauce, diced onions, bacon, pickles, american cheese.")
    print("This will cost $10.99")
    sides()
    
  elif answer == "Guacamole Burger".upper():
    print("This will come with guacamole, bacon, pickles, onions.")
    print("This will cost $11.30")
    sides()
    
  elif answer == "Double Burger".upper():
    print("Will come with ketchup, mustard, and pickles")
    print("This will cost $8.89")
    sides()

  elif answer == "Double Cheese Burger".upper():
    print("Will come with cheese, ketchup, mustard, and pickles")
    print("This will cost $11.89")
    sides()
    
  elif answer == "Chicken Burger".upper():
    print("Will come with mustard, pickles, chedder cheese")
    print("This will cost $12.79")
    sides()
    
  elif answer == "Swiss Mushroom Burger".upper():
    print("Will come with swiss cheese, mustard")
    print("This will cost $8.49")
    sides()
        
  elif answer == "Lasagna".upper():
    print("This will cost $12.37")
    sides()
        
  elif answer == "Stake".upper():
    print("This will cost $15.79")
    print("All stakes are cooked medium rare.")
    sides()
        
  
print("Waitress = 'I suggest the Guacamole burger on the lunch menu")
Time_of_day = input("Would you like Breakfast, Lunch, Or Dinner?").upper()

if Time_of_day == "Breakfast".upper():
  print(breakfast_menu())
  
elif Time_of_day == "Lunch".upper():
  print(lunch_menu())
  
elif Time_of_day == "Dinner".upper():
  print(dinner_menu())