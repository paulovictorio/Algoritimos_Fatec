from time import sleep
min = 10
seg = 0
while True:
    print(f"{min:02d}:{seg:02d}")
    if seg == 0:
        min -= 1
        seg = 59
    else:
        seg -= 1
    if seg == 0 and min == 0:
        break
    sleep(1)