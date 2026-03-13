def count_vowel(text):
    count=0
    vowels="aeiouAEIOU"
    for char in text:
        if char in vowels:
            count+=1
    return count
def main():
    text=input("enter the name:")
    print("vowel count: ",count_vowel(text))
main()
    
