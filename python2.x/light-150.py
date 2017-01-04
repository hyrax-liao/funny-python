#!/usr/bin/python
# -*- coding:utf-8 -*-
'''150盏灯的问题,定义数组，使用异或预算 ^ 不存在 0 ^ 0 情况'''
def change_status(L,n):
    m = len(L)/n
    for i in  range(m):
        L[(i+1)*n-1] ^= 1
    #print L
def main():
    L = [ 1 for raw in range(150) ]
    change_status(L,3)
    change_status(L,5)
    #print L
    print sum(L)

if __name__ == '__main__':
    main()

