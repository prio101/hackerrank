def findMin(V):
     
    # All denominations of Indian Currency
    deno = [100, 50, 25, 10, 5, 1]
    n = len(deno)
     
    # Initialize Result
    ans = []
 
    # Traverse through all denomination
    i = n - 1
    while(i >= 0):
         
        # Find denominations
        while (V >= deno[i]):
            V -= deno[i]
            ans.append(deno[i])
 
        i -= 1
 
    # Print result
    print(ans)
 
# Driver Code
if __name__ == '__main__':
    n = 7
    print("Following is minimal number",
          "of change for", n, ": ", end = "")
    findMin(n)