

def find_threshold(arr,threshold):
    first_difference = []
    second_difference = []
    result = []
    for i in range(1,len(arr)):
        first_difference.append(abs(arr[i] - arr[i-1]))
    for j in range(1,len(first_difference)):
        second_difference.append(abs(first_difference[j]-first_difference[j-1]))
    for i in second_difference:
        if i >= threshold:
            result.append(1)
        else:
            result.append(0)
    return result

n = int(input())
threshold = int(input())
result = []
for i in range(n):
    pkgs = int(input())
    input_ = str(input())
    array = input_.strip().split()
    array = [int(element) for element in array]
    result.append(find_threshold(array,threshold=threshold))

for i in result:
    for j in i:
        print(j,end=" ")
    print()
