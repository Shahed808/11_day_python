''' set is immutable data type
And it is unordered'''


# d = {1,True,'hello',3.65,None}                                                 
# print(d,type(d))                                                                # {1,'hello',3.65,None}


# s = {1,2,1,2,1,2,1,2,3}
# print(s)                                                                        # {1,2,3}


                                                                           

# w = {1,3.65,False,('hii',25)}
# print(w,type(w))

# print(dir(set))

'''         set methods              '''

# q = {1, 2,3,5}                                                                    # add()
# p = 6,1,5,8,9,7
# q.add(p)
# print(q)                                                                         # {1,2,3,5,(6,1,5,8,9,7)}


# s = {1,2,1,2,1,2,1,2,3}                                                           # clear()
# s.clear()
# print(s)                                                                          # set()


# e = {1,'code',3.6,("program",1,5)}                                                # copy()
# d = e.copy()
# print(d)                                                                       # {1, 3.6, 'code', ('program', 1, 5)}



# h = {1,13.6,True,'Hii',False,458.35}                                          # difference()                                              
# g = {False,'python',55,458.35}

# a = h.difference(g)
# b = g.difference(h)

# print(a)                                                                        # {1,13.6,'Hii}
# print(b)                                                                        # {'python',55}
# print(h-g)                                                                      # {1,13.6,'Hii}
# print(g-h)                                                                      # {'python',55}


# h = {1,13.6,True,'Hii',False,458.35}                                          # difference_update(Doubt)                                              
# g = {False,'python',55,458.35}

# # h.difference_update(g)
# # print(h)                                                                   # {1,13.6,'Hii'}
# g.difference_update(h)
# print(g)                                                                    # {'python', 55}


# c = {"hello",None,3.5,562}                                                      # discard()
# c.discard(3.50)
# print(c)                                                                        # {'hello',562,None}

# c.discard('hellol')
# print(c)                                                                        # {'hello', None, 3.5,562}


# y = {"pineapple","apple","banana",23,.36}                                         # intersection()
# z = {"Dxc","CGI","Dell","apple",0.36}

# t = y.intersection(z)
# print(t)                                                                       # {'apple',0.36}


# y = {"pineapple","apple","banana",23,.36}                                         # intersection_update()
# z = {"Dxc","CGI","Dell",'apple'}

# x = y.intersection_update(z)
# print(x)                                                                         # None (Doubt)


# r = {'cake',12,'dog',3.65,True}                                                   # isdisjoint()
# s = {False,3.65,'pet'}

# g = r.isdisjoint(s)
# print(g)                                                                            # False


# l = {'code',3.6,'hii',45}
# o = {'python',256,True}

# b = l.isdisjoint(o)
# print(b)                                                                            # True

''' The issubset() method returns True if all items in the set exists in the specified set,
                                    otherwise it retuns False.
             Return True if all items in set x are present in set y:      '''

# i = {1,2,3,4}                                                                         # issubset()
# m = {4,6,8,9,7,2}

# j = i.issubset(m)
# print(j)                                                                              # False

# i = {1,2,3,4}
# m = {4,6,8,9,7,2,1,3}

# h = m.issubset(i)
# print(h)                                                                               # False

# y = i.issubset(m)
# print(y)                                                                               # True

''' Return True if all items set y are present in set x: '''

# x = {'a','b','c',}
# y = {'z','y','t','a','d','c','b'}

# z = x.issuperset(y)
# print(z)                                                                                # False

# g  = {'z','y','t','a','d','c','b'}
# o = {'a','b','c',}
# h = g.issuperset(o)
# print(h)                                                                                # True

# f = o.issuperset(g)
# print(f)                                                                                # False


# v = {'bob','hi',56,3.65,True,1}                                                         # pop()
# v.pop()
# print(v)                                                                                # {True,3.65,'hi',56}


# g = {'python',36,True,3.652}                                                             # remove
# g.remove(True)
# print(g)                                                                                # {3.652,36,'python}


# g = {'python',3,1,2,45,456,.356}                                                         # update()
# k = ['dog',36,45.36,'python',456]
# g.update(k)
# print(g)                                                                                # {0.356, 1, 2, 3, 'python', 'dog', 456, 36, 45, 45.36}


# w = {'python',3,1,2,45,456,.356}                                                         # update()
# o = {'dog',36,45.36,'python',456}
# w.update(o)
# print(w)                                                                                # {0.356, 1, 2, 3, 36, 456, 45, 45.36, 'dog', 'python'}


# d = {1,2,4,5,3.6,'hii'}                                                                 # union
# e = {5,8,9,7,6,2,1,4,'python'}

# t = d.union(e)
# print(t)                                                                                # {'python', 1, 2, 3.6, 4, 5, 6, 7, 'hii', 8, 9}


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