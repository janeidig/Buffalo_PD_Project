import csv
import json
import urllib.request

#functions from part 2,3

def split_date(date):
  dateList=[]
  sub = date.split('-')
  dateList.append(int(sub[0]))
  dateList.append(int(sub[1]))
  return dateList

def fix_data(lod,k):
  for dic in lod:
    if k in dic.keys():
      newV = split_date(dic[k])
      dic['year']=newV[0]
      dic['month']=newV[1]
  return lod

def json_loader(url):
  response=urllib.request.urlopen(url)
  content=response.read().decode()
  data=json.loads(content)
  return data

def make_values_numeric(keys,dic):
  for k in keys:
    dic[k]=float(dic[k])
  return dic 
      
def save_data(lod,keys,filename):
  f = open(filename,"w")
  writer=csv.writer(f)
  writer.writerow(keys)
  for dic in lod:
    list=[]
    for key in keys:
      list.append(dic[key])
    writer.writerow(list)

def load_data(file):
  f=open(file,"r")
  data=csv.reader(f)
  header=next(data)
  retList = []
  for line in data:
    newDic={}
    for l in range(len(line)):
      newDic[header[l]]=line[l]
    retList.append(newDic)
  return retList

def list_dic_gen(list, list2):
  finalList = []
  for x in list2:
    newDict={}
    for index in range(len(list)):
      newDict[list[index]] = x[index]
    finalList.append(newDict)
  return finalList

def read_values(file):
  f = open(file)
  reader = csv.reader(f)
  next(reader)
  newList = []
  for line in reader:
    newList.append(line)
  return(newList)

def list_gen(listD,listS):
  finalList = []
  for key in listD:
    subList = []
    for value in listS:
      subList.append(key[value])
    finalList.append(subList)
  return finalList

def write_values(list,file):
    f = open(file,'a')
    writer = csv.writer(f)
    for line in list:
        writer.writerow(line)