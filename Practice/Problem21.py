# Enough Fuel Consumption

def check_fuel_distance(fuel, distance):
   required =fuel*distance
   if required>50:
       print("Enough")
   else:
       print("Go On")
check_fuel_distance(2,10)