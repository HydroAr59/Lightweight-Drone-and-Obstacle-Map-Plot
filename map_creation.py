try:
    from urllib.request import urlopen
    import io
    import tilemap_math as tm
    from PIL import Image

except:
    from urllib2 import urlopen
    import io
    import tilemap_math as tm
    from PIL import Image

class createMap:

    def __init__(self,lat,lng,zoom=16):
        self.lat = lat
        self.lng = lng
        self.zoom = zoom

    def generateImage(self):
        #longitude is x and latitude is y
        tile_size = 600
        map_img = Image.new("RGB", (tile_size * 5, tile_size * 5))

        lat = self.lat
        lng = self.lng

        for x in range(0,5):
            xpoint2, ypoint2 = tm.deg2num(lat, lng, self.zoom)

            for y in range(0,5):



                google_url = "https://maps.googleapis.com/maps/api/staticmap?center=" + str(lat)+","+ str(lng) + "&zoom="+str(self.zoom)+"&scale=1&size="+str(tile_size)+"x"+str(tile_size)+"&maptype=satellite&format=png&visual_refresh=true"
                file = io.BytesIO(urlopen(google_url).read())
                im = Image.open(file)

                if (y == 4 and x == 0):
                    xpoint3, ypoint3 = tm.deg2num(lat, lng, self.zoom)

                    ycoord3 = ypoint3 * 2 ** self.zoom
                    nycoord3 = ycoord3 + 300
                    #nypoint3 = nycoord3 / 2 ** self.zoom

                    xcoord3 = xpoint3 * 2 ** self.zoom
                    nxcoord3 = xcoord3 - 300
                    #nxpoint3 = nxcoord3 / 2 ** self.zoom

                   # lat2, lng2 = num2deg(nxpoint3, nypoint3, self.zoom)
                    print("Bottom left corner:",int(nxcoord3),int(nycoord3))
                    with open("map_info.txt",'w') as map_info:
                        map_info.write(str(int(nxcoord3))+","+str(int(nycoord3)) + "," + str(self.zoom))

                elif (y == 0 and x == 4):
                    xpoint3, ypoint3 = tm.deg2num(lat, lng, self.zoom)

                    ycoord3 = ypoint3 * 2 ** self.zoom
                    nycoord3 = ycoord3 - 300
                    #nypoint3 = nycoord3 / 2 ** self.zoom

                    xcoord3 = xpoint3 * 2 ** self.zoom
                    nxcoord3 = xcoord3 + 300
                    #nxpoint3 = nxcoord3 / 2 ** self.zoom

                    #lat2, lng2 = num2deg(nxpoint3, nypoint3, self.zoom)
                    print("Top right corner:",int(nxcoord3),int(nycoord3))

                map_img.paste(im,(x*tile_size,y*tile_size))

                xpoint, ypoint = tm.deg2num(lat, lng, self.zoom)

                ycoord = ypoint * 2 ** self.zoom
                nycoord = ycoord + 600
                nypoint = nycoord / 2 ** self.zoom

                lat,lng = tm.num2deg(xpoint,nypoint,self.zoom)

            xcoord = xpoint2 * 2 ** self.zoom
            nxcoord = xcoord + 600
            nxpoint = nxcoord / 2**self.zoom
            lat, lng = tm.num2deg(nxpoint, ypoint2, self.zoom)

        return map_img

if __name__ == '__main__':
    '''
    gmd = createMap(lat,lon,zoomlevel) #add the top left corner latlng coordinates of the area you want and the zoom level
    img = gmd.generateImage()
    img.save('map.png')
    '''