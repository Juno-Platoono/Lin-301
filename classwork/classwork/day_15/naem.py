

x = 13.2

if x % 2 == 0:
    print(x,"is even.")
elif x % 2 == 1: 
    print(x,"is odd.")
else:
    print(x,"is a decimal.")

novel = "Agnes Grey"

charlotte = ["The Professor","Jayne Eyre","Shirley","Villette"]
emily = ["wuthering Heights"]
anne = ["Agnes Grey","The Tenant of Wildfell Hall"]

bronte_checks={"charlotte":0, "emily":0,"anne":0}
if novel in charlotte:
    bronte_checks["charlotte"] +=1
    print("charolette bronte wrote ",novel)
elif novel in anne:
    bronte_checks["anne"] +=1
    print("anne bronte wrote ",novel)
elif novel in emily:
    bronte_checks["emily"] +=1
    print("emily wrote ",novel)
else:
    print("not from bronte sisters")
