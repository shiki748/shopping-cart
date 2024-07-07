print('Hello, welcome to my gundam store, press 1 to start viewing the list of GUNDAMS available!')
def menu():
    print("[1]View Menu/Place orders")


order = ['GUNDAM RAISER     ',
         'Gundam SEED Astray',
         'Wing Gundam       ',
         'Freedom Gundam    ',
         'RG GoldyMarg      ',
         'RG Gao Gai Gar    ',
         'God Gundam        ',
         'Wing Gundam Astray',
         'Eclipse Gundam    ',
         'Full Saber        ',
         'Unicorn Gundam    ',
         'Gundam Dynames    ',
         'Messiah Ranka Lee ',
         'Ganesa            ',
         'Arcanadea Lumitea ',
         'Tsubasa Kazanari  ',
         'Little Ryan       ',
         'Elephant RAcer    ',
         'Zoids Stylaser    ',
         'Cannon Bull       ']

price = [315, 320, 350, 410, 52, 78, 58, 38, 195, 72, 64, 56, 95, 20, 75, 90, 30, 17, 148, 35]
grade = ['Perfect Grade     ',
         'Perfect Grade     ',
         'Perfect Grade     ',
         'Perfect Grade     ',
         'Real Grade        ',
         'Real Grade        ',
         'Real Grade        ',
         'Real Grade        ',
         'Master Grade      ',
         'Master Grade      ',
         'Master Grade      ',
         'Master Grade      ',
         'Mecha Girl        ',
         'Mecha Girl        ',
         'Mecha Girl        ',
         'Mecha Girl        ',
         'Mototrized        ',
         'Mototrized        ',
         'Mototrized        ',
         'Mototrized        ']

cart = []
quantity =[]


shoppinglist = [[1, "Arcanadea Lumitea", 75, "Mecha Girl"],
                            [2, "Cannon Bull", 35, "Motorized"],
                            [3, "Eclipse Gundam", 195, "Master Grade"],
                            [4, "Elephant Racer", 17, "Motorized"],
                            [5, "Freedom Gundam", 410, "Perfect Grade"],
                            [6, "Full Saber", 72, "Master Grade"],
                            [8, "Ganesa", 20, "Mecha Girl"],
                            [7, "GUNDAM RAISER", 315, "Perfect Grade"],
                            [11, "Gundam SEED Astray", 320, "Perfect Grade"],
                            [9, "God Gundam", 58, "Real Grade"],
                            [10, "Gundam Dynames", 56, "Master Grade"],
                            [12, "Little Ryan", 30, "Motorized"],
                            [13, "Messiah Ranka Lee", 95, "Mecha Girl"],
                            [14, "RG GoldMarg", 52, "Real Grade"],
                            [15, "RG Gao Gai Gar", 78, "Real Grade"],
                            [16, "Tsubasa Kazanari", 90, "Mecha Girl"],
                            [17, "Unicorn Gundam", 64, "Master Grade"],
                            [18, "Wing Gundam", 350, "Perfect Grade"],
                            [19, "Wing Gundam Astray", 38, "Real Grade"],
                            [20, "Zoids Stylaser", 148, "Motorized"],
                            ]
def displaymenu():
    print(''' ====================GUNDAM FIGURINES FOR SALE! (LIMITED EDITIONS!)====================  ''')
    print(''' -------------------------------------------------------------------------------------- 
| Number |         Item           |        Price(SGD)         |        Category       |
--------------------------------------------------------------------------------------- ''')

    for item in shoppinglist:
        print("|", item[0], " "*(5-len(str(item[0]))),"|", item[1], " "*(21-len(item[1])), "|",
              item[2], " "*(24-len(str(item[2]))), "|", item[3], " "*(20-len(item[3])), "|")

