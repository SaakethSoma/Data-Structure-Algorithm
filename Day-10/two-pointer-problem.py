arr = [2, 7, 11, 13]
target = 9

left = 0
right = len(arr) - 1

while left < right:
    current_sum = arr[left] + arr[right]

    if current_sum == target:
        print(arr[left], arr[right])
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1
