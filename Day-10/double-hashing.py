'''
double hashing : it uses two hash functions.
formula : index = h1(key) + (i*h2(key))%table_size
h1(key): key % table_size
h2(key): prime number lesser than table size -(key % prime number lesser than table_size)

ex : [8,15,22] , table_size=7
h1(key)= 8%7 = 1
i1-> 8

h1(key)=15
15%7=1
h2(key)= 5-(15%5) = 5
1+ (1*5)%7 = 6

i6-> 15

h1(key)=22
22%7=1
h2(key)= 5-(22%5)=3
1+(1*3)%7 = 4
i4-> 22
'''
table_size = 7
hash_table = [None] * table_size

def h1(key):
    return key % table_size

def h2(key):
    return 5 - (key % 5)

def insert(key):
    index = h1(key)

    if hash_table[index] is None:
        hash_table[index] = key
    else:
        i = 1
        while True:
            new_index = (h1(key) + i * h2(key)) % table_size
            if hash_table[new_index] is None:
                hash_table[new_index] = key
                break
            i += 1

keys = [8, 15, 22]

for key in keys:
    insert(key)

print("Final Hash Table:")
for i in range(table_size):
    print(i, ":", hash_table[i])
