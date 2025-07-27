#  ------------------------کدهای رنگی -----------------
PIZZA_COLOR = "\033[1;91m"     # قرمز پررنگ
SALAD_COLOR = "\033[1;92m"     # سبز پررنگ
BURGER_COLOR = "\033[1;93m"    # زرد پررنگ
RESET = "\033[0m"              # بازنشانی رنگ
#------------------------------------------------------

#--------------------- تعریف غذا ها و قیمت‌های پایه برای غذاها----------------
foods = ["پیتزا", "سالاد", "برگر", "پیتزا", "سالاد"]
base_prices = {
    "پیتزا": 50000,
    "سالاد": 30000,
    "برگر": 40000
}
#-------------------------------------------------------------------------------

for food in foods:
    # محاسبه قیمت با افزودن مالیات 9%
    if food in base_prices:
        price = base_prices[food]
        final_price = int(price * 1.09)  # اضافه کردن 9% مالیات
        formatted_price = f"{final_price:,}"
        if food == "پیتزا":
            print(f"{PIZZA_COLOR} {food}: {formatted_price} تومان (با مالیات){RESET}")
        elif food == "سالاد":
            print(f"{SALAD_COLOR} {food}: {formatted_price} تومان (با مالیات){RESET}")
        elif food == "برگر":
            print(f"{BURGER_COLOR} {food}: {formatted_price} تومان (با مالیات){RESET}")
    else:
        print(f"غذای '{food}' در منو وجود ندارد.")