# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
#print(data)
census=np.concatenate((data,new_record),axis=0)
#print(np.shape(census))
#print(census)
age=np.array(census[0:len(census),:1]),
#print(age)
max_age=int(np.max(age))
min_age=int(np.min(age))
age_mean=round(np.mean(age),2)
age_std=round(np.std(age),2)

#print(int(max_age),int(min_age),round(age_mean,2),round(age_std,2),sep=",")
race_0=[]
race_1=[]
race_2=[]
race_3=[]
race_4=[]
for i in range(len(census)):
    if census[i:i+1,2:3]==0:
        race_0.append(0)
    if census[i:i+1,2:3]==1:
        race_1.append(1)
    if census[i:i+1,2:3]==2:
        race_2.append(2)
    if census[i:i+1,2:3]==3:
        race_3.append(3)
    if census[i:i+1,2:3]==4:
        race_4.append(4)
race_0=np.asarray(race_0)
race_1=np.asarray(race_1)
race_2=np.asarray(race_2)
race_3=np.asarray(race_3)
race_4=np.asarray(race_4)
#print(race_0,race_1,race_2,race_3,sep="-")
len_0=len(race_0)   
len_1=len(race_1)   
len_2=len(race_2)   
len_3=len(race_3)   
len_4=len(race_4)   

#print(len_0,len_1,len_2,len_3,len_4,sep="-")

race_len=[len_0,len_1,len_2,len_3,len_4]
minority_race=race_len.index(min(race_len))
#print(minority_race)


senior_citizens=[]
for i in range(len(age[0])):
    if age[0][i]>60:
        senior_citizens.append(age[0][i])
senior_citizens=np.asarray(senior_citizens)
#print(senior_citizens)

senior_citizens_len=len(senior_citizens)

working_hours_sum=0
for i in range(len(age[0])):
    if census[i:i+1,:1] in senior_citizens:
        working_hours_sum=working_hours_sum+census[i:i+1,6:7]

#print(working_hours_sum[0][0])
working_hours_sum=int(working_hours_sum[0][0])

avg_working_hours=round(working_hours_sum/senior_citizens_len,2)
print(avg_working_hours)


high=[]
low=[]
for i in range(len(census)):
    if census[i:i+1,1:2]<=10:
        low.append(census[i:i+1,1:2])
    else:
        high.append(census[i:i+1,1:2])
#print(high,low,sep="-")
high=np.asarray(high)
low=np.asarray(low)
#print(high,low,sep="-")

avg_pay_high=[]
avg_pay_low=[]
for i in range(len(census)):
    if census[i:i+1,1:2] in high:
        avg_pay_high.append(census[i:i+1,7:8])
    else:
        avg_pay_low.append(census[i:i+1,7:8])

avg_pay_high=np.asarray(avg_pay_high)
avg_pay_high=round(np.mean(avg_pay_high),2)


avg_pay_low=np.asarray(avg_pay_low)
avg_pay_low=round(np.mean(avg_pay_low),2)

#print(avg_pay_high,avg_pay_low)









