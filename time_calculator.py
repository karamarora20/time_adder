def add_time(start, duration, day=""):
      # new_time= start+duration
  if(duration=="0:00"):
      return start
  time= simplify_time(start)#
  time_val=time.split(":")#
  extra_time=duration.split(':')#
  extra_days=0
  day=day.lower()#empty
  final_time=[]
  week=['','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
  for i in range(8):
    if(week[i]==day):
      days=i#0
  
  hours=int(time_val[0])#

  minutes=int(time_val[1])#
  hours_add=int(extra_time[0])#

  minutes_add=int(extra_time[1])#
  new_hour= hours+hours_add#35
  
  
  new_minute= minutes+minutes_add#63
  if(new_minute>59):
      new_minute-=60#3
      new_hour+=1#36

  if(new_hour>24):
      extra_days=new_hour//24#2
      new_hour=new_hour%24#12
      
      
  days=days+extra_days#20
  final_time.append(new_hour)#
  final_time.append(new_minute)#
  dayss= str(extra_days) #string for number of days
  if(days>7 and day!=''):
      day= week[days%7].capitalize()
  elif(day!=''):
      day= week[days].capitalize()
  answer=encode_time(final_time)
      
  
  if(day!=''):#day given
          if(extra_days>1):
              new_time=answer+', '+day+' ('+dayss+' days later)'
          elif(extra_days==1):
              new_time=answer+', '+day+' (next day)'  
          else:
              new_time=answer+', '+day
  else:#day not given
          if(extra_days>1):
              new_time=answer+' ('+dayss+' days later)'
          elif(extra_days==1):
              new_time=answer+' (next day)'
          else:
              new_time=answer
                
      
      

  print(new_time)  
  return new_time
    
    
  
  





def simplify_time(start):
  time= start.split(" ")#11:43, PM
  time_val=time[0].split(":")# time_val[0] is 11 and 43 is minutes 
  if(time[1]=='AM'):
    time[0]= time_val[0]+':'+time_val[1]#time[0]= 11:43 for 11:43 AM
  elif(time[1]=='PM'):
    time[0]= str(int(time_val[0])+12)+':'+time_val[1]# 
  return time[0]
def encode_time(time):#time=[12,3]
  hours=time[0]
  minutes=time[1]
  if(hours>12):
      if(minutes>9):
          new_time=str(hours-12)+':'+str(minutes)+' PM'
      else:
          new_time=str(hours-12)+':0'+str(minutes)+" PM"
  elif(hours==12):
      if(minutes>9):
          new_time='12:'+str(minutes)+" PM"
      else:
          new_time='12:0'+str(minutes)+" PM"
  elif(hours>0 and hours <12):
      if(minutes>9):
          new_time=str(hours)+':'+str(minutes)+" AM"
      else:
          new_time=str(hours)+':0'+str(minutes)+" AM"
  else:
      if(minutes>9):
          new_time='12:'+str(minutes)+" AM"
      else:
          new_time='12:0'+str(minutes)+" AM"
      
    
  return new_time