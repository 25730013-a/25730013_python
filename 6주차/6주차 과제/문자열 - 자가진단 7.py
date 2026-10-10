time=input()
time=time.split()

hour=int(time[0])
min=int(time[1])

if hour>=12:
    if hour>=13:
        hour=hour - 12
    print(f"{hour:02d} : {min:02d} PM")
else:
    print(f"{hour:02d} : {min:02d} AM")
