#  1  mutable
# 2 elemnts are stroe id pair ig "key " Value
# key= 1 immutble
#       2 unique
# values= all datat type
 

# create  empty dictinary
# dt={}
# dt1=dict()
# print(dt,dt1)


# dt={ 1:5,"hello":35,3.5:"python",7:4}
# print(dt)

 
# lst=[(2,5),(8,'hello'),(5,6.7),(4,6)]
# d=dict(lst)
# print(d)

# et=({23,4,5,34,5})
# s=set(et)
# print(s)


# dt={1:23,45:4,'hello':5.6,'hi':55,1:34,1:65}
# print(dt)
# print(dt['hello'])



# print(dt.keys())  # sari keys ko dekh sakht hai
# print(dt.values())  # value

# print(dt.items())  #key+value=items


#  teavers

dt={1:23,45:4,'hello':5.6,'hi':55,1:34,1:65}
# for k,v in dt.items():
#     print(k,v)

for k in dt.keys():
        print(k,dt[k])


dt={ 1:2,2:3,3:4,6:12,17:18,18:12}
for key in dt.keys():
        if int(key)%2==0:
              dt[key]-=5
        else:
               dt[key] +=5 


