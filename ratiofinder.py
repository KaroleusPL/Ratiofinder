#!/bin/python3

# Made by KaroleusPL
# MIT License
# Copyright (c) 2026 Karoleus.PL

def ratiofinder_normal():
    print("Mode: normal\n")

    ratio = input("Enter ratio ('a/b') or 'exit': ")

    ratio = ratio.replace(" ", "")

    if ratio.istitle and ratio.lower() == "exit":
        return

    ratio_split = ratio.split("/")

    if len(ratio_split) < 2:
        print("Error: invalid syntax")
        return

    ratio_a = ratio_split[0]
    ratio_b = ratio_split[1]

    if ratio_a.isdecimal() and ratio_b.isdecimal():

        ratio_a = int(ratio_a)
        ratio_b = int(ratio_b)
        
        if ratio_a > 0 and ratio_b > 0:

            ratio_count = input("How many ratios would you like to get? (starting from " + str(ratio_a) + "x" + str(ratio_b) + ") ")

            if not ratio_count.isdecimal():
                print("Error: ratio count must be an integer")

                return

            if int(ratio_count) < 0:
                print("Error: ratio count must bigger than 0")

                return

            print("\033[34m", str(ratio_a), " x ", str(ratio_b), "\033[0m")

            for i in range(int(ratio_count)):
                cur_a = ratio_a * (i + 2)
                cur_b = ratio_b * (i + 2)

                if cur_a % 8 == 0 and cur_b % 8 == 0:
                    print("\033[32m", str(cur_a), " x ", str(cur_b), " - Divisible by 8\033[0m")
                else:
                    print(str(cur_a), " x ", str(cur_b))
            
        else:
            print("Error: ratio must be bigger than 0.")
            return
    else:
        print("Error: ratio can contain integers only.")
        return


def ratiofinder_advanced():
    print("Mode: advanced\n")
    ratio = input("Enter ratio ('a/b') or 'exit': ")

    ratio = ratio.replace(" ", "")

    if ratio.istitle and ratio.lower() == "exit":
        return

    ratio_split = ratio.split("/")

    if len(ratio_split) < 2:
        print("Error: invalid syntax")
        return

    ratio_a = ratio_split[0]
    ratio_b = ratio_split[1]

    if ratio_a.isdecimal() and ratio_b.isdecimal():

        ratio_a = int(ratio_a)
        ratio_b = int(ratio_b)
        
        if ratio_a > 0 and ratio_b > 0:

            ratio_count_type = input("How to get the amount of ratio? (amount/until) ")

            #Until
            if ratio_count_type == "until": 
                ratio_stop_marker = input("At what width should ratio stop? (width = a) ")

                if not ratio_stop_marker.isdecimal():
                    print("Error: ratio stop marker must be an integer")
    
                    return

                if int(ratio_stop_marker) < 0:
                    print("Error: ratio stop marker must bigger than 0")
    
                    return

                print("\033[34m", str(ratio_a), " x ", str(ratio_b), "\033[0m")

                start_a = ratio_a
                start_b = ratio_b
                i = 1

                cur_a = start_a
                cur_b = start_b

                while (cur_a < int(ratio_stop_marker)):
                    i += 1
                    cur_a = start_a * i
                    cur_b = start_b * i
                    
                    if cur_a % 8 == 0 and cur_b % 8 == 0:
                        print("\033[32m", str(cur_a), " x ", str(cur_b), " - Divisible by 8\033[0m")
                    else:
                        print(str(cur_a), " x ", str(cur_b))

            #amount
            else:

                ratio_count = input("How many ratios would you like to get? (starting from " + str(ratio_a) + "x" + str(ratio_b) + ") ")

                if not ratio_count.isdecimal():
                    print("Error: ratio count must be an integer")
    
                    return

                if int(ratio_count) < 0:
                    print("Error: ratio count must bigger than 0")
    
                    return

                print("\033[34m", str(ratio_a), " x ", str(ratio_b), "\033[0m")

                for i in range(int(ratio_count)):
                    cur_a = ratio_a * (i + 2)
                    cur_b = ratio_b * (i + 2)

                    if cur_a % 8 == 0 and cur_b % 8 == 0:
                        print("\033[32m", str(cur_a), " x ", str(cur_b), " - Divisible by 8\033[0m")
                    else:
                        print(str(cur_a), " x ", str(cur_b))
            
        else:
            print("Error: ratio must be bigger than 0.")
            return
    else:
        print("Error: ratio can contain integers only.")
        return

print("\nRatiofinder 1.0 - KaroleusPL \n")

mode = input("normal/advanced: ")

if mode == "advanced":
    ratiofinder_advanced()
else:
    ratiofinder_normal()