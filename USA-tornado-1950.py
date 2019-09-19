# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/USA-tornado-1950.csv',encoding="cp1252")

print("\n------- output data :-----------\n")
print("USA Tornado data analysis:")
print("\n-----------------------------------\n")

# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")


#---------- Question-1 : statewise no. of Tornados in 1950 ----------------

df_states = df.groupby(['STATE'])[['YEAR']].count()
print(df_states)
print("\n-------------------------------------------\n")

print('Total no. of Tornados in USA (1950) :',sum(df_states))
print("\n-------------------------------------------\n")

plt.title("[Question-01] Statewise No. of Tornados in 1950")
plt.xlabel('State sl. no. -->')
plt.grid(True)
plt.ylabel('No. of tonados -->') 
plt.hist(df['STATE_FIPS'])
plt.show()

#---------- Question-2 : Monthwise analysis --------

df_months = df.groupby(['MONTH_NAME'])[['YEAR']].count()
print(df_months)

#---------- Question-3 : starting point(latitute and longitude)------

df_begin_lat = df['BEGIN_LAT']
df_begin_lon = df['BEGIN_LON']
df_end_lat = df['END_LAT']
df_end_lon = df['END_LON']

print(df_begin_lat)
print(df_begin_lon)
print(df_end_lat)
print(df_end_lat)

plt.title("[ Question - 3 ] : Tornado starting and ending point plotting")
plt.xlabel("latitude --->")
plt.ylabel("longitude --->") 
plt.scatter(df_begin_lat,df_begin_lon,label="Starting points")
plt.scatter(df_end_lat,df_end_lon,label="Ending points")
plt.legend()
plt.show()

#----------- Question-4 : Tornado details ------------------

df_begin_date = df['BEGIN_DATE_TIME']
df_end_date = df['END_DATE_TIME']

df_length = df['TOR_LENGTH']
df_width = df['TOR_WIDTH']

df_begin_lat = df['BEGIN_LAT']
df_begin_lon = df['BEGIN_LON']

df_end_lat = df['END_LAT']
df_end_lon = df['END_LON']

df_property = df['DAMAGE_PROPERTY']

print("-------- Tornado Details --------\n")

for i in range(0,223) :
    print("\n-------- Tornado : ",i+1,"----------\n")
    print("[A-1] Begining Date & Time : ",df_begin_date[i])
    print("[A-2] Ending Date & Time : ",df_end_date[i])
    
    print("\n[B-1] Tornado length : ",df_length[i])
    print("[B-2] Tornado width : ",df_width[i])
    
    print("\n[C-1] Begining latitude : ",df_begin_lat[i])
    print("[C-2] Begining longitude : ",df_begin_lon[i])
    print("[C-3] Ending latitude : ",df_end_lat[i])
    print("[C-4] Ending longitude : ",df_end_lat[i])
    
    print("\n[D-1] Damaged Property Cost : ",df_property[i])

#----------- Question-5 : Injuries direct and indirect ------

df_injuries_direct = df['INJURIES_DIRECT']
df_injuries_indirect = df['INJURIES_INDIRECT']

print(df_injuries_direct)
print(df_injuries_indirect)

plt.title("[ Question - 5 ] : Direct & Indirect injuries")
plt.xlabel("sl. no. of tornadoes --->")
plt.ylabel("no. of injuries --->") 
plt.plot(df_injuries_direct,label="Direct")
plt.plot(df_injuries_indirect,label="Indirect")
plt.legend()
plt.show()

#----------- Question-6 : Deaths direct and indirect ------

df_deaths_direct = df['DEATHS_DIRECT']
df_deaths_indirect = df['DEATHS_INDIRECT']

print(df_deaths_direct)
print(df_deaths_indirect)

plt.title("[ Question - 6 ] : Direct & Indirect deaths")
plt.xlabel("sl. no. of tornadoes --->")
plt.ylabel("no. of deaths --->") 
plt.plot(df_deaths_direct,label="Direct")
plt.plot(df_deaths_indirect,label="Indirect")
plt.legend()
plt.show()

#-