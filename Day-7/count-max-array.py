def count_max(arr):
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
    max_count=0
    result=None
    for key,value in freq.items():
        if value>max_count:
            max_count=value
            result=key
    return result
def main():
    arr=[1,3,2,3]
    print("most frequent:",count_max(arr))
main()
