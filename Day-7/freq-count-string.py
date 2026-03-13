def freq_count(s):
    freq={}
    for ch in s :
        freq[ch]=freq.get(ch,0)+1
    return freq
def main():
    s=input("enter the string:")
    result=freq_count(s)
    print("frequency count:",freq_count(s))
main()
