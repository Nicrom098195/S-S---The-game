import os

directory = 'assets/swords'  # Replace with the actual directory path
cds={}


# Get all files in the directory
file_list = []
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(file)
        file_list.append(file_path)
        print("Now making",file.replace(".png",""))
        name=file.replace(".png","")
        life=input("Life: ")
        tp=input("Type [1:sword|0:shield]: ")
        cds[file]={}
        if int(tp) == 1:
            attack1=input("Attack 1: ")
            atval1=input("Attack 1 value: ")
            attack2=input("Attack 2: ")
            atval2=input("Attack 2 value: ")
            cds[file]["name"]=name
            cds[file]["life"]=life
            cds[file]["tp"]=1
            cds[file]["attack1"]=attack1
            cds[file]["atval1"]=atval1
            cds[file]["attack2"]=attack2
            cds[file]["atval3"]=atval2
        else:
            defval=input("Defense value:")
            cds[file]["name"]=name
            cds[file]["life"]=life
            cds[file]["tp"]=0
            cds[file]["defval"]=defval


print(cds)