def list():
    grand = 0.0
    print('-'*65)
    print('Item', 'Price(SGD)', '\b\b\bGrades', sep='\t\t\t\t\t\t')
    for kk in range(len(order)):
        print('|' + str(kk + 1) + '|' + order[kk], price[kk], '|' + grade[kk] + '|', sep='\t\t\t')

    print()
    shopping_complete = 0
    while shopping_complete == 0:
        fort = int(input('Select your option, 1 to 20, 21 to view shopping cart items and 0 to check out.\n'))
        if fort == 0:
            print('Proceeding to checkout')
            shopping_complete = 1

        elif fort <= 20:
            print('You selected', order[fort - 1])
            quan = int(input('How many units do you wish to purchase?\n'))
            if order[fort - 1] in cart:
                print('repeated selection')
                idx = cart.index(order[fort - 1])
                print(idx)
                quantity[idx] += quan
            else:
                print('New selection')
                cart.append(order[fort - 1])
                quantity.append(quan)

        elif fort == 21:
            view_cart()

        else:
            print('Invalid option, please try again')

    print()
    print('-' * 65)
    print('ITEM', ' QUANTITY', '\b\bPRICE(SGD)', sep='\t\t\t\t')
    for kk in range(len(cart)):
       idx = order.index(cart[kk])
       lol = price[idx]
       total = round(quantity[kk] * lol, 2)
       grand = grand + total
       print(cart[kk], quantity[kk], total, sep='\t\t\t')
    print()
    print(f'Your total in cart is: $ {grand}')
    print('-' * 65)

    print('Would you like to edit your shopping cart? (yes/no): ')
    YN = input()
    print()
    if YN == "yes":
        basket = input("Would you like to add additional items or remove items to your shopping cart?(type add or remove): ")
        if basket == "add":
            Q = int(input("What item number (aka the ranking of the items of order you placed in cart) would you like to add to the shopping cart?:  "))
            U = Q - 1
            A = quantity.pop(U)
            N = int(input('How many quantity do u want to add?: '))
            T = A + N
            quantity.insert(U, T)
            print()
            print('-' * 65)
            print('ITEM', ' QUANTITY', '\b\bPRICE(SGD)', sep='\t\t\t\t')
            for kk in range(len(cart)):
                idx = order.index(cart[kk])
                lol = price[idx]
                total = round(quantity[kk] * lol, 2)
                grand = total
                final = sum(round(quantity[kk] * price[order.index(cart[kk])], 2) for kk in range(len(cart)))
                print(cart[kk], quantity[kk], total, sep='\t\t\t')
            print()
            print(f'Your total in cart is: $ {final}')
            print('-' * 65)

        elif basket == 'remove':
            Q = int(input("What item number would you like to remove from the shopping cart?:  "))
            U = Q - 1
            A = quantity.pop(U)
            N = int(input('How many quantity would you want to remove?: '))
            T = A - N
            quantity.insert(U, T)
            print()
            print('-' * 65)
            print('ITEM', ' QUANTITY', '\b\bPRICE(SGD)', sep='\t\t\t\t')
            for kk in range(len(cart)):
                idx = order.index(cart[kk])
                lol = price[idx]
                total = round(quantity[kk] * lol, 2)
                grand = total
                final = sum(round(quantity[kk] * price[order.index(cart[kk])], 2) for kk in range(len(cart)))
                print(cart[kk], quantity[kk], total, sep='\t\t\t')
            print()
            print(f'Your total in cart is: $ {final}')
            print('-' * 65)
        else:
            print('Invalid option, please try again')

    membership = 'none'
    dct_rate = 0.0
    print('Do you perhaps have a membership discount? (yes/no)')
    YP = input()

    if YP == 'yes':
        membership = input('Select a membership: Gold membership is [15%], Silver membership is [10%], '
                           'and Bronze membership is [5%]: ')

    if membership == 'gold':
        dct_rate = 15.0  # discount in percentage for gold
        gst_rate = 8.0   # gst rate included
        print()
        print('-' * 65)
        print('ITEM', ' QUANTITY', '\b\bPRICE(SGD)', sep='\t\t\t\t')
        for kk in range(len(cart)):
            idx = order.index(cart[kk])
            lol = price[idx]
            total = round(quantity[kk] * lol, 2)
            grand = grand + total
            final = sum(round(quantity[kk] * price[order.index(cart[kk])], 2) for kk in range(len(cart)))
            print(cart[kk], quantity[kk], total, sep='\t\t\t')
        print()
        print(f'Your total in cart is: $ {final}')
        print('-' * 65)

    elif membership == 'silver':
        dct_rate = 10.0  # discount in percentage for silver
        gst_rate = 8.0  # gst rate included
        print()
        print('-' * 65)
        print('ITEM', ' QUANTITY', '\b\bPRICE(SGD)', sep='\t\t\t\t')
        for kk in range(len(cart)):
            idx = order.index(cart[kk])
            lol = price[idx]
            total = round(quantity[kk] * lol, 2)
            grand = grand + total
            final = sum(round(quantity[kk] * price[order.index(cart[kk])], 2) for kk in range(len(cart)))
            print(cart[kk], quantity[kk], total, sep='\t\t\t')
        print()
        print(f'Your total in cart is: $ {final}')
        print('-' * 65)

    elif membership == 'bronze':
        dct_rate = 5.0  # discount in percentage for bronze
        gst_rate = 8.0 # gst rate included
        print()
        print('-' * 65)
        print('ITEM', ' QUANTITY', '\b\bPRICE(SGD)', sep='\t\t\t\t')
        for kk in range(len(cart)):
            idx = order.index(cart[kk])
            lol = price[idx]
            total = round(quantity[kk] * lol, 2)
            grand = grand + total
            final = sum(round(quantity[kk] * price[order.index(cart[kk])], 2) for kk in range(len(cart)))
            print(cart[kk], quantity[kk], total, sep='\t\t\t')
        print()
        print(f'Your total in cart is: $ {final}')
        print('-' * 65)

    elif YP == 'no':
        gst_rate = 8.0 # gst rate included
        print()
        print('-' * 65)
        print('ITEM', ' QUANTITY', '\b\bPRICE(SGD)', sep='\t\t\t\t')
        for kk in range(len(cart)):
            idx = order.index(cart[kk])
            lol = price[idx]
            total = round(quantity[kk] * lol, 2)
            grand = grand + total
            final = sum(round(quantity[kk] * price[order.index(cart[kk])], 2) for kk in range(len(cart)))
            print(cart[kk], quantity[kk], total, sep='\t\t\t')
        print()
        print(f'Your total in cart is: $ {final}')
        print('-' * 65)
    else:
        print('Invalid option, please try again.')

    discount = round(dct_rate / 100.0 * final, 2)
    gst = round(gst_rate / 100.0 * (final - discount), 2)
    print('Your total order is (SGD) $', final)
    print(f'Discount IS (SGD) $ {discount}')
    print(f'GST (8%) is (SGD) $ {gst}')
    print('Your order value, after discount (SGD) $', round(final - discount, 2))
    print('Including GST rate of 8% (SGD) $', round(gst, 2))
    print('The total you have to pay is (SGD) $', round(final - discount + gst, 2))
    print('Thank you for your purchase! Hope to see you again!')
    print('-' * 65)
    if discount >= 1:
        exit()
    if not discount >= 1:
        exit()


