arr=[1,2,3,4,5]
seen=set()
duplicates=False
for num in arr:
    if num in seen:
        duplicates=True
        break
    seen.add(num)
if duplicates:
    print("Duplicates present")
else:
    print("no duplicates")
