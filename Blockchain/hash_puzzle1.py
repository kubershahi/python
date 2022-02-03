import hashlib
import time

'''

x (binary string) = 1111011111101111111001111110110 
decimal representatin = 2079847414

'''

start = time.time()

k = 226
T = 2**k                 # given T is 2^226

throws = 2**31     # expected number of throws = 2^30, taking 2^31 throws

for i in range(throws):
    # print(i)
    
    h = hashlib.sha256()
    h.update(b'kuber.shahi_asp22@ashoka.edu.in' + i.to_bytes(4,'big'))
    a = h.hexdigest()
    a_int = int(str(a), 16)
    
    if (a_int < T):
        print(a_int)
        print("............ is a solution where x is:", i)
        print("{0:0256b}".format(a_int))
        break

print("\nNumber of iterations: ", i)

end = time.time()
print("Time elasped: ", (end - start)/60, 'min')


# Code to check the answer

# h = hashlib.sha256()
# h.update(b'kuber.shahi_asp22@ashoka.edu.in' + (2079847414).to_bytes(4,'big'))
# a = h.hexdigest()
# print(a)
# a_int = int(str(a), 16)
# print(a_int)

# if (a_int < T):
#     print('Correct x')