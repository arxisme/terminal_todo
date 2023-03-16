import os
home_path = os.path.expanduser('~')
home_path = home_path +"/"
os.system("touch "+home_path+"todo.txt")
with open(home_path+"todo" , 'w') as f:
    f.write('#!')
os.system("which python3 >> "+home_path+"todo")

file_path = home_path+"todo.txt"
fin = open("todo",'r')
fout = open(home_path+'todo' , 'a')
for line in fin:
    fout.write(line.replace('/home/blobr0pchop/todo_terminal/todo.txt',file_path))

os.system("sudo chmod +x "+home_path+'todo' )

