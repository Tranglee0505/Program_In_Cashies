def calc_total_price(apple_weight,APPLE_PRICE):
    # total = float(apple_weight) * float(APPLE_PRICE)
    return apple_weight * APPLE_PRICE

def calc_return(totals_price,moneys_given):
    if moneys_given < totals_price :
        return -1
    else:
        return moneys_given - totals_price


def infor_money(total):
    # 500 200 100 50 20 10 5 2 1
    money_500 = int(total / 500)
    total = total - money_500 * 500
    if money_500 != 0:
        print("500K : " + str(money_500))

    money_200 = int(total / 200)
    total = total - money_200 * 200
    if money_200 != 0:
        print("200K : " + str(money_200))

    money_100 = int(total / 100)
    total = total - money_100 * 100
    if money_100 != 0 :
        print("100K : " + str(money_100))

    money_50 = int(total / 50)
    total = total - money_50 * 50
    if money_50 != 0:
        print("50K : " + str(money_50))

    money_20 = int(total / 20)
    total = total - money_20 * 20
    if money_20 != 0:
        print("20K : " + str(money_20))

    money_10 = int(total / 10)
    total = total - money_10 * 10
    if money_10 != 0 :
        print("10K : " + str(money_10))

    money_5 = int(total / 5)
    total = total - money_5 * 5
    if money_5 != 0:
        print("5K : " + str(money_5))

    money_2 = int(total / 2)
    total = total - money_2 * 2
    if money_2 != 0:
        print("2K : " + str(money_2))

    money_1 = int(total / 1)
    total = total - money_1 * 1
    if money_1 != 0:
        print("1K : " + str(money_1))

def main():
    APPLE_PRICE = 21 
    apple_weight = float(input("Enter weight of apples: "))
    money_given =  float(input("Total money customer give you: "))

    total_price = calc_total_price(apple_weight,APPLE_PRICE)
    money_return = calc_return(total_price,money_given)
    print("Total price need to pay:" + str(total_price))
    if money_return == -1 :
        print("Not enough cash")
    else :
        print("You need to return to customer :"+ str(money_return))
        
    infor_money(money_return)
main()

