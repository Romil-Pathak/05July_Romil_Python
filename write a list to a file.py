'''list = ['pradip','sudha','dipal']
with open('text2.txt', 'w') as l:
    l.write(str(list))'''

'''class P:
    def __init__(self):
        y={-9}
print(P()==P())'''

'''h='7834834001'
h=h[3::3] + '23'*3+'461'
print(len(h))'''

'''a=5
class B:
    def __init__(self):
        a=4
if __name__=='__main__':
    B()
    print(a)'''

def doTheJob():
    try:
        return 5
    except:
        return 8
    finally:
        return 11
    
    return 12
print(doTheJob())

