'''
freq counting
no.of times the element appears in the container(arrays or strings)
used in hashmaps,sliding window,backend logic,real-time cases
'''
def freq_count(arr):
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
    return freq
def main():
    arr=[1,2,2,1,2,3,2,1,3,4,5,5]
    result=freq_count(arr)
    print("frequency count:",result)
main()

