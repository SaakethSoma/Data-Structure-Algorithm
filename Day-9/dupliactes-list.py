#counting duplicates in list

def count_duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False
def main():
    arr=[1,1,1,2,3]
    print("duplicates found:",count_duplicates(arr))
main()


# step-1 : 1-> for 1 in arr , if 1 in seen: False -> seen.add(1) -> set(1)
# step-2 : 1-> for 1 in arr , if i in seen: -> True -> duplicates found !!
