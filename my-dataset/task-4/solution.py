window = []

def add_number(num):
    window.append(num)
    
    if len(window) > 3:
        window.pop(0)   # ✅ FIX (in-place change)
    
    return sum(window) / len(window)