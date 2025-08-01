#  ------------------------کدهای رنگی -----------------
SUNNY = "\033[1;33m"    # زرد پررنگ (آفتابی)
RAINY = "\033[1;34m"    # آبی پررنگ (بارانی)
CLOUDY = "\033[1;37m"   # سفید پررنگ (ابری)
RESET = "\033[0m"       # بازنشانی رنگ
#------------------------------------------------------

weathers = ["آفتابی", "بارانی", "ابری", "آفتابی", "ابری"]

for weather in weathers:
    if weather == "آفتابی":
        print(f"{SUNNY} هوا آفتابی است. روز خوبی برای پیاده‌روی!{RESET}")
    elif weather == "بارانی":
        print(f"{RAINY} هوا بارانی است. چتر خود را فراموش نکنید!{RESET}")
    elif weather == "ابری":
        print(f"{CLOUDY} هوا ابری است. ممکن است باران ببارد!{RESET}")
    else:
        print(f"وضعیت هوا نامشخص: {weather}")