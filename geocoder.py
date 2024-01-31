def get_spn(toponym) -> str:
    coords = list(toponym.get("boundedBy").get("Envelope").values())
    x1, y1 = map(float, coords[0].split())
    x2, y2 = map(float, coords[1].split())
    return f"{abs(x2 - x1)},{abs(y2 - y1)}"


def get_ll(toponym) -> str:
    coords = toponym["Point"]["pos"]
    longitude, lattitude = coords.split(" ")
    coords = ",".join([longitude, lattitude])
    return coords
