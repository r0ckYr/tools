

def usefind():
    msg = "green,red,blue,red,gerrn,"
    lis = msg.partition(',')
    print(msg[140:100])
    msg1 = ''.join(lis)

    m = "hello"
    m1 = m + 'ff'
    print(m1)

def match(str1,str2):
    temp1 = str1.lower()
    temp2 = str2.lower()

    for i in temp1:
        print(i)

def fun():
    m = [['hhh', 'hh'], 'dfff']
    m1 = m
    print(m[0][0])


def commonChar(str1, str2):
    temp1 = str1.lower()
    temp2 = str2.lower()
    count = 0
    for i in range(len(temp1)):
        ch1 = temp1[i]
        if(ch1 not in temp1[:i]):
            for j in temp2:
                if(ch1==j):
                    count = count + 1
                    break
    
    print(count)



def productsum(n1,n2):
    p = n1*n2
    if p > 1000:
        s = n1+n2
        return s
    return p


def main():
    n1 = int(input("Enter first number "))
    n2 = int(input("Enter second number "))
    m = productsum(n1,n2)
    print(m)


def printrev():
    end = 10
    while(end>0):
        print(end)
        end = end - 1


printrev()
