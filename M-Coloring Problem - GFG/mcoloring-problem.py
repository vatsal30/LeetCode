#User function Template for python3

def isPossible(graph, color, i, idx, V):
    for k in range(V):
        if (k!= idx and graph[idx][k] == 1 and color[k]==i):
            return False
    return True

def canColor(idx, graph, color, V, k):
    if (idx == V):
        return True
    
    for i in range(k):
        if (isPossible(graph, color, i+1, idx, V)):
            color[idx] = i + 1
            if (canColor(idx+1, graph, color, V, k)):
                return True
            color[idx] = 0
    return False
#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    #your code here
    color = [0]*V
    return canColor(0, graph, color, V, k)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends