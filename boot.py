

import udodec

print('import complete')

#udodec.run_once()
udodec.run_once()

face = [-1,-9,-7,-5,-3]
trios = [1,-1,30,-30,24,-24,17,-17,13,-13,6,-6]
quartets = [-10,11,12,-15,16,17,-5,6,7,-22,-26,-30]

for i in quartets:
  r = udodec.random.randint(0,32)
  g = udodec.random.randint(0,32)
  b = udodec.random.randint(0,32)
  udodec.pixel.append([i,2,1,1,'RL',(r,g,b),60])
  udodec.pixel.append([i,1,1,1,'RL',(r,g,b),60])
  udodec.pixel.append([i,0,1,1,'RL',(r,g,b),60])



for i in range(1000):
  udodec.move()
  udodec.np.write()
  #udodec.dim()
 




