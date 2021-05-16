import requests

spot_data = requests.get("http://127.0.0.1:5000/")
print(spot_data.json())
places = spot_data.json()["Spots"]

print("Please type the coordinates of the desired location in the format x y")
going_to = input()

going_to = going_to.split()
x = int(going_to[0])
y = int(going_to[1])

min = 100000000
for place in places:

    dis = (int(place[0]) - x)**2 + (int(place[1]) - y)**2

    if dis <= min:
        min = dis
        best_place = place

print("The closest parking spot is " + str(best_place))

