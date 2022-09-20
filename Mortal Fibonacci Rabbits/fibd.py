import numpy as np
n, m = 94, 16
profile = np.zeros(m, dtype=np.uint256)
profile[0] = 1
for i in range(n):
    temp = np.zeros(m, dtype=np.uint256)
    print(f'{i+1}: {profile.sum():20d}')
    for j in range(profile.size-1, 0, -1):
        temp[j] = profile[j-1]
    temp[0] = np.sum(profile[1:])
    profile = temp
