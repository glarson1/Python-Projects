import os,sys,time

path = "C:\\Users\\gabri\\OneDrive\\Documents\\Script_Challenge"

dirs = os.listdir(path)


array = []
for file in dirs:
        if file.endswith(".txt"):
            modification_time = os.path.getmtime(path)
            local_time = time.ctime(modification_time)
            array.append(file)
            print(os.path.join(path,file), local_time)

            
        
