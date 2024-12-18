import winsound
def alarm_system():
    correct_password="1234"
    attempts=0

    while attempts<2:
        entered_password=input("رمز را وارد کنید: ")
        if entered_password==correct_password:
            print('دستگاه قفل شد')
            break
        else:
            attempts+=1
            print(f'رمز اشتباه است. {2-attempts} تلاش دیگر دارید')

    if attempts==2:
        print("آلارم فعال شد! دزدگیر به صدا درآمد.")
        winsound.Beep(1000, 1000)  # صدای بوق با فرکانس 1000 و مدت 1 ثانیه

alarm_system()