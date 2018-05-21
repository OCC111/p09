def jie(k):
    if k>1:
        result = k*jie(k-1)
    else :
        result = 1
    return result
a = jie(521)
print(a)
