# This program was written by Effiea on November 19th 2020
# Last modified December 23rd 2020
# This program gets an input of a number and validates to confirm the type of card

from cs50 import get_int
import math

# Main Programs 
def main():
    ccn = get_int("Number: ")
    ccn_length = len(str(ccn))
    check_sum = checksum(ccn, ccn_length)
    get_cardtype(ccn, ccn_length, check_sum)

# Calculating the checksum to return sum to validate card type 
def checksum(ccn, ccn_length):
    sum = 0
    for i in range(ccn_length):
        if (ccn != 0):
            if (i % 2 == 0):
                sum += ccn % 10
            else:
                evendigit = 2 * (ccn % 10);
                sum += (evendigit // 10) + (evendigit % 10)
            ccn //= 10
        
    sum % 10 == 0
    return sum

# Determine the credit card type     
def get_cardtype(ccn, ccn_length, check_sum):
    # Check whether it is a the last digit of checksum is 0 and whether the length is that of a valid card
    if ((check_sum % 10 == 0) and (ccn_length == 15 or ccn_length == 16 or ccn_length == 13)):
        startdig = (ccn) // pow(10, ccn_length - 2) 
        visastartdig = (ccn) // pow(10, ccn_length - 1) 
        
        # Conditions to determine AMEX, MASTERCARD, VISA and INVALID
        if (ccn_length == 15 and (startdig == 34 or startdig == 37)):
            print("AMEX") 
        elif (ccn_length == 16 and (startdig >= 51 and startdig <= 55)):
            print("MASTERCARD")         
        elif (visastartdig == 4 and (ccn_length  == 16 or ccn_length  == 13)): 
            print("VISA")               
        else:
            print("INVALID")
    else:
        print("INVALID")
main()

