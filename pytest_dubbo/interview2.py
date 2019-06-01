
'''
n 为任意大于1的正整数

行数=输入的数
星号的个数
星号+空格=输入的数
前面空格的个数=后面空格的个数， 前面、后面空格数=（输入的数-星号个数）//2
'''
def print_img(n):
#前半部分
    for i in range(1,n+1,2):
        img=' '*((n-i)//2)  + '*' * i +' '*((n-i)//2)
        print(img)

    if n%2==0:
        s=n - 1
    else:
        s=n -2
    for i in range(s,0,-2):
        img = ' ' * ((n - i) // 2) + '*' * i + ' ' * ((n - i) // 2)
        print(img)

print_img(5)

