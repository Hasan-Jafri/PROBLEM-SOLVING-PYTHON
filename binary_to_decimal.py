# Program to convert binary to decimal.

binary = 10101010
answer = 0
binary = str(binary)

for i in range(len(binary)-1,-1,-1):
    answer += int(binary[i])*(2**(len(binary)-i-1))
    
print(answer)