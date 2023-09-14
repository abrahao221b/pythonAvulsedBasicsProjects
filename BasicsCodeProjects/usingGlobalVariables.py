enemies = 1

def modifying_global():
    global enemies
    enemies += 1
    print(f"Has {enemies} enemies!")

modifying_global()
print(f"{enemies}")
