#Kennon sauter,U2L4, DS, 10/9/24



def mat_sum(m1, m2):
    rowsize = len(m1) 
    collumns = len(m2[0])
    new = [[0]*rowsize for i in range(collumns)]
    if rowsize != collumns:
        return "no solution"
    for i in range(rowsize):
        for j in range(collumns):
            new[i][j] = m1[i][j] + m2[i][j] 

    return new

def mat_mul(m1, m2):
    rowsize = len(m1) 
    m1col = len(m1[0])
    m2row = len(m2)
    collumns = len(m2[0])
    if m1col == m2row:
        new = [[0]*collumns for i in range(rowsize)]
        print(new)
        #if rowsize != collumns:
        #return "no solution"    
    
        for i in range(rowsize):
        
            for j in range(collumns):
                for h in range(m1col):
                    new[i][j] += (m1[i][h] * m2[h][j]) 
            
        return new
    else:        
        return "no solution"