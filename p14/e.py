def get_current_limit(signs: list[int]) -> int:
  ngtv=[]
  pstv = []
  for i in signs:
    if i < 0:
      ngtv.append(i)
    if i > 0:
      pstv.append(i)
  ngtv=[element * -1 for element in ngtv]
  for i in ngtv:
    if i in pstv:
      pstv.remove(i)
  if not pstv:
    print(50)
  else:
    print(pstv[-1])

get_current_limit([20, 40, 60, -60, -40])
