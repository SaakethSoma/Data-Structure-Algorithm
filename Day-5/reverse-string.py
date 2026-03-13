def rev_string(text):
    reversed_text=""
    for char in text:
        reversed_text=char + reversed_text
    return reversed_text
def main():
    text=input("enter the name:")
    print("reversed text:",rev_string(text))
main()
