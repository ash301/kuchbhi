#take the year as input

def function(year):
	leap = False

	if(year%4 == 0):
		if(year%100 == 0):
			if(year%400 == 0):
				leap = True

		else:
			leap = True

	

	return leap



year = int(input("Enter the Year : "))
print function(year)



#Documentation taken from url:
#https://support.microsoft.com/en-in/kb/214019

# To determine whether a year is a leap year, follow these steps:
# 1)If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# 2)If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# 3)If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# 4)The year is a leap year (it has 366 days).
# 5)The year is not a leap year (it has 365 days).
