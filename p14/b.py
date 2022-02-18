from unidecode import unidecode

def make_valid(filename:str) -> str:
  special_char = '@!#$%^&*()<>?/\|}{~:;[]'
  for character in special_char:
    filename = filename.replace(character, "")
  strlist=[]
  strlist[:0]=filename
  for i in range(len(filename)):
    if strlist[0] in ["_", ".", "-"]:
      strlist.pop(0)
    if strlist[-1] in ["_", ".", "-"]:
      strlist.pop(-1)
  filename = ''.join(strlist)
  unidecode(filename)
  if len(filename) >2:
    return filename
  else:
    return 'understated'
 


print(make_valid('4432hghf--ds-'))
