import hashlib
import time

start = time.time()

k = 226
T = 2**k                 # given T is 2^226

throws = 2**(256 - k)     # hence number of throws is 2^30

email = 'kuber.shahi_asp22@ashoka.edu.in'

for i in range(throws):
    h = hashlib.sha256()
    inp = email + str(i)
    h.update(inp.encode())  # byte length 4 which is 2^32 
    a = h.hexdigest()
    
    a_int = int(str(a), 16)

    if (a_int < T):
        print(a_int)
        print("............ is a solution where x is:", i)
        print("Number of leading 0’s in H(x):", 256-k)
        print("{0:0256b}".format(a_int))
        break


print("Number of iterations: ", i)

end = time.time()
print("Time elasped: ", (end - start) % 60, 'min')



# Code to check the correct answer

# h = hashlib.sha256()
# inp = 'kuber.shahi_asp22@ashoka.edu.in' + str()
# h.update(inp.encode())
# a = h.hexdigest()
# print(a)
# a_int = int(str(a), 16)
# print(a_int)

# if (a_int < T):
#     print('Correct x')
