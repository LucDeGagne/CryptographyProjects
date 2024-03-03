def inversemod(a,b):
    r = 0
    old_r = 1
    while b != 0:
        quot = a // b
        a, b = b, a%b
        r, old_r = old_r - quot * r, r
    return old_r

def getinv(num, den, p):
    inv = inversemod(den, p)
    return num * inv

def productInputs(vals):
    prod = 1
    for v in vals:
        prod = prod * v
    return prod

def lagrange(x, x_i, y_j):
    #f(x) = sum(y_j*l_j(x)) where j=0 to j=4
    p = 8675309
    nums = []
    dens = []
    for i in range(len(x_i)): #len(x_i) should be 5 or else not all the x's needed
        cur = x_i[i]
        top = []
        bottom = []
        for j in range(len(x_i)):
            if (x_i[j] != x_i[i]): #Don't want to subtract by itself and multiply by 0
                top.append(x - x_i[j])
                bottom.append(cur - x_i[j])
        nums.append(productInputs(top))
        dens.append(productInputs(bottom))
    #Combination of nums and dens would produce l_j(x)
    den = productInputs(dens) #Create a common denominator
    y_jl_jx = []
    for i in range(len(x_i)):
        y_jl_jx.append(getinv(nums[i] * den * y_j[i] % p, dens[i], p))
    fx = sum(y_jl_jx)
    return (getinv(fx, den, p) + p) % p #Just missing modulo work
x1 = [12,23,34,45,56]
y1 = [7143298,1423230,5749964,7567123,6604906]
x2 = [67, 78, 89, 91, 107]
y2 = [6204779,4644166,3811758,2227010,6208490]
print(lagrange(0,x1,y1))
print(lagrange(0,x2,y2))

print(lagrange(613,x1,y1))
print(lagrange(613,x2,y2))
