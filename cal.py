#!/usr/bin/env python3

#============================================================================
# PROGRAM TO FIND THE SECOND WORKING DAY OF THE MONTH
# NOTE : UPDATE THE LEAVES OF THE YEAR IN THE TEXT FILE
# AUTHOR : NAVEN SURESH
#============================================================================

import datetime

FILENAME = "leaves.txt"

inp_year_str = ""
inp_month_str = ""
inp_str = inp_year_str + "_" + inp_month_str + "_"
inp_year_int = 0
inp_month_int = 0
str1 = ""
res_day_str = ""
lis = []
new_lis = []
year_lis = []

#============================================================================
# PARSE THE LEAVES FILE AND STORE THE LEAVES IN A LIST
# ARGS - NO ARGUMENTS
# AND RETURNS THE LIS (LIST)
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
	return lis
	

#============================================================================
# CHECK THE GIVEN YEAR IS IN LEAVES OR NOT
# ARGS - YEAR (STRING)
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
# ARGS - MONTH (STRING)
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
# ARGS - NO ARGUMENTS
# RETURN THE INPUT STRING IF THE YEAR AND MONTH ARE VALID
# RETURN 0 IF THE YEAR IS NOT FOUND IN LEAVES TEXT FILE OR MONTH IS INVALID
#============================================================================
def get_input():
	print("Enter the year:")
	inp_year_str = input()
	global inp_year_int 
	inp_year_int = int(inp_year_str)
	#print(inp_year_str)
	#print(type(inp_year_str))
	if check_year(inp_year_str):
		print("Enter the month:")
		inp_month_str = input()
		global inp_month_int
		inp_month_int = int(inp_month_str)
		if check_month(inp_month_str):
			inp_month_str = inp_month_str.zfill(2)
			return inp_year_str + "_" + inp_month_str + "_"
		else:
			print("Month is not valid!")
			return 0
	else:
		print("Year not found in the leaves!")
		return 0


#============================================================================
# PRINT THE SECOND WORKING DAY OF THE MONTH
# ARGS - LIS (LIST) & INP_STR1 (STRING)
# PRINTS THE DATE IF THE SECOND WORKING DAY IS FOUND
# RETURN - NOTHING
#============================================================================
def second_working_day(lis, inp_str1):
	count = 1
	flag = 0
	print(inp_year_int)
	print(inp_month_int)
	print(count)
	for count in range(1, 31):
		a = datetime.datetime(inp_year_int, inp_month_int, count)
		res_day_str = a.strftime("%A")
		new_day = inp_str1 + str(count).zfill(2)
		if((res_day_str != "Saturday") and (res_day_str != "Sunday")):
			if new_day not in lis:
				flag += 1
				if flag == 2:
					print(new_day)
					break
		count += 1 
	

#==============================================
# MAIN FUNCTION
# ARGS - NO ARGUMENTS
# RETURN - NOTHING
#==============================================
def main():
    lis = parse_leaves()  
    inp_str = get_input()
    if inp_str != 0:
    	second_working_day(lis, inp_str)
    else:
    	exit()


#========================================================
# STANDARD BOILERPLATE TO CALL THE MAIN() FUNCTION
#========================================================
if __name__ =='__main__':
    main()
