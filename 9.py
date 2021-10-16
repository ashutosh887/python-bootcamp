# Sets
# Contains only unique values

s = set()
l = [1,2,3,4,5,6,5,7,8,7,6]
l = set(l)

print(l)
print(type(l))

l.add(10)
l.remove(1)

# Some set functions
s1 = l.union({1,2,33})
s2 = l.intersection({2,3,4,5})


# .isdisjoint
# .difference
print(s, s1, s2)