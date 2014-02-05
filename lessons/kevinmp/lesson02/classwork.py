
# matrices copied from instructors notes with one additional for error checking
v = [5, 6, 7, 8]
m1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
m2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
m3 = [[1, 2], [3, 4], [5, 6]]

def matrixbycolumnvector(m, cv):
    """ 
    input / bounds checking makes up a majority of 
    any production code, so I'm to skip all of that
    and just do a few simple checks.
    Note: I'm not even checking that they're all ints
    """
    """
    check that the 1st input is a matrix (well list of lists)
    not even checking that the sizes are the same (that wouldn't
    be a matrix anymore, would it?
    """
    if not all(isinstance(i, list) for i in m):
        print "First input must be a matrix"
        return False
        
    """
    check that the 2nd input is a column vector (well, not
    a list of lists, anyway)
    """
    if any(isinstance(i, list) for i in cv):
        print "Second input must be a column vector"
        return False
    
    """
    check that cols in matrix match rows in column vector
    i.e. check that multiplication is possible
    """
    if not len(m[0]) == len(v):
        print "The number of columns in the matrix must equal the number of" 
        print "rows in the column vector"
        return False

    # okay, passed all the "basic" checks, let's do math
    
    result = [0]*len(m)
    
    for i in range(len(m)):
        dotproduct = 0
        print "Result[" + str(i) + "] = ",
        for x in range(len(v)):
            print "(" + str(m[i][x]) + " x " + str(v[x]) + ")",
            if not x==len(v)-1:
                print " + ",
            else:
                print
            dotproduct += m[i][x] * v[x]
        result[i] = dotproduct
    
    return result

def matrixbymatrix(m1, m2):
    """ 
    input / bounds checking makes up a majority of 
    any production code, so I'm to skip all of that
    and just do a few simple checks.
    Note: I'm not even checking that they're all ints
    """
    
    """
    checking that all inputs are matrices (well, list of
    lists, anyway)
    """
    if not all(isinstance(i, list) for i in m1):
        print "First input must be a matrix"
        return False
    elif not all(isinstance(i, list) for i in m2):
        print "Second input must be a matrix"        
        return False
        
    """
    unlike matirix by vector, there's too many row cols to keep
    track of here, so I'm putting them into vars
    Note:
    """
    m1_rows = len(m1)
    m1_cols = len(m1[0])
    m2_rows = len(m2)
    m2_cols = len(m2[0])

    if not m1_cols == m2_rows:
        print "The number of columns in matrix 1 must equal the number of rows in matrix 2"
        return False
    
    # "basic" checks are ok, let's do math
    
    # initialise an empty result matrix
    result = []
    for i in range(m1_rows):
        result.append([])
        for x in range(m2_cols):
            result[i].append(0)

    for x in range(m1_rows):
        for y in range(m2_cols):
            print "Result[" + str(x) + "]"+"["+str(y)+"] = ",
            for z in range(m1_cols):
                print str(m1[x][z]) + " x " + str(m2[z][y]),
                if not z == m1_cols-1:
                    print " + ",
                else:
                    print 
                result[x][y] += m1[x][z]*m2[z][y]
    
    return result

def idMatrix(size):
    
    #check that size is an int
    if not isinstance(size, int):
        print "Enter a size in integer"
        return False
    # loop it
    result = []
    for x in range(size):
        result.append([])
        for y in range(size):
            result[x].append(0)
            if x == y:
                result[x][y] = 1
    
    return result


# will not run   
matrixbycolumnvector(v, m1)
# will not run
matrixbycolumnvector(m1, m1)
# will not run
matrixbycolumnvector(m2, v)
# runs
print matrixbycolumnvector(m1, v)
# will not run
matrixbymatrix(v,m2)
# will not run
matrixbymatrix(m1,v)
# will not run
matrixbymatrix(m1,m3)
# runs
print matrixbymatrix(m1,m2)
# will not run
idMatrix("four")
# runs
print idMatrix(4)


