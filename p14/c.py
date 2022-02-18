def brace_scale(M:int):
  weights = [1,2,2,4]
  R=[M]
  L=[]
  weights.sort(reverse = True)
  index=0
  if M >8:
    print('too heavy')
  else:
    for i in weights:
      if M >4:
        M-=weights[index]
        L.append(weights[index])
        weights.pop(index)
      if M <4:
        weights.pop(index)
      if M >2:
        M-=weights[index]
        L.append(weights[index])
        weights.pop(index)
      if M==2:
        M-=weights[index]
        L.append(weights[index])
        weights.pop(index)
      if M ==1:
        M-=weights[-1]
        L.append(weights[-1])
        weights.pop(-1)

    index+=1
    print(R,L)

brace_scale(8)
