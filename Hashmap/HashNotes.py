# Hashsets

s= set()
print(s)

# Add item into Set - O(1)
s.add(1)
s.add(2)
s.add(3)

print(s)

#Lookup if item in  set - O(1) amortized
if 1 in s:
    print(True)

#Remove -O(1)
s.remove(2)
print(s)

#Set construction - O(S) - S is the length of the string
string = "aaaaaabbbbbbbbbbccccccceeeeeeeee"
sett = set(string)

print(sett)
# Loop aver items in set - O(n) - n is the length of the set
for x in sett:
    print(x)

# Hashmaps - Dictionary
#Value can be everything
d = {'greg' : 1, 'steve' :2, 'rob':3}

#Add key:val in dictionary - O(1)
d['arsh']=4
print(d)

# Check for presence of key in dictionary - O(1)
if 'greg' in d:
    print(True)

# Check the value corresponding to a key in the dictionary - O(1)
# The key must be in the dictionary (error if not)
print(d['greg'])

#Loop over the key:value pairs of the dictionary - O(n) - n is the length of the dictionary
for key, val in d.items():
    print(f'key {key}: val {val}')

# Defaultdict
from collections import defaultdict
default = defaultdict(int)
# That return 0 if 2 is not in the dictionary, not as precedent dictionary
print(default[2])

# Counter
from collections import Counter
counter = Counter(string)
print(counter)