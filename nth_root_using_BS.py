#Optimal Approach TC= O(logM) SC=O(1)
def nthRoot(n, m):
        # Set low and high for binary search
        low, high = 1, m

        # Start binary search
        while low <= high:
            # Calculate mid
            mid = (low + high) // 2

            # Store result of mid^n
            ans = 1
            for _ in range(n):
                ans *= mid
                

            # If mid^n equals m
            if ans == m:
                return mid

            # If mid^n is less than m
            if ans < m:
                low = mid + 1

            # If mid^n is more than m
            else:
                high = mid - 1

        # Return -1 if not found
        return -1
print(nthRoot(4,256))
'''#bruteforce
def nthRoot(self, n, m):
        # Loop from 1 to m
        for i in range(1, m + 1):
            # Compute i^n
            power = i ** n

            # If equal to m, return i
            if power == m:
                return i

            # If exceeds m, break
            if power > m:
                break

        # If not found, return -1
        return -1'''