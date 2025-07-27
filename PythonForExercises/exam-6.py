
price_per_bread = 5000

print("نانوایی - قیمت هر نان: 5,000 تومان")

# دریافت اطلاعات یک مشتری
name = input("\nنام مشتری: ").strip()

#----------------------- محاسبات اصلی برنامه ---------------------
if name:  # اگر نام وارد شده باشد
    quantity_input = input("تعداد نان: ")

    if quantity_input.isdigit() and int(quantity_input) > 0:
        quantity = int(quantity_input)
        total = quantity * price_per_bread

        # --------------------------- نمایش نتیجه --------------------------
        print("\n--- نتیجه سفارش ---")
        print(f"نام مشتری: {name}")
        print(f"تعداد نان: {quantity}")
        print(f"هزینه کل: {total:,} تومان")
    else:
        print("\n تعداد نامعتبر! لطفاً عدد مثبت وارد کنید.")
else:
    print("\n نام مشتری وارد نشد! سفارش ثبت نشد.")

#---------------------------------------------------------------