print("*** Rabbit & Turtle ***")

d, Vr, Vt, Vf = map(int, input("Enter Input : ").split())


time = d / (Vt - Vr)
fly_distance = time * Vf


print("{:.2f}".format(fly_distance))
