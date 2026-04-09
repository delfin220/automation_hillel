data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def calculate(s: str) -> int:
    parts = s.split(",")
    total = 0
    for i in parts:
        total += int(i)
    return total

for i in data :
    try:
     total = calculate(i)
     print(total)
    except:
     print("Не можу вивести")

