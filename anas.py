class Fitas:   
    def __init__(self , x1 , x2):
        self.x1 = x1
        self.x2 = x2
    def fita(self):
        s = ((self.x1**2) + (self.x2**2))**0.5
        return f"النتيجة هي {s}cm"
def inpu1():
            
            print("فيثاغورس:")
            a = float(input("ماهو الرقم الاول؟"))
            b = float(input("ماهو الرقم الثاني؟"))
            return Fitas(a , b)
class Talis:
    def __init__(self , x1 , x1s ,x2):
        self.x1 = x1
        self.x1s = x1s
        self.x2 = x2
    def tali(self):
        d = (self.x1s * self.x2)/self.x1
        return f"الطول هو {d}cm"
def inpu2():
    print("طالس")
    sf = float(input("ادخل الرقم الاول؟"))
    sg = float(input("ادخل الرقم الثاني؟"))
    sh = float(input("ادخل الرقم الثالث؟"))
    return Talis(sf , sg , sh)
        
        
    

while True:
    ifg = input("""
    1.اختار فيثاغورس📐.
    2.اختار طالس 📐.
    3.خروج🙋.
    
    """)
    
    
    if ifg == "1":
        print("="*37)
        s = inpu1()
        print(s.fita())
        print("="*37)
        
    elif ifg == "2":
        print("="*37)
        h = inpu2()
        print(h.tali())
        print("="*37)
    elif ifg == "3":
        print("="*37)
        print("تم")
        print("="*37)
        break
    else:
        print("="*37)
        print("🚫لايوجد هدا الخيار")
        print("="*37)