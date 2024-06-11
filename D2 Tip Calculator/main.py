print("Welcome to the tip calculator!")
bill=round(float(input("How much was your bill? ")),2)
tip=round(float(input("What percentage tip would you like to give? ")),2)/100+1
people=round(float(input("How many people are splitting the bill? ")),2)
pay=round(bill*tip/people,2)
print(f"You pay ${pay}")
