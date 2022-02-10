
# number = str('123')
# w =[]
# for i in number:  
#     w.append(i)
#     # back_number=int(i)
#     # now_number=int(i)
#     for i in w:
#         x = w[i:i+1]
# print(w)
# A = [1, 2, 3, 4, 5]
# for i in range(len(A) - 1):
#     value = A[i:i+2]

# print(value)


# print(back_number)
# print(good_number)


w =[1,20,3]
q = []
for i in w:
    x = w[i:i+1]
    for k in x:
        c=k
        y = c+i
        q.append(y)
        max = q[0]
        for i in range(len(q)):
            if q[i] > max:
                max = q[i]
                print(max)