inventory = []
for i in range (0, 8):
    inventory.append("")
worldmap = [
    ["g", "g", "g", "g", "g", "g"],
    ["g", "g", "g", "g", "g", "g"],
    ["g", "g", "g", "g", "g", "g"],
    ["g", "g", "g", "g", "g", "g"],
    ["g", "g", "g", "g", "g", "g"],
    ["g", "g", "@", "g", "g", "g"],
    ]
x = 2
z = -1
print(worldmap[z])
def up():
    global z
    z = z+1
    worldmap[z-1][x] = "g"
    worldmap[z][x] = "@"
    print(worldmap[z])
