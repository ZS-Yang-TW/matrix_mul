from ConnectDatabase import database

# db = database()
# db.connect()
# R_M3=[[0,0,0],[0,0,0],[0,0,0]]
# R_M3_get = db.select_last()

# for i in range(3):
#     R_M3[i] = R_M3_get[i].split(",")


# print(R_M3[2][2])

db = database()
db.connect()
R_M3={"1strow":list,"2ndrow":list,"3rdrow":list}
R_M3_get = db.select_last()

R_M3["1strow"] = R_M3_get[0].split(",")
R_M3["2strow"] = R_M3_get[1].split(",")
R_M3["3strow"] = R_M3_get[2].split(",")


print(R_M3["1strow"][0])
print(type(R_M3))

