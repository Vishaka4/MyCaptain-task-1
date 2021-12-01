n=(input("Input the File name:"))
a=len(n)
if n[(a-1)-a]=='y' and n[(a-2)-a]=='p' and n[(a-3)-a]=='.':
    print("The extension  of the file is:'python'")
else:
    print("The extension of the file is not python")
