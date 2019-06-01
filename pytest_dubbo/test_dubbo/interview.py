import string
import re
print(string.digits)
print(string.ascii_letters)
print(string.punctuation)

def find(s):
    digital = []
    letters = []
    pun = []
    chinese = []
    for ss in s:
        if ss in string.digits:
            digital.append(ss)
        elif ss in string.ascii_letters:
            letters.append(ss)
        elif ss in string.punctuation:
            pun.append(ss)
        else:
           chinese.append(ss)
    print('数字是：{}'.format(''.join(digital)))
    print('符号是：{}'.format(''.join(pun)))
    print('英文是：{}'.format(''.join(letters)))
    print('中文是：{}'.format(''.join(chinese)))

def find_by(s):
    pa={"数字":"\d","英文":'[a-zA-Z]','中文':'[\u4e00-\u9fff]'}
    # if re.search('\d',s):
    #     t=re.findall('\d',s)
    #     s=re.sub('\d','',s)
    #     print(s)
    # if re.search('[a-zA-Z]',s):
    #     t=re.findall('[a-zA-Z]',s)
    #     s=re.sub('[a-zA-Z]','',s)
    #     print(s)
    for k,v in pa.items():
        ss=re.findall(v,s)
        print(k + ':'+''.join(ss))
        s=re.sub(v,'',s)
    print('符号：{}'.format(s))

if __name__ == '__main__':
    sun='wc,mxc,woajjksd12233j@#钟会'
    # find(sun)
    find_by(sun)