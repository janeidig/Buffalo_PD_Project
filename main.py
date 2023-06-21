import bottle
import os.path
import data
import process
import csv
import json

@bottle.route('/')
def index():
   return bottle.static_file("index.html", root=".")

@bottle.route('/frontend.js')
def frontEnd():
  return bottle.static_file("frontend.js", root = ".")

@bottle.route('/ajax.js')
def ajax():
  return bottle.static_file("ajax.js", root = ".")

@bottle.get('/barGraph')
def barGraph():
  sepData=data.load_data("saved_data.csv")
  newDic=process.gen_dictionary(sepData,"year")
  yearTally=process.yearAccum(sepData,newDic)
  yearTally=process.remove_min(yearTally,20)
  dic=sorted(yearTally)
  sortedDic={key:yearTally[key] for key in dic}
  return json.dumps(sortedDic)
  
@bottle.get('/pieChart')
def pieChart():
  #set up accum for incidents per day of the week
  Monday = 0
  Tuesday = 0
  Wednesday = 0
  Thursday = 0
  Friday = 0
  Saturday = 0
  Sunday = 0
  with open("saved_data.csv") as f:
    reader = csv.reader(f)
    headers = next(f)
    #accum number of incidents per day
    for line in reader:
      if line[4] == "Monday":
        Monday += 1
      if line[4] == "Tuesday":
        Tuesday += 1
      if line[4] == "Wednesday":
        Wednesday += 1
      if line[4] == "Thursday":
        Thursday += 1
      if line[4] == "Friday":
        Friday += 1
      if line[4] == "Saturday":
        Saturday += 1
      if line[4] == "Sunday":
        Sunday += 1
    data = [Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday]
  return json.dumps(data)

@bottle.post('/lineChart')
def lineChart():
  dataJSON = bottle.request.body.read().decode()
  content = json.loads(dataJSON)
  finalVal={}
  retVal=[]
  with open("saved_data.csv") as f:
    reader = csv.reader(f)
    headers = next(f)
    for line in reader:
      if line[2] == content["line"]:
        retVal.append(line)
    retVal.sort()
    for lis in retVal:
      if lis[0] not in finalVal:
        finalVal[lis[0]]=1
      else:
        finalVal[lis[0]]+=1
  return json.dumps(finalVal)

#given function to pull BPD data and call to function
def startup():
  csv_file = 'saved_data.csv'
  if not os.path.isfile(csv_file):
    url = 'https://data.buffalony.gov/resource/d6g9-xbgu.json?$limit=50000'
    info = data.json_loader(url)
    data.fix_data(info,"incident_datetime")
    heads = ['year','month','hour_of_day','incident_type_primary','day_of_week']
    data.save_data(info, heads, csv_file)

startup()

bottle.run(host="0.0.0.0", port=8080)