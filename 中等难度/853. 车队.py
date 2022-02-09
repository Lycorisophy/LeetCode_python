def carFleet(target: int, position: [int], speed: [int]) -> int:
    cars = sorted(zip(position, speed))
    times = [float(target - p) / s for p, s in cars]
    ans = 0
    while len(times) > 1:
        lead = times.pop()
        if lead < times[-1]:
            ans += 1
        else:
            times[-1] = lead
    return ans + bool(times)


if __name__ == '__main__':
    print(carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
