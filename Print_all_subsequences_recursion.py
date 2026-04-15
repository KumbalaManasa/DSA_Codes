def getSubsequences(s: str) -> list[str]:
        # Length of input string
        n = len(s)

        # Total subsequences = 2^n
        total = 1 << n

        # List to store all subsequences
        subsequences = []

        # Iterate over all bit masks from 0 to 2^n - 1
        for mask in range(total): #lets say mask = 5 check position i = 0, 1 << 0 = 001, 5 = 101 101 and 001 → NOT ZERO → YES now check for all places i=1,i=2 etc
            # Temporary subsequence list
            subseq = []

            # Check each bit position in mask
            for i in range(n):
                # If i-th bit of mask is set, include s[i]
                if mask & (1 << i):
                    subseq.append(s[i])

            # Store the formed subsequence as string
            subsequences.append("".join(subseq))

        # Return all generated subsequences
        return subsequences

s = "abc"
print(getSubsequences(s))