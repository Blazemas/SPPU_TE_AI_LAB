def water_balance(capacity1, capacity2, result):
    jug1 = 0
    jug2 = 0
    
    while jug1 != result and jug2 != result:
        print(f"Jug 1: {jug1}, Jug 2: {jug2}")
        if jug1 == 0:
            jug1 = capacity1
        elif jug1 > 0 and jug2 < capacity2:
            pour_water = min(jug1, capacity2 - jug2)
            jug1 -= pour_water
            jug2 += pour_water
        elif jug2 == capacity2:
            jug2 = 0
    
    print(f"Jug 1: {jug1}L, Jug 2: {jug2}L")
    

if __name__ == "__main__":
    capacity1 = int(input("Enter capacity of Jug 1 >> "))
    capacity2 = int(input("Enter capacity of Jug 2 >> "))
    result = int(input("Enter the target amount of water >> "))
    
    water_balance(capacity1, capacity2, result)