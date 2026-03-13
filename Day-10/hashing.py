'''
Hashing : it is a technique used to store and retrieve data using key.
* In python, hashing is implemented using dictionaries(dict)

----->o(1)
* hashing allows fast lookup o(1) time complexity

1.open hashing : whenever we get same index value colliding with the previous index,it is going to be stored in a form of linked list.
* all the collisions are stored in chain.

advantages: 1. easy to implement 2. no need to search for empty slots 3. table never becomes completely full 4. handles many collisions. 


2. closed hashing: in closed hashing all the elements are stored inside the hash table itself.
* when a collision occurs, we find the another empty slot in the table.
* no linked list are used.

types of closed hashing :
1.Linear probing : when collision occurs, the next slot should be filled sequentially.
formula : (index + i) % table_size

2.Quadratic probing: instead of checking next index, we jump using squares.
formula : (index + i^2) % table_size 



problem : 9,16,23

linear -> 9%7 = 2
 (0 + 2) % 7 = 2
i-2 -> 9

16%7=2
(1+2)%7=3
i-3 -> 16

23%7=2
(2+2)%7 = 4
i-4 -> 23

quadratic -> 9%7=2
(2+0)%7 = 2
i-2 -> 9

16%7=2
(2+1)%7=3
i-3->16

23%7=2
(2+4)%7 = 6
i-6 -> 23
'''
table_size=7
hash_table=[None]*7
def hash_function(key):
    return key % table_size
def insert_linear(key):
    index = hash_function(key)
    i=0
    while hash_table[(index+i)% table_size] is not None :
        i+=1
    new_index =(index+i)%table_size
    hash_table[new_index]=key
keys=[8,15,22]
for key in keys:
    insert_linear(key)
print("linear probing table:")
print(hash_table)

