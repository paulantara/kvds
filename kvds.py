import json
def fileExist(filename):
  try:
    f=open(filename,'r+')
    f.close()
    return True
  except:
    return False

class KVDS:
  def __init__ (self,filename,user='',password=''):
    extenderFilename= filename+ '.json'
    if (fileExist(extendedFilename)):
      f=open(extendedFilename,)
      data=json.load()
      if(data['setup']['user']==user and data['setup']['password']==password):
         self.__filePath = extendedFilename
      else:
        raise Exception('Access Denied')
    else:
      f=open(extendedFilename,'w+')
      setup={
          "setup":{
              "user":user,
              "password":password
          },
          "data":{
              
          }
      }
      json.dump(setup,f,indent=4)
      self.__filePath = filename+'.json'
      f.close()

def insert(self,key,data):
  f =open(self, __filePath, 'r+')
  loaded_data = json.load(f)
  f.close()
  loaded_data['data'][key]=data
  f=open(self,__filePath,'w+')
  json.dump(loaded_data,f,indent=4)
  f.close()


def select(self,key):
  f=open(self,__filePath, 'r+')
  data=json.load(f)
  f.close()
  try:
    return data['data'][key]
  except:
    raise KeyError("Attribute not found")

def delete(self,key):
  f=open(self. __FilePath,)
  loaded_data=json.load(f)
  f.close()
  try:
    del loaded_data['data'][key]
  except:
    raise KeyError("Attribute not found")

