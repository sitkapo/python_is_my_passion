# # def dominoes(str, list:str):

# #     list.sort()
# #     for i in list:
        
        


# # dominoes('A',['AA','AC','BC','CA'])

list=['AA','AC','BC','CA']
# print(list[1])
# index =0
# for i in range(len(list)):
#     index+=1
#     # print(index,list[i])
#     for i in list[i]:
#         print(index,i)
    
# print(index)
#     # for i in list[i]:
#     #     print(i)


# def dominoes(str, list:str):
#     index =0
#     for i in range(len(list)):
#         index+=1
#         # print(index,list[i])
#         for i in list[i]:
#             print(i)



            



# dominoes('A',)

# def compare(a, b):
#     w=['A']
#     for x, y in zip(a, b):
#         if x == y:
#             w.append(b)
#     print(w)

# compare('AC', 'CA')

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1
# Driver code
str1="AA"
# print(Convert(str1))

list=['AA','AC','BC','CA']


# def domino(list):
#     w=[]
#     s=[]
#     index =0
#     for i in list:
#         list1=[]
#         list1[:0]=i
#         w.append(list1)
#     for i in range(len(w)):
#         
#         s.append(w[i])
#         if s[0][1]==s[1][0]:
#             print(s[0],s[1])
    

# domino(['AA','AC','BC','CA'])

# index=0
# for i in list:
#     print(i[index])

def domino(list):
    w=[]
    d=[]
    index =0
    for i in list:
        list1=[]
        list1[:0]=i
        w.append(list1)
    s=[w[index]]
    for i in range(len(w)-1):
        if s[index][1]==w[index+1][0]:
            # print(w[index])
            s.append(w[index+1])
        else:
            d.append(w[index+1])
        index+=1
    print(s)

domino(['AA','AB','BC','CA','AB'])
        # else:
        #     pass
    # print(w)

# def domino(list):
#     w=[]
#     s=[]
#     index =0
#     for i in list:
#         list1=[]
#         list1[:0]=i
#         w.append(list1)
#     print(w)
#     for i in range(len(w)-1):
#         if w[index][1]==w[index+1][0]:
#             s.append(w[index+1])
#         index+=1
#     print(s)
            
        
#         # else:
#         #     pass
#     # print(w)
            




