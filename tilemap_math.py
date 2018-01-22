import math

def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = (((lon_deg + 180.0) / 360.0 * n)*256/n)
  ytile = (((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)*256/n)
  return (xtile, ytile)

def num2deg(xtile, ytile, zoom):
  n = 2.0 ** zoom
  lon_deg = (xtile*(n/256)) / n * 360.0 - 180.0
  lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * (ytile*(n/256)) / n)))
  lat_deg = math.degrees(lat_rad)
  return (lat_deg, lon_deg)

def latlng2tilenum(lat,lng,zoom):
    xpoint3, ypoint3 = deg2num(lat, lng, zoom)

    ycoord3 = ypoint3 * 2 ** zoom
    nycoord3 = ycoord3

    xcoord3 = xpoint3 * 2 ** zoom
    nxcoord3 = xcoord3
    return (int(nxcoord3), int(nycoord3))

def tilenum2pix(tilenum):
    with open("map_info.txt", "r") as map_info:
        tuple = (map_info.read().split(','))
        btmleft = (int(tuple[0]),int(tuple[1])) #origin
        return (tilenum[0] - btmleft[0], btmleft[1] - tilenum[1])

def latlng2pix(lat,lng):
    #need to get bottom left corner of the map in tilenum to set as the origin
    with open("map_info.txt","r") as map_info:
        tuple = (map_info.read().split(','))
        btmleft = (tuple[0],tuple[1])  # origin
        xpoint3, ypoint3 = deg2num(lat, lng, int(tuple[2]))

        ycoord3 = ypoint3 * 2 ** int(tuple[2])
        nycoord3 = ycoord3

        xcoord3 = xpoint3 * 2 ** int(tuple[2])
        nxcoord3 = xcoord3

        return (int(nxcoord3) - int(btmleft[0]), int(btmleft[1]) - int(nycoord3))



