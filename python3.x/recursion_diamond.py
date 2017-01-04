#!/usr/bin/python
# -*- encoding:UTF-8 -*-
V = '*'
V2 = ' '
def pb(i,v):
    '''定义打印函数，不换行的方式打印各行的 凸显符号和 空白符号'''
    '''打印个数为i+1 个且不换行'''
    if i > 0:
        print ('{}'.format(v),end='')
        pb(i-1,v)
    else:
        print (v,end='')
def main(k,d=1,b=1):
    '''k 为上三角行数，d 表示每行单个空格或星号所占宽度，b用作递归条件变换'''
    '''空格宽度，单个空格 乘以 d ， 打印 * 号个数通过传入参数控制'''
    V1 = V*d
    if k > 0:
        pb(k,V1,)
        pb(2*d*b-2*d,V2,)
        pb(k, V1)
        print ('')
        main(k-1,d,b+1)
    else:
        #在else中打印递归最后一行
        pb(k,V1,)
        pb(2*d*b-2*d,V2,)
        pb(k, V1, )
        print('')
        #在else中打印最长一行
        pb(2*d*b, V2,)
        print ('')
    pb(k, V1,)
    pb(2*d*b-2*d, V2,)
    pb(k, V1, )
    print ('')
if __name__ == '__main__':
    L=int(input('Enter length:'))
    W=int(input('Enter width:'))
    main(L,W)

