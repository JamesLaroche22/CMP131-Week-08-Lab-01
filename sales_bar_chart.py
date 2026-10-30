#James_Laroche
#CMP-131 
#Week_8
#Lab_1 
#sales_bar
#October_30th
ast=""
store=int(input("enter number of stores: ")) 
for i in range (store):
    sales=int(input("enter todays number of sales" +str(i+1) +":"))
    sales=sales/100 
    sales=int(sales)
    for j in range (sales):
            ast=ast + "*"
    ast=ast+"\n"
print (ast)
    