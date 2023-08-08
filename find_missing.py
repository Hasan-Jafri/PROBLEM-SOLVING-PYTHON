# Finding which number is missing from the array.

array = [37, 16, 81, 92, 5, 67, 44, 95, 14, 76,0, 84, 63, 91, 
         68, 9, 90, 72, 43, 47, 30, 93, 62, 100, 29, 36, 57, 12, 85, 94, 56, 20, 53, 
         25, 23, 86, 89, 55, 41, 48, 32, 19, 83, 73, 40, 13, 42, 45, 97, 2, 58, 70, 26, 87, 
         11, 17, 65, 78, 74, 28, 66, 21, 50, 38, 31, 88, 64, 34, 8, 39, 75, 4, 80, 79, 18, 35, 61, 
         24, 10, 22, 60, 69, 49, 98, 7, 15, 77, 51, 1, 27, 59, 99, 71, 3, 52, 33, 6, 82, 54, 46]
sum = 0
for i in range(len(array)):
    sum = sum + array[i]
result = 5050 - sum # Such that the array conatains elements 0-100 so the total sum would be 5050.

print(result)