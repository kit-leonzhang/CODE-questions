def makeConnected(n: int, connections: list) -> int:
    if n > (len(connections) + 1):
        return -1
    elif ((n-2)*(n-1)/2+1) <= len(connections):
        return 0
    else
