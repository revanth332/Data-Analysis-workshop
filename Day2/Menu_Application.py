#build a menu card application 
#show the customer the menu of items and prices
# at the end of the order show the entire bill

menu={'biryani':300,'fried Rice':200,'noodles':250,'upma':120,'dosa':20,'idli':10,'pizza':200}
print('MENU')
for item in menu:
    print(item,menu[item])
order=input('Please give your order: ').split()
bill=0
for item in order:
    item=item.lower()
    if item in menu:
        bill+=menu[item]
    else: print('sorry',item,'not available')
print('Total bill is:',bill)
