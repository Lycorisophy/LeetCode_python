def canMeasureWater(jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
    if targetCapacity > jug1Capacity + jug2Capacity:
        return False
    if targetCapacity == jug1Capacity or targetCapacity == jug2Capacity \
            or targetCapacity == jug1Capacity + jug2Capacity:
        return True
    if jug1Capacity == jug2Capacity:
        return False
    elif jug1Capacity > jug2Capacity:
        jug1Capacity, jug2Capacity = jug2Capacity, jug1Capacity
    return


if __name__ == '__main__':
    print(canMeasureWater(3, 5, 4))
    print(canMeasureWater(2, 6, 5))

