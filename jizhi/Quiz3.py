#判断括号数目是否相同以及位置是否正确
def valid_parentheses(input_str):

    # valid_parentheses("hi(hi)(hi") -> False
    # valid_parentheses("((hei())hei()()hei)") -> True
    # >>>> show me the code <<<<
    print(input_str)
    count=0
    #right_count=0
    for i in input_str:
        if i=='(' or i==')':
            if i=='(':
                count+=1
           
            else: #i==")":
                if count==0:
                    return False
                else:
                    count-=1
           
    #print(left_count,right_count)
    print(count)
    if count==0:
        return True
    else:
        return False





    # >>>> show me the code <<<<

#不同的括号统计
    def valid_braces(input_str):  

    # valid_braces("())({}}{()][][") -> False
    # valid_braces("(({{[[]]}}))") -> True
    # >>>> show me the code <<<<
    



    # valid_parentheses("hi(hi)(hi") -> False
    # valid_parentheses("((hei())hei()()hei)") -> True
    # >>>> show me the code <<<<
    print(input_str)
    l_count=0
    m_count=0
    b_count=0
    #right_count=0
    for i in input_str:
        if i in "()[]{}":
            if i=='(':
                l_count+=1
            elif i=='[':
                m_count+=1
            elif i=='{':
                b_count+=1
            elif i==')':
                if l_count==0:
                    return False
                else:
                    l_count-=1
            elif i==']':
                if m_count==0:
                    return False
                else:
                    m_count-=1
            else:
                 if b_count==0:
                    return False
                 else:
                    b_count-=1
           
    #print(left_count,right_count)
    #print(count)
    if l_count==0 and m_count==0 and b_count==0:
        return True
    else:
        return False





    # >>>> show me the code <<<<

    # >>>> show me the code <<<<

    #答案用的stack和字典

    def valid_braces(input_str):  

    left = ["[", "{", "("]
    right = {"]":"[", "}":"{", ")":"("}

    stack = []


    try:
        for i in input_str:

            if i in left:
                stack.append(i)

            if i in right:

                if stack[-1] == right[i]:
                    stack.pop()

                else:
                    return False
                    break

    except IndexError:
        return False

    return stack == []

#螺旋读取矩阵  【不是很懂！！！】
    def snail(input_arr):

    '''
    snail([[1, 2, 3],  
           [4, 5, 6],
           [7, 8, 9]]) -> [1, 2, 3, 6, 9, 8, 7, 4, 5] 
    '''
    # >>>> show me the code <<<<

    output_arr = []

    while input_arr:

        output_arr.extend(input_arr.pop(0))

        tmp_arr = []
        #不太懂？
        for i in zip(*input_arr):
                tmp_arr.append(list(i))

        input_arr = tmp_arr[::-1]
   
    print(output_arr)
    return output_arr


    # >>>> show me the code <<<<



#螺旋丸转01，答案的，但是一直报错
    import numpy as np

def spiralize(size):

 
    spiral_3 = np.array([[1,1,1],
                         [0,0,1], 
                         [1,1,1]])

    spiral_4 = np.array([[1,1,1,1], 
                         [0,0,0,1], 
                         [1,0,0,1], 
                         [1,1,1,1]])

    if size == 3:
        return spiral_3 

    if size == 4:
        return spiral_4 

    else:

        sp_arr = np.zeros((size, size))
        sp_arr[0,:] = 1
        sp_arr[1:,-1] = 1
        sp_arr[-1,-2] = 1

        sp_arr[2:,:-2] = spiralize(size-2)[::-1, ::-1]

        return sp_arr
    # >>>> show me the code <<<<