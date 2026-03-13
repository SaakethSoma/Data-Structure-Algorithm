def count_char(text):
    count=0
    for char in text:
        count+=1
    return count
def main():
    text=input("enter the name:")
    print("char count: ",count_char(text))
main()
    
