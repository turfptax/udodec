

#udodec.py


import neopixel
import machine
import time
print('hello world!')

np = neopixel.NeoPixel(machine.Pin(39),300)

verts= [[-1,2,3],
[-3,4,5],
[-5,6,7],
[-7,8,9],
[-9,10,1],
[-4,-17,18],
[-14,15,-2],
[-10,11,12],
[-8,-23,24],
[-6,-20,21],
[20,-18,19],
[17,-15,16],
[14,-12,13],
[-11,-24,25],
[23,-21,22],
[-19,-29,30],
[29,-16,-28],
[28,-13,-27],
[27,-25,26],
[-26,-22,-30]] 
sequence = 'RLLRLLLLBLL'
die_rate = 10
pixel = []
pixel.append([-1,0,1,3,sequence,(20,127,50),55])

edges = []
for i in range(31):
  edges.append([i,0])


def run_once(np=np):
  for i in range(300):
    np[i] = (255,127,0)
    np.write()
    time.sleep(.01)
    np[i] = (0,0,0)
    np.write()
  return
  
  
def count_edges(np=np):
  for i in range(30):
    for a in range(10):
      np[(i*10)+a] = (127,127,255)
    np.write()
    time.sleep(1)
    print(f'group:{i*10}-{((i+1)*10)-1}')
    input()
    for a in range(10):
      np[(i*10)+a] = (27,0,0)
    np.write()
    
    
    
def convert_directions(text):
  numeric = []
  for i in text:
    if i == 'R':
      numeric.append(-2)
    if i == 'L':
      numeric.append(-1)
    if i == 'B':
      numeric.append(-3)
  return numeric
  
def change_color(cp,rgb):
  global edges
  hits = edges[abs(cp)][1]
  new_rgb = [0,0,0]

  new_rgb[hits%3] += 11
  r = rgb[0] + new_rgb[0]
  g = rgb[1] + new_rgb[1]
  b = rgb[2] + new_rgb[2]
  edges[abs(cp)][1] += 1
  return (r,g,b)
  
  
  
# have to give it directions:pattern and how many times:runs
def iterate_route(pattern,runs,verts=verts,np=np):
  cp = -1
  pat = convert_directions(pattern)
  print(f'Pattern Numeric Array:{pat}')
  for r in range(runs):
    for p in pat:
      if cp > 0:
        color = change_color(cp,np[(cp*10)-10])
      else:
        color = change_color(cp,np[(-cp*10)-10])
      for y in range(10):
        if cp > 0:
          np[(cp*10)-10+y] = color
        elif cp < 0:
          np[(-cp*10)-10+(9-y)] = color
        np.write()
        time.sleep(.1)
        if cp > 0:
          np[(cp*10)-10+y] = (0,0,0)
        elif cp < 0:
          np[(-cp*10)-10+(9-y)] = (0,0,0)
        np.write()
        #time.sleep(.01)
      #Pattern code
      found = False
      for i,x in enumerate(verts):
        if -cp in x and not found:
          print(f'cp:{cp}',f'Vertici:{x}',f'pattern:{p}')
          indie = x.index(-cp)
          cp = x[indie+p]
          print(f'new cp:{cp} indie:{indie} p:{p}')
          found = True
 
      
def dim(die_rate=die_rate,np=np):
  for i in range(len(np)):
    r = np[i][0] - die_rate
    g = np[i][1] - die_rate
    b = np[i][2] - die_rate
    if r < 0:
      r = 0
    if g < 0:
      g = 0
    if b < 0:
      b = 0
    np[i] = (r,g,b)
  np.write()
    
def move(verts=verts,np=np):
  global pixel
  newp = []
  for p in pixel:
    edge = p[0]
    pix = p[1]
    l = p[2]
    speed = p[3]
    pattern = p[4]
    adjustment = p[5]
    ttl = p[6]
    pat = convert_directions(pattern)
    found = False
    for num in range(speed):
        if pix + 1 > 9:
          for i,x in enumerate(verts):
            if -edge in x and not found:
              print(f'edge:{edge}',f'Vertici:{x}',f'pattern:{p}')
              indie = x.index(-edge)
              edge = x[indie+pat[0]]
              print(f'new edge:{edge} indie:{indie} pat[0]:{pat[0]}')
              found = True
          pattern = pattern[1:] + pattern[0]
          pix = pix + 1 - 10
        else:
          pix = pix + 1
        if edge > 0:
          np[(edge*10)-10+pix + 1] = adjustment
        elif edge < 0:
          np[(-edge*10)-10+(9-pix + 1)] = adjustment
    ttl -= 1
    np.write()
    dim()
    if ttl:
      newp.append([edge,pix,l,speed,pattern,adjustment,ttl])
  pixel = newp

print('right before!')
#iterate_route('RLLRLLLLBLL',50)
for i in range(100):
  move()



