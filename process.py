#functions from parts 1
def gen_dictionary(data,str):
  new_dic = {}
  for key in data:
    if str in key:
      v = key[str]
      new_dic[v] = 0
  return (new_dic)

def total_matches(lod,k,v):
  accum = 0
  for value in lod:
    if k in value:
      if value[k] == v:
        accum += 1
  return accum

def total_matches_specific(lod,k,v,k2,v2):
  accum2 = 0
  for value in lod:
    if k in value:
      if (value[k] == v) and (value[k2] == v2):
        accum2 += 1
  return accum2

def remove_min(data,int):
  min_dic = {}
  for key in data:
    if data[key] > int:
      min_dic[key] = data[key]
  return min_dic

def yearAccum(lod,lod2):
  for key in lod2:
    for dic in lod:
      if key in dic["year"]:
        lod2[key]+=1
  return lod2