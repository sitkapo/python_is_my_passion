def brace_scale(M:int):
  weights = [1,3,3]
  R=[M]
  L=[]
  weights.sort(reverse = True)
  index=0
  if M >7:
    print('too heavy')
  else:
    for i in weights:
      if M >3:
        M-=weights[index]
        L.append(weights[index])
        weights.pop(index)
      if M ==3:
        M-=weights[index]
        L.append(weights[index])
        weights.pop(index)
      # if R >2:
      #   R-=weights[index]
      #   L.append(weights[index])
      #   weights.pop(index)
      # if R==2:
      #   R-=weights[index]
      #   L.append(weights[index])
      #   weights.pop(index)
      # if R ==1:
      #   R-=weights[-1]
      #   L.append(weights[-1])
      #   weights.pop(-1)

    index+=1
    print(R)
    print(L)

brace_scale(3)
