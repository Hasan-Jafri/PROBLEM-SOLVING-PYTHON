#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      walit
#
# Created:     04/11/2023
# Copyright:   (c) walit 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def calculate_combinations(n, k):
    if k < 0 :
        return 0
    if k == 0 or k == n or k > n:
        return 1

    numerator = 1
    denominator = 1

    for i in range(1, min(k, n - k) + 1):
        numerator *= n
        denominator *= i
        n -= 1

    return numerator // denominator


def main():
    test=int(input(""))
    N=int(input(""))
    data=[]
    for i in range(N):
        dept=int(input(''))
        for i in range(dept):
            ids=input('').split()
            data+=ids
    data = list(set(data))
    result = calculate_combinations(len(data), N)
    print(result)



if __name__== '__main__':
    main()