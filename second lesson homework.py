math = input('數學幾分？')
english = input('英文幾分？')
math = float(math)
english = float(english)

if math >= 90 and english >= 90:
    print('有獎品')
elif math < 60 and english < 60:
    print('處罰')