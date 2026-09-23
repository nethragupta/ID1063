import numpy as np

# counts how many 1s in a row start at position i
def runLength(a, n, i):
    count = 0
    # keep going until we hit a 0 or the end of the array
    while i < n and a[i] == 1:
        count = count + 1
        i = i + 1
    return count

# read the limit k and the activity log (1 = studying, 0 = break)
k = int(input("Enter k: "))
a = np.array(input("Enter the log: ").split(), dtype=int)
n = len(a)   # length found automatically

ans = 0   # stays 0 if the rule is never broken

for i in range(n):
    # if the run starting here is longer than k, the rule breaks
    if runLength(a, n, i) > k:
        # (k+1)th session of this run is at position i+k,
        # +1 because sessions are numbered from 1
        ans = i + k + 1
        break

print(ans)
