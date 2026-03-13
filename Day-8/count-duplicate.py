def count_duplicates(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
             count +=1
    return count
def main():
    arr = [1, 2, 3, 4, 5, 6, 4, 2, 1, 5]
    print('duplicates: ', count_duplicates(arr))
main()
