# -*- coding: utf-8 -*-
# (Date of Easter after 1582.) Let Y be the year
# for which the date of Easter is desired.

#Written by Joe Kruger

print("Find the date of Easter for a range of years after 1582.")


year1,year2="abc","abc"  # year has replaced Y and "abc" is dummy starting value
count = 0   # count attempts are data entry

# force entry of a 4-digit year>1582
while ((not year1.isdigit()) or (len(year1)!=4) or (year1<="1582")):
  year1=input("Enter the first year: ")

  # error message to user
  if not year1.isdigit():
    print("Digits, please.")
  elif len(year1)!=4:
    print("Four digits, please.")
  elif year1<="1582":
    print("After 1582, please.")
    
  count=count+1
  if (count>3)and((not year1.isdigit()) or (len(year1)!=4) or (year1<="1582")):
    print("You are a moron ... Just sayin'")

while ((not year2.isdigit()) or (len(year2)!=4) or (year2<="1582")):
  year2=input("Enter the last year: ")

  # error message to user
  if not year2.isdigit():
    print("Digits, please.")
  elif len(year2)!=4:
    print("Four digits, please.")
  elif year2<="1582":
    print("After 1582, please.")
    
  count=count+1
  if (count>3)and((not year2.isdigit()) or (len(year2)!=4) or (year2<="1582")):
    print("You are a moron ... Just sayin'")

  # once a valid year has been entered

year1=int(year1)
year2=int(year2)
  
  # Golden Number. Set G = ( Y mod 19) + 1.
  #( G is the “golden number” of the year in the 19-year Metonic cycle.)
year = year1
while year<=year2:
  goldenNumber= (year%19)+1 # goldenNumber has replaced G

  # Century. Set C = [ Y ÷ 100] + 1. (When Y is not a multiple of 100,
  # C is the century number; i.e., 1984 is in the twentieth century.)
  century=(year/100)+1 # century has replaced C

  # Corrections. Set X = [3 C ÷ 4] − 12, Z = [(8 C +5) ÷ 25] − 5.
  #( X is the number of years, such as 1900, in which leap year was dropped
  # in order to keep in step with the sun. Z is a special correction
  # designed to synchronize Easter with the moon's orbit.)
  dropLeapsCorrection = (3*century/4)-12 # dropLeapsCorrection has replaced X
  moonCorrection=(8*century+5)/25-5 # moonCorrection has replaced Z

  # Find Sunday. Set D = [5 Y ÷ 4] − X − 10.#
  # (March ((− D ) mod 7) actually will be a Sunday.)
  sunday = 5*year/4 - dropLeapsCorrection - 10 # sunday has replaced D


  # Epact. Set E = (11 G + 20 + Z − X ) mod 30.
  # If E = 25 and the golden number G is greater than 11,
  # or if E = 24, then increase E by 1.
  # ( E is the “epact,” which specifies when the full moon occurs.)
  epact = (11*goldenNumber + 20 + moonCorrection - dropLeapsCorrection)%30
  if (epact==25 and goldenNumber>11) or epact==24: # epact has replaced E
    epact += 1

  # Find full moon. Set N = 44 − E . If N < 21 then set N = N + 30.
  #(Easter is supposedly the “first Sunday following the first full
  # moon which occurs on or after March 21.”
  # Actually perturbations in the moon's orbit do not make this strictly
  # true, but we are concerned here with the “calendar moon” rather than
  # the actual moon. The N th of March is a calendar full moon.
  date = 44 - epact # date has replaced N
  if date<21:
    date += 30

  # Advance to Sunday. Set N = N + 7 − (( D + N ) mod 7).
  date += 7 - ((sunday+date)%7)

  # Get month. If N > 31, the date is ( N − 31) April;
  # otherwise the date is N March.
  if date>31:
    date -= 31
    print("%d: April %d" % (year, date))
  else: print("%d: March %d" % (year, date))
  year += 1
