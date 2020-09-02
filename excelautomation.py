# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:30:16 2020

@author: Mayank Tripathi
"""
#to import library
import numpy as np
import pandas as pd
#import os  
# to rename a file using os library
#os.rename('D:\\drive-download-20200411T200405Z-001\\tscautomation\\GG_ALL_Active_Windows_Server_Computers_and_Servers.csv','D:\\drive-download-20200411T200405Z-001\\tscautomation\\Physical Servers.csv')
# to read csv file.encoding is used to consider all types of symbols which will not be conisdered if we would use utf-8 default one.
dataset=pd.read_csv("D:\\excelautomation\\document1.csv",encoding='latin1')
dataset2=pd.read_csv("D:\\excelautomation\\document2.csv",encoding='latin1')
dataset3=pd.read_csv("D:\\excelautomation\\document3.csv",encoding='latin1')
dataset4=pd.read_csv("D:\\excelautomation\\document4.csv",encoding='latin1')
dataset5=pd.read_csv("D:\\excelautomation\\document5.csv",encoding='latin1')
dataset6=pd.read_csv("D:\\excelautomation\\document6.csv",encoding='latin1')
#x=dataset.iloc[:,[0]].values
#df.filter(["Name", "College", "Salary"])
#print(dataset.head(5))
#print(df[dataset['virtual']='true']);
#print(dataset.head(2))
#print(dataset.dtypes)
#print(df2.head(2).shape)
#this will return all records for which virtual column having value as true to df1 and to df2 for false. 
df1=dataset[dataset['virtual']]
df2=(dataset[dataset['virtual']==0])
#df4=dataset.iloc[:,[1,2]].values()
#print(df4.dtypes)
#print(df1.shape)
#print(df2.shape)
#df1.to_csv('D:\\drive-download-20200411T200405Z-001\\tscautomation\\Virtual Servers.csv');
#df2.to_csv('D:\\drive-download-20200411T200405Z-001\\tscautomation\\Physical Servers.csv');
#print(df2.head(2))
#df1.insert(7, "Cluster Name","",True)
#df1.insert(8, "Host Name","",True)
#print(dataset2.dtypes)
#print("end")
#print(df1.dtypes)
#print(df1.dtypes)
#print(df1.head(2))
#print(dataset2.head(2))
#to fetch some columns of a dataset and give it to dataframe.It will fetch all records and columns which are mentioned in [].
df10=dataset2.iloc[:,[1,2]]
#this will generate boolean value for all the records in a dataset.it will give false for first value of duplicate value and also for unique values.
#will give true for remaning values.
bool_series = df10['vmname'].duplicated(keep = 'first') 
  
# bool series 
#bool_series 
  
# passing NOT of bool series to see unique values only.

df10 = df10[~bool_series]
#print(len(df1.index))
#df3=pd.merge(df1,dataset2[['hostname','vmname']],on='vmname',how='left')
#merge is same like join operation in sql.
df6=pd.merge(df1,df10,on='vmname',how='left')
#print(len(df6.index))
#print(df3.head(2))
#print(df3.dtypes)
#print(df1.dtypes)
#df3.to_csv('D:\\drive-download-20200411T200405Z-001\\tscautomation\\temp.csv');
#print(df3['hostname'].head(2))
df13=dataset5.iloc[:,[0,1]]
df3=pd.merge(df6,df13,on='vmname',how='left')
#print(len(df3.index))
for ind in df3.index:
    #bgh=df4[''][ind]
    if(isinstance(df3['hostname'][ind],float) and not(isinstance(df3['Host Name'][ind],float))):
      drt=df3.loc[ind,'Host Name']
      #print(drt)
      #find return index of elemnet needed to be searched.It return -1 if it doesn't exist.
      inu=drt.find('.')
      if(inu!=-1):
      	#to create substring
        drt=drt[0:inu]
      else:
      	drt=df3.loc[ind,'Host Name']
      df3.loc[ind,'hostname']=drt 
df11=dataset3.iloc[:,[1,2]]
bool_series = df11['hostname'].duplicated(keep = 'first') 
  
# bool series 
#bool_series 
  
# passing NOT of bool series to see unique values only 
df11 = df11[~bool_series]
df5=pd.merge(df3,df11,on='hostname',how='left')
#print(len(df5.index))
#print(df4.dtypes)
df12=dataset4.iloc[:,[0,1]]
df4=pd.merge(df5,df12,on='clustername',how='left')
#print(df4.head(2))
#df4.to_csv('D:\\drive-download-20200411T200405Z-001\\tscautomation\\temp.csv');
#df4.set_index(['clustername','hostname'],append=True,drop=True)
#print(df4['os'].head(7))
#print(len(df4.index))
#df4=df4[['location.u_region','location.country','location','location.name','location.u_site_name','sys_class_name','clustername','hostname','vmname','virtual','os','os_version','u_os_version','cpu_type','cpu_name','ip_address','u_prod_status','u_discovered','manufacturer','model_id','cpu_manufacturer','cpu_count','cpu_core_count','ram','serial_number','last_discovered','sys_updated_on','sys_created_on','ref_cmdb_ci_server.u_not_a_server','ref_cmdb_ci_server.u_server_role']]
#df4.to_csv('D:\\drive-download-20200411T200405Z-001\\tscautomation\\temp.csv');
df4.insert(31, "Is OS Edition or Version is incomplete","",True)
df4.insert(32, "Is CPU count is blank or zero","",True)
df4.insert(33, "Is Cluster or Host name is missing","",True)
df4.insert(34, "Is all data available","",True)
#print(df4.head(2))
#print(df4['os'][185])
#print(df4['vmname'][185])
#print(df4.dtypes)
#df4['os'].fillna('',inplace=True)
#df4=pd.DataFrame(df4)
#dataset2.set_value(185,'os','NO')
#df4.fillna('')
#df4.to_csv('D:\\drive-download-20200411T200405Z-001\\tscautomation\\temp1.csv');
#print()
#print(df4.dtypes)
#df4.loc[1,'cpu_count']=0
#df4.loc[2,'cpu_count']=""
#df4.to_csv('D:\\drive-download-20200411T200405Z-001\\tscautomation\\temp2.csv');
for ind in df4.index:
  #if(ind==0 or ind ==1):
    flag=1  
    bgh=df4['os'][ind]
    #print(bgh)
    if(isinstance(bgh,float)):
      #print(ind)
      #df4=df4.at[ind,'Is OS Edition or Version is incomplete']='NO'
      #df4.set_value(df4.loc[ind],'Is OS Edition or Version is incomplete','NO')
      #df4.at[185,'Is OS Edition or Version is incomplete']='NO'
      #print(df4.iat[4,6])
      #df4.iat[4,6]
      #df4['Is OS Edition or Version is incomplete'][ind]='NO'
      #print(df4.loc[ind].at['Is OS Edition or Version is incomplete'])
      df4.loc[ind,'Is OS Edition or Version is incomplete']='NO'
      flag=0
      #df4.at[ind,'os']='NO'
      #print("here")
      #print(df4.loc[ind].at['Is OS Edition or Version is incomplete'])
    else:
      #print(ind)
      #df4['Is OS Edition or Version is incomplete'][ind]='YES'
      #df4.at[ind,'os']='YES'
      #df4.at[185,'Is OS Edition or Version is incomplete']='YES'
      #print(df4.at[ind,'Is OS Edition or Version is incomplete'])
      #print(df4.loc[ind].at['Is OS Edition or Version is incomplete'])
      df4.loc[ind,'Is OS Edition or Version is incomplete']='YES'
      #print(df4.loc[ind].at['Is OS Edition or Version is incomplete'])
      #print("here2")
    bgh=df4['cpu count'][ind]
    if(bgh==0 or pd.isnull(df4['cpu count'][ind])):
     df4.loc[ind,'Is CPU count is blank or zero']='NO'
     flag=0
    else:
     df4.loc[ind,'Is CPU count is blank or zero']='YES'
    bgh=df4['clustername'][ind]
    ghi=df4['hostname'][ind]
    if(isinstance(bgh,float) or isinstance(ghi,float)):
     df4.loc[ind,'Is Cluster or Host name is missing']='NO'
     flag=0
    else:
     df4.loc[ind,'Is Cluster or Host name is missing']='YES' 
    if(flag==0):
     df4.loc[ind,'Is all data available']='NO'
    else:
     df4.loc[ind,'Is all data available']='YES'
#df4['Is OS Edition or Version is incomplete'][ind]='NO'   
#else:
#df4['Is OS Edition or Version is incomplete'][ind]='YES'  
#df4.to_csv('D:\\drive-download-20200411T200405Z-001\\tscautomation\\Virtual Servers.csv')
#print(len(df4.index))
#print(df1.head(2))
df2.insert(28, "Is OS Edition or Version is incomplete","",True)
df2.insert(29, "Is CPU count is blank or zero","",True)
#df4.insert(32, "Is Cluster or Host name is missing","",True)
df2.insert(30, "Is all data available","",True)

#print(df1.dtypes)
for ind2 in df2.index:
  #if(index==185):
    flag=1  
    bgh=df2['os'][ind2]
    #print(bgh)
    if(isinstance(bgh,float)):
      #print(ind)
      #df4=df4.at[ind,'Is OS Edition or Version is incomplete']='NO'
      #df4.set_value(df4.loc[ind],'Is OS Edition or Version is incomplete','NO')
      #df4.at[185,'Is OS Edition or Version is incomplete']='NO'
      #print(df4.iat[4,6])
      #df4.iat[4,6]
      #df4['Is OS Edition or Version is incomplete'][ind]='NO'
      #print(df4.loc[ind].at['Is OS Edition or Version is incomplete'])
      df2.loc[ind2,'Is OS Edition or Version is incomplete']='NO'
      flag=0
      #df4.at[ind,'os']='NO'
      #print("here")
      #print(df4.loc[ind].at['Is OS Edition or Version is incomplete'])
    else:
      #print(ind)
      #df4['Is OS Edition or Version is incomplete'][ind]='YES'
      #df4.at[ind,'os']='YES'
      #df4.at[185,'Is OS Edition or Version is incomplete']='YES'
      #print(df4.at[ind,'Is OS Edition or Version is incomplete'])
      #print(df4.loc[ind].at['Is OS Edition or Version is incomplete'])
      df2.loc[ind2,'Is OS Edition or Version is incomplete']='YES'
      #print(df4.loc[ind].at['Is OS Edition or Version is incomplete'])
      #print("here2")
    bgh=df2['cpu count'][ind2]
    if(bgh==0 or pd.isnull(df2['cpu count'][ind2])):
     df2.loc[ind2,'Is CPU count is blank or zero']='NO'
     flag=0
    else:
     df2.loc[ind2,'Is CPU count is blank or zero']='YES'
    if(flag==0):
     df2.loc[ind2,'Is all data available']='NO'
    else:
     df2.loc[ind2,'Is all data available']='YES'
df2.insert(31, "License Product Family","",True)
df2.insert(32, "License Version","",True)
df2.insert(33, "License Quanity","",True)
#to arrange column in the way as required.
df4=df4[['Region','Country','Location','GSL Site ID','Site name','Class','clustername','hostname','vmname','virtual','os','os version','OS Version (Import)','cpu type','cpu name','IP Address','Production Status','Discovered?','Manufacturer','Model ID','CPU manufacturer','cpu count','cpu core count','RAM (MB)','Serial number','Most recent discovery','Updated','Created','This is not a Server [Server]','Server Role [Server]','DRS Status','Is OS Edition or Version is incomplete','Is CPU count is blank or zero','Is Cluster or Host name is missing','Is all data available']]
df7=df4[['clustername','hostname','vmname','os','os version','cpu count','cpu core count','DRS Status']]
#print(df11.dtypes)
df8=dataset3.iloc[:,[2,6,7]]
bool_series = df8['hostname'].duplicated(keep = 'first') 
df8 = df8[~bool_series]
#print(df8.dtypes)
df8=df8[['hostname','CPU count','CPU core count']]
df9=pd.merge(df7,df8,on='hostname',how='left')
df9=df9[['clustername','hostname','CPU count','CPU core count','vmname','os','os version','cpu count','cpu core count','DRS Status']]
df9=df9.sort_values(by=['clustername','hostname','vmname'])
#df14=df9.groupby(['clustername'])['hostname','CPU count','CPU core count','vmname','os','os version','cpu count','cpu core count','DRS Status'].apply(lambda x:x)
#print(df14.head(5))
#df9.iloc[:,[1,2,3,4,5,6,7,8,9]]=df14.iloc[:,[0,1,2,3,4,5,6,7,8]]
#print(df14.head(10))
#df14=df9.groupby(['clustername']).agg('hostname')
df9.insert(10, "License Product Family","",True)
df9.insert(11, "License Version","",True)
df9.insert(12, "License Quanity","",True)
for ind2 in df2.index:
    if(not(pd.isnull(df2['os'][ind2]))):
     bgh=df2['os'][ind2]
     inu=bgh.find("Windows")
     if(inu!=-1):
      sta=bgh.find("Standard")
      ent=bgh.find("Enterprise")
      data=bgh.find("Datacenter")
      if(sta!=-1 or ent!=-1 or data!=-1):
       if(sta!=-1):  
        df2.loc[ind2,'License Product Family']="Windows Standard"
        df2.loc[ind2,'License Version']=bgh[8:sta-1]+""+bgh[sta+8:len(bgh)]
       elif(ent!=-1):
        df2.loc[ind2,'License Product Family']="Windows "+"Enterprise"    
        df2.loc[ind2,'License Version']=bgh[8:ent-1]+""+bgh[ent+10:len(bgh)]
       else:
        df2.loc[ind2,'License Product Family']="Windows "+"Datacenter"    
        df2.loc[ind2,'License Version']=bgh[8:data-1]+""+bgh[data+10:len(bgh)]
      else:
       df2.loc[ind2,'License Product Family']="Windows"    
       df2.loc[ind2,'License Version']=bgh[8:len(bgh)]
     else:
      df2.loc[ind2,'License Product Family']=bgh

for ind2 in df9.index:
    if(not(pd.isnull(df9['os'][ind2]))):
     bgh=df9['os'][ind2]
     inu=bgh.find("Windows")
     if(inu!=-1):
      sta=bgh.find("Standard")
      ent=bgh.find("Enterprise")
      data=bgh.find("Datacenter")
      if(sta!=-1 or ent!=-1 or data!=-1):
       if(sta!=-1):  
        df9.loc[ind2,'License Product Family']="Windows Standard"
        df9.loc[ind2,'License Version']=bgh[8:sta-1]+""+bgh[sta+8:len(bgh)]
       elif(ent!=-1):
        df9.loc[ind2,'License Product Family']="Windows "+"Enterprise"    
        df9.loc[ind2,'License Version']=bgh[8:ent-1]+""+bgh[ent+10:len(bgh)]
       else:
        df9.loc[ind2,'License Product Family']="Windows "+"Datacenter"    
        df9.loc[ind2,'License Version']=bgh[8:data-1]+""+bgh[data+10:len(bgh)]
      else:
       df9.loc[ind2,'License Product Family']="Windows"    
       df9.loc[ind2,'License Version']=bgh[8:len(bgh)]
     else:
      df9.loc[ind2,'License Product Family']=bgh

df15=dataset6.iloc[:,[0,1,2,3,4,5,6,7,8]]
#print(df15.dtypes)
for ind2 in df15.index:
    if(not(pd.isnull(df15['License Product Family'][ind2])) and not(pd.isnull(df15['License Version'][ind2]))):
     count1=0
     count2=0	
     for ind3 in df2.index:
      if(not(pd.isnull(df2['License Product Family'][ind3])) and (df2['License Product Family'][ind3]==df15['License Product Family'][ind2]) and not(pd.isnull(df2['License Version'][ind3])) and (df2['License Version'][ind3]==df15['License Version'][ind2])):
       count1=count1+1
     df15.loc[ind2,'Physical']=count1
     for ind4 in df9.index:
      if(not(pd.isnull(df9['License Product Family'][ind4])) and (df9['License Product Family'][ind4]==df15['License Product Family'][ind2]) and not(pd.isnull(df9['License Version'][ind4])) and (df9['License Version'][ind4]==df15['License Version'][ind2])):
       count2=count2+1
     df15.loc[ind2,'Virtual']=count2
     df15.loc[ind2,'Total']=count1+count2
     if(df15.loc[ind2,'Livingstone Rights']>=df15.loc[ind2,'Total']):
      df15.loc[ind2,'Availability']=df15.loc[ind2,'Livingstone Rights']-df15.loc[ind2,'Total']
      df15.loc[ind2,'Compliance Status']="In Compliance"
     if(df15.loc[ind2,'Livingstone Rights']<df15.loc[ind2,'Total']):
      df15.loc[ind2,'Availability']=df15.loc[ind2,'Total']-df15.loc[ind2,'Livingstone Rights']
      df15.loc[ind2,'Compliance Status']="Not Compliant"
#df4.to_csv('D:\\tcsautomation\\Virtual Servers.csv',index=False)
#df2.to_csv('D:\\tcsautomation\\Physical Servers.csv',index=False)
#df9.to_csv('D:\\tcsautomation\\VM Calculation1.csv',index=False)
#df9[['cl']].dropduplicates(inplace==True)

#df14.to_csv('D:\\tcsautomation\\VM Calculation3.csv',index=False)
#df9.to_csv('D:\\tcsautomation\\VM Calculation4.csv',index=False)
#to remove index column from dataset.
df15.to_csv('D:\\tcsautomation\\Summary Sheet.csv',index=False)



