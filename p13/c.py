# # def dominoes(str, list:str):

# #     list.sort()
# #     for i in list:
        
        


# # dominoes('A',['AA','AC','BC','CA'])

# list=['AA','AC','BC','CA']
# # print(list[1])
# index =0
# for i in range(len(list)):
#     index+=1
#     # print(index,list[i])
#     for i in list[i]:
#         print(index,i)
    
# print(index)
#     # for i in list[i]:
#     #     print(i)


def dominoes(str, list:str):
    index =0
    for i in range(len(list)):
        index+=1
        # print(index,list[i])
        for i in list[i]:
            print(index,i)
            



dominoes('A',['AA','AC','BC','CA'])