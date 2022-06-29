# h = {1,13.6,True,'Hii',False,458.35}                                          # difference_update(Doubt)                                              
# g = {False,'python',55,458.35}

# # h.difference_update(g)
# # print(h)                                                                   # {1,13.6,'Hii'}
# g.difference_update(h)
# print(g)                                                                    # {'python', 55}


# y = {"pineapple","apple","banana",23,.36}                                         # intersection_update()
# z = {"Dxc","CGI","Dell",'apple'}

# x = y.intersection_update(z)
# print(x)                                                                         # None (Doubt)


''' Return True if all items set y are present in set x: '''

# x = {'a','b','c',}                                                                    # issuperset()
# y = {'z','y','t','a','d','c','b'}

# z = x.issuperset(y)
# print(z)                                                                                # False
# t = y.issuperset(x)
# print(t)                                                                                  # True  

# g  = {'z','y','t','a','d','c','b'}
# o = {'a','b','c',}
# h = g.issuperset(o)
# print(h)                                                                                # True

# f = o.issuperset(g)
# print(f)                                                                                # False

# g = {'python',36,True,3.652}                                                             # remove
# g.remove(True)
# print(g)                                                                                # {3.652,36,'python}
# g.remove(45)
# print(g)                                                                                  # KeyError : 45

''' The symmetric_difference() method returns a set that contains all items from both set, 
                                                    but not the items that are present in both sets. '''

# m = {'python',1,56,1.23,'hii'}                                                          # symmetric_difference()
# n = {"hii",5.36,5.6,1.23}

# l = m.symmetric_difference(n)
# print(l)                                                                                # {5.36,5.6,'python',1,56}

# n.symmetric_difference_update(m)
# print(n)                                                                             # {1, 5.36, 5.6, 'python', 56} -   # None(Doubt)


''' The symmetric_difference_update() method updates the original set 
                                   by removing items that are present in both sets, and inserting the other items.'''



w = {'sam','bob','carlie','hub'}
x = {'bob','IT','infosys','sam'}

w.symmetric_difference_update(x)
print(w)                                                                          # {'hub', 'infosys', 'IT', 'carlie'}


x.symmetric_difference_update(w)
print(x)                                                                           # {'IT', 'carlie', 'hub', 'infosys'}


e = {1,2,3.6,12,45,63,5}
w = {2,6,56,859,62,}
e.symmetric_difference_update(w)
print(e)