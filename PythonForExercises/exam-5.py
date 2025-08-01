# --------------------- زمان آماده‌سازی هر غذا (دقیقه)----------------------
prep_time = {
    "پیتزا": 15,
    "برگر": 10,
    "ساندویچ": 8,
    "سالاد": 5
}
#---------------------------------------------------------------------------

# ------------------------------ نمایش منو------------------------------------
print("منوی غذاها:")
for food, time in prep_time.items():
    print(f"- {food}: {time} دقیقه")
#---------------------------------------------------------------------------

# ----------------- دریافت سفارش ---------------
food = input("\nنوع غذا را وارد کنید: ")

if food in prep_time:
    quantity = input("تعداد را وارد کنید: ")

    if quantity.isdigit() and int(quantity) > 0:
        quantity = int(quantity)
#----------------------------------------------

        # --------------------- محاسبه زمان آماده‌سازی ------------------
        if food == "پیتزا":
            time_needed = prep_time[food] + 3 * (quantity - 1)
        else:
            time_needed = prep_time[food] * quantity

        print(f"\nزمان آماده‌سازی: {time_needed} دقیقه")
        #---------------------------------------------------------------
    else:
        print("\n تعداد نامعتبر! لطفاً عدد مثبت وارد کنید.")
else:
    print("\n این غذا در منو وجود ندارد!")
#---------------------------------------------------------------