def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print('''=================Shopping Cart================    ''')
        print('ITEM', ' QUANTITY', '\b\bPRICE(SGD)', sep='\t\t\t\t')
        for item, qty in zip(cart, quantity):
            idx = order.index(item)
            price_item = price[idx]
            total_item = round(qty * price_item, 2)
            print(item, qty, total_item, sep='\t\t\t')
        print()
        print('Your total in cart is: $', sum(round(quantity[kk] * price[order.index(cart[kk])], 2) for kk in range(len(cart))))
        print('-'*65)


def main():
    menu()
    option = int(input("Enter your option:"))
    while option != 0:
        if option == 1:
            print("=======Menu=======")
            print("Sort Menu by alphabetical, prices, category and start placing orders!")
            print("[1] Alphabetical")
            print("[2] Prices")
            print("[3] Category")
            print("[4] Place order")
            MenuType = int(input("Please select display type:"))

            if MenuType == 1:
                def sort_item(item):
                    return item[1]
                shoppinglist.sort(key=sort_item)

            elif MenuType == 2:
                def sort_item(item):
                    return item[2]
                shoppinglist.sort(key=sort_item)

            elif MenuType == 3:
                def sort_item(item):
                    return item[3]
                shoppinglist.sort(key=sort_item)
                print()

            elif MenuType == 4:
                list()

            else:
                print("Invalid option")

            displaymenu()

        elif option == 2:
           view_cart()

        elif option == 3:
            pass

        else:
            print("Invalid option")

        menu()

main()