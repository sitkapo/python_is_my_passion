def see_mountain():
  D=[1,2,4,8,16]
  H=[5,5,24,80,160]
  S=[]
  index=0
  S.append(H[0])
  for i in range(len(D)-1):
    if D[index+1] >= 2*D[index]:
      if H[index+1] >2* H[index]:
        S.append(H[index+1])
    index+=1
  print(S)
see_mountain()