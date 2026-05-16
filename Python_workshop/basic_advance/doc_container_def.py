import os #import is used to bring a module/library into your Python program.
def docker_status():  #Colon means:"Start of function block" Everything indented below belongs to this function.
    os.system("docker ps") #system() is a function inside the os module.It executes Linux/shell commands.

docker_status() #This calls the function.Creating a function is NOT enough.You must CALL it.

