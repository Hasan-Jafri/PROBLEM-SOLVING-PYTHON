# Program to convert decimal to binary.

num = 48
print(bin(num))
binary = ""
# loop_item = num
# while(loop_item > 0):
#     if(loop_item % 2 ==0):
#         binary= "0" + binary
#     else:
#         binary = "1" + binary
#     loop_item = loop_item // 2
#     # print(loop_item)
# binary = str(loop_item) + binary
# print(binary)

# Efficient Method.
while(num > 0):
    rim = num % 2
    binary = str(rim) + binary
    num = num//2 
# binary = str(num)  + binary #Using this for unsigned i.e 0.

print(binary)     