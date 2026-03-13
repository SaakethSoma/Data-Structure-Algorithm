def count_duplicate_opt(arr):
    freq={}
    count=0
    for num in arr:
        if num in freq:
            count+=1
        else:
            freq[num]=1
    return count
def main():
      arr = [1, 2, 3, 4, 5, 6, 4, 2, 1, 5]
      print('duplicates: ', count_duplicate_opt(arr))
main()
