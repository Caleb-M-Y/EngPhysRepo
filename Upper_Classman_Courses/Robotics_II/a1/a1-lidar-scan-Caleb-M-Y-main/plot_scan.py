import matplotlib.pyplot as plt
from adafruit_rplidar import RPLidar
from math import floor, pi

# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME, timeout=3)
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# math setup
x = 0
y = 0
#r = 0
th = 0
th_rad = [0]*360
counter = 0

# used to scale data to fit on the screen
max_distance = 0
scan_data = [0]*360

def polTOcart(th, scan_data):
    th_rad = (th * pi / 180)
    x = scan_data * cos(th_rad)
    y = scan_data * sin(th_rad)
    return x, y

# def process_data(data):
    #print(data)
#     th = list(range(360))
#     th_rad = ((pi / 180) * angle)

#scan_data = [0]*360



#    print(lidar.get_info())
for i in range(360):
    th_rad[i] = pi * i / 180
    
   
for scan in lidar.iter_scans():
    counter += 1
    if counter > 10:
        break
    for (_, angle, distance) in scan:
        scan_data[min([359, floor(angle)])] = distance
        

#     if i > 1:
#         break
    #process_data(scan_data)
    
#polor to cart funciton
scan_data = list(reversed(scan_data))
x, y = polTOcart(0, scan_data[0])
print(x, y)
x, y = polTOcart(135, scan_data[135])
print(x, y)
x, y = polTOcart(225, scan_data[225])
print(x, y)

print(scan_data)
print(0, scan_data[0])
print(135, scan_data[135])
print(225, scan_data[225])

ax.plot(th_rad, scan_data, ".")
ax.set_rmax(1000)
ax.set_rticks([250, 500, 750, 1000]) 
plt.show()
lidar.stop()
lidar.disconnect()


