import calendar
yy=2022

ietilpiba=input("Izvēlaties cik personas (no 1 līdz 5(ieskaitot)) nakšņos! ")

if ietilpiba=="1" or ietilpiba=="2" or ietilpiba=="3" or ietilpiba=="4" or ietilpiba=="5":
  mm=int(input("Ievadiet mēnesi pēc kārtas, kurā Jūs vēlaties nakšņot! "))
  print(calendar.month(yy,mm))
  print(calendar.month(yy,mm+1))
else:
  print("Jūsu izvēlētais personu skaits nav atbilstošs.")

if ietilpiba=="1":
  viens=open("vienvietigs.txt","r")
  aiznemts=viens.read()
  print("Šie datumi ", aiznemts ,"šim numuram nav pieejami!")
  ierasanas=float(input("Ievadiet datumu, kad ieradīsieties (piem.,30.01)!" ))
  aizbrauksana=float(input("Ievadiet datumu, kad izrakstīsieties (piem.,01.02)!" ))

f=open("klients.txt","a")
f.write("Personu skaits - "+ ietilpiba +"\n")