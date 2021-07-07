from pythonic import CountFromTen, decor1, decor, Parrot

def test_task1():
    actual = []
    for i in CountFromTen(15):
        actual.append(i)
        
    expected = [10,11,12,13,14,15]

    assert actual == expected


def test_task2():
    @decor1
    @decor
    def num(): 
        return 10
  
    actual = num()
    expected = 400

    assert actual == expected 


def test_task3():
    parrot = Parrot('romeo', 2)
    actual = print(parrot)
    expected = '''
\\
(o>
//\
V_/__
||
||

 This is romeo, 2 years old.'''
