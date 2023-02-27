import os
import platform
#print(os.name)
#print(platform.uname())
print(os.getcwd())
path=os.path.join(os.getcwd(),"CursoPython")
print(path)
print(os.path.split(os.getcwd()))
print(os.path.isfile(os.path.join(os.getcwd(),"Alumnos.py")))
print(os.listdir(path))
os.chdir("../")
#os.mkdir("test1")
os.listdir(path)



