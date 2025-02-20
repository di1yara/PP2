import json
with open("sample-data.json") as file:
    data = json.load(file)
print("Interface Status")
print("=" * 80)
print("{:<40} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80 )
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else "N/A"
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print(f"{dn:<20} {descr:<10} {speed:<10} {mtu:<10}")

print("=" * 80)

