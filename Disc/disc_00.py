def f(x):
    return x - 1
def g(x):
    return x * 2
def h(x,y):
    return int(str(x) + str(y))
'''
example = g( h(10, 12) )
10 == 5 * 2  >>>>>> 10 == g(5) >>>>>> g5
12 == 2 * 2 * (5 - 1 - 1) >>>>>> 12 == g( g( f( f(5) ) ) )   >>>>>>ggff5
so example = g ( h( g(5), g( g( f( f(5) ) ) ) ) ) >>>>>> g( h( g5, ggff5 ) ) >>>>>> gh(g5, ggff5)
'''
example = g(h(g(5),g(g(f(f(5))))))

print(example)
