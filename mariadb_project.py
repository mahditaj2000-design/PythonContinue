import mariadb as ma

def taker():

    while True:
        s = []
        d = []
        u = input("Pleas enter email: ")
        p = input("Pleas enter your password: ")

        for i in p:
            d.append(i.isalpha() == True)
            s.append(i.isdigit() == True)

        uu = u.find("@")

        if (uu == -1) or (uu == 0):
            print("Error: Email is not correct!")
            continue

        us = u[uu+1:]
        uuu = us.find(".")

        if (uuu == -1) or (us[0] == ".") or (u[-1] == "."):
            print("Error: Email is not correct!")
            continue

        elif (len(p) < 6) or (True not in d) or (True not in s):
            print("password is not correct")
            continue

        else:
            break
        
    return u , p
          
def database(u , p):
    con = ma.connect(
        host = "localhost",
        port = 3307,
        user = "root",
        password = "",
        database = "users"
    )
    
    crs = con.cursor()
    crs.execute("INSERT INTO users (username , password) VALUES (? , ?)" , (u , p))
    con.commit()
    print("username & password aded succesfuly!")

    crs.close()
    con.close()
             
u , p = taker()
database(u , p)     