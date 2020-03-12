file = open(r"C:\Users\HP\Desktop\data_files\10.txt","r")
a = file.readlines()

kelime = input("Aranacak kelimeyi girin:")
for i in range(0,len(a)):
    s=0
    t =["","","","",""]
    x=a[i].split()
    if kelime in x:
        while(x[s]!=kelime):
            s=s+1
        m=len(x)   
        for j in range(0,5):
            if(x[s+j] is not None):
                t[j]=x[s+j]
                print(t[:j+1])
            else:
                t[j]="null"
                print(t[:j+1])
                break
