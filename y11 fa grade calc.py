# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 13:21:56 2023
Modified on Wed Dec 27 12:31:37 2023

@author: kkarimov
@helper: drsp3ed
"""

a = []
while len(a) < 6 or len(a) > 6:
    try:
        a=list(map(float, input("Input your grades in the order shown below. \nUse space, do not use any comma: CPA2 CPA3 CPA4 CPA5 AA PA:\n").split(" ")))
    except Exception as e:
        raise SystemExit(f"An error occured with the input values. Error: {str(e).split(':')[0]}\n")

    if len(a) < 6 or len(a) > 6:
        print(f"You're supposed to input 6 values, but {len(a)} elements were provided. Please, try again.\n")
        continue

process=True
while process:
    try:
        b=float(input("Input what grade you want to get from the course:\n"))
    except Exception as e:
        raise SystemExit(f"An error occured while converting. Error: {str(e).split(':')[0]}\n")
    cpa=((a[0]+a[1]+a[2]+a[3])*0.2/4)
    aa=a[4]*0.15
    pa=a[5]*0.25
    fa=(b-cpa-aa-pa)/0.4
    print(f"\nYou need to get at least {fa:.2f} from the final exam in order to get your desired overall of {b:.02f}\n")
    haha = input("if you want to continue, type 'y':\n")
    if haha.strip().lower() != 'y':
        print("The session is over. Thank you for using this. We might consider making it profitable...")
        process = False


    


