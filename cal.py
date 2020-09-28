#!/usr/bin/env python3

import sys
import os
import glob
import calendar
import datetime

f = open("leaves.txt", "r")

str1 = f.read()

lis = str1.split("\n")

while("" in lis):
    lis.remove("")

in_year = "2020"
in_month = "05"
inp = in_year + "_" + in_month + "_"

int_year = int(in_year)
int_month = int(in_month)

count = 4
a = datetime.datetime(int_year, int_month, count)
res = a.strftime("%A")
print(res)
print(type(res))

new_date = inp + str(count).zfill(2)

if ((res != "Saturday") and (res != "Sunday")):
	if new_date in lis:
		print("yes")
	else:
		print("no")
else:
	print("Weekend! :)")
