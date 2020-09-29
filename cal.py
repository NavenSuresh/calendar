#!/usr/bin/env python3

import datetime

FILENAME = "leaves.txt"

inp_year_str = ""
inp_month_str = ""
inp_str = inp_year_str + "_" + inp_month_str + "_"
count = 1
inp_year_int = 0
inp_month_int = 0
str1 = ""
res_day_str = ""
lis = []
new_lis = []
year_lis = []

#============================================================================
# PARSE THE LEAVES FILE AND STORE THE LEAVES IN A LIST
#============================================================================
def parse_leaves():
	f = open(FILENAME, "r")
	str1 = f.read()
	lis = str1.split("\n")
	while("" in lis):
		lis.remove("")
	for i in range(0, len(lis)):
		new_lis.append(lis[i][:4])
	[year_lis.append(x) for x in new_lis if x not in year_lis]
	

#============================================================================
# CHECK THE GIVEN YEAR IS IN LEAVES OR NOT
# RETURN 1 IF FOUND
# RETURN 0 IF NOT FOUND
#============================================================================
def check_year(year):
	if year in year_lis[:4]:
		return 1
	else:
		return 0


#============================================================================
# CHECK THE GIVEN MONTH IS CORRECT OR NOT
# RETURN 1 IF CORRECT
# RETURN 0 IF NOT CORRECT
#============================================================================
def check_month(month):
	if int(month) > 0 and int(month) < 13:
		return 1
	else:
		return 0
	

#============================================================================
# GET USER INPUT YEAR & MONTH
#============================================================================
def get_input():
	print("Enter the year:")
	inp_year_str = input()
	#print(inp_year_str)
	#print(type(inp_year_str))
	if check_year(inp_year_str):
		print("Enter the month:")
		inp_month_str = input()
		inp_year_int = int(inp_year_str)
		inp_month_int = int(inp_month_str)
		if check_month(inp_month_str):
			return 1
		else:
			print("Month is not valid!")
			return 0
	else:
		print("Year not found in the leaves!")
		return 0


#============================================================================
# PRINT THE SECOND WORKING DAY OF THE MONTH
#============================================================================
def second_working_day():
	print(inp_year_int)
	print(inp_month_int)
	print(count)
	a = datetime.datetime(inp_year_int, inp_month_int, count)
	res_day_str = a.strftime("%A")
	new_day = inp_str + str(count).zfill(2)
	if((res_day_str != "Saturday") and (res_day_str != "Sunday")):
		if new_day in lis:
			if flag == 2:
				print(new_day)
			else:
				flag += 1
		

#==============================================
# MAIN FUNCTION
#==============================================
def main():
    parse_leaves()
    if get_input():
    	second_working_day()
    else:
    	exit()


#========================================================
# STANDARD BOILERPLATE TO CALL THE MAIN() FUNCTION
#========================================================
if __name__ =='__main__':
    main()
