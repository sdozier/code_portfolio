#Project Euler prob 67
#Simone Dozier

def readTriangle():
    """Converts triangle data in file to a matrix"""
    
    f = open('p067_triangle.txt','r')
    rows=[]
    for line in f:
        l=line[:-1].split(' ')
        rows.append(map(int,l))
    return rows

def process():
    """Finds the maximum path through the triangle

    Dynamic programming solution. Calculates maximum path to each square, starting
     with the first two squares and working down the triangle. Only stores the max
     path to each square so you don't calculate every path."""
    
    rows=readTriangle()
    ws = rows[0] #the working sums
    nws = [0,0] #"next working sum"
    for i in range(1,len(rows)):
        nws[0] = ws[0] + rows[i][0]
        nws[-1] = ws[-1] + rows[i][-1]
        for j in range(1,len(ws)):
            x1 = rows[i][j]+ws[j-1]
            x2 = rows[i][j]+ws[j]
            nws[j] = max(x1,x2)
        ws = nws
        nws = [0]*(i+2)
    return(max(ws))

def prob67():
    print process()
