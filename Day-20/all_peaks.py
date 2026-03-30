def all_peaks(arr):
    n=len(arr)
    peaks=[]
    for i in range(n):
        if (i==0 or arr[i]>=arr[i-1]) and \
            (i==n-1 or arr[i]>=arr[i+1]):
                peaks.append(arr[i])
    return peaks
arr=[20,1,2,4,20,7,6,20]
print(all_peaks(arr))