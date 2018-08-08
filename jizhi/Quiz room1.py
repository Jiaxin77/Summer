def sum_of_multiples(number):

    # sum_of_multiples(10) 应该返回 23
    sum=0
    for i in range(1,number):
        if i%3==0 or i%5==0:
            sum+=i
    # >>>> show..me...the...code <<<<

    return sum

    # >>>> show..me..th... <<<<
#判断元音字母

    def letter_counts(input_str):


    # letter_counts('abcdefgABCDEFG') 应该返回 4
    print(input_str)
    count=0
    # >>>> show me the code <<<<
    for i in input_str.lower():
        print(i)
        if  i in "aeiou" :#用字符串包含来判断。为什么使用i == "a" or "e"的方式会把所有字符都进入判断？
            count+=1
        else:
            count
    print(count)
    return count

    # >>>> show me the code <<<<
#rgb转换
    def rgb_to_hex(r,g,b):

    # rgb_to_hex(255, 255, 255) 应该返回 'FFFFFF'
    # rgb_to_hex(0, 0, 0) 应该返回 '000000'
    # >>>> what color? <<<<
    output_str=""
   # output_str=hex(r)+hex(g)+hex(b)
    output_str="{:02X}".format(r)+"{:02X}".format(g)+"{:02X}".format(b)
    print(output_str)
    output_str=output_str.upper()
    return output_str

    # >>>> wc? <<<<


#判断是否可以整除，看注释
    def dig_pow(n, p):

    # dig_pow(89, 1) 返回 1，因为 8¹ + 9² = 89，89 / 89 == 1
    # dig_pow(695, 2) 返回 2，因为 6² + 9³ + 5⁴= 1390，1390 / 695 == 2
    # dig_pow(46288, 3) 返回 51 因为 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688，2360688 / 46288 == 51
    # 如果不能整除，返回 -1

    # >>>> show me the code <<<<
    #字符串转列表
    #q=n
    #basic_lst=[]
    #zero=0
   # while q>=0:
    #    basic_lst.append(q%10)
    #    q=q/10
   # in_list = list(reversed(basic_lst))
    #print(basic_lst)
    #print(in_list)
    #x=p
    #count=0
    #for i in in_lst:
     #   count+=i**x
    #if count%n==0:
     #   return count/n
    #else:
     #   return -1
    print(n)
    count=0
    for index,basic in enumerate(str(n)):
        print(index)
        print(basic)
        count+=int(basic)**(index+p)
        print (count)
    if count%n==0:
        return count/n
    else:
        return -1

    # >>>> show me the code <<<<


 

    #返回数字排列最大的数 如126->621

    def biggest(n):
    print(n)
    #str_lst=(r%10 while r>0)
    r=n
    str_lst=[]
    while r>0:
        str_lst.append(r%10)
        r=r-r%10
        r=int(r/10)
    # >>>> show me the password <<<<
    print(str_lst)
    str_str=''.join(str(str_lst))
    #str_sort=str_lst.sorted()#从小到大排序
    str_sort=sorted(str_lst)
    count=0
    print(str_sort)
    for index,basic in enumerate(str_sort):
        print(index,basic)
        
        count=count+int(basic)*(10**int(index))
        print(count)
    print(count)
    
    return count
    # >>>> show me the password <<<<
    #answer

    def biggest(n):

    big = sum(j * 10**i for i,j in enumerate(sorted([int(i) for i in str(n)])))
    # big = int(''.join(str(i) for i in sorted([int(i) for i in str(n)], reverse=True)))

    return big




    #返回next bigger
    def next_bigger(number):

    # next_bigger(1024) -> 1042
    # next_bigger(1234567980) -> 1234568079
    # next_bigger(9876) -> 9876 9786
    # >>>> show me the code <<<<
    def next_bigger(number):

    nb = str(number)

    try:
        idx_low = [i-1 for i in range(len(nb)-1, 0, -1) if nb[i] > nb[i-1]][0]
        idx_high = idx_low + nb[idx_low:].index([x for x in nb[idx_low:] if x > nb[idx_low]][-1])

        nb_lst = list(nb)
        nb_lst[idx_low], nb_lst[idx_high] = nb_lst[idx_high], nb_lst[idx_low]

        return int(''.join(nb_lst[:idx_low+1] + nb_lst[:idx_low:-1]))

    except IndexError:
        return number



    # >>>> show me the code <<<<