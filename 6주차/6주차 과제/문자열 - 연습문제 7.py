hour=int(input())
min=int(input())

if hour>12:
    print(f"{hour:02d} : {min:02d} PM")
else:
    print(f"{hour:02d} : {min:02d} AM")
