def search_with_duplicates(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        
        # Handle duplicates properly
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue   # 🔥 important fix
        
        # Left half sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half sorted
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
                
    return -1


arr = [4,5,6,6,7,8,1,2]
target = 6
print(search_with_duplicates(arr, target))