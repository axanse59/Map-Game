import pyglet # import the library
win= pyglet.window.Window() # create the window


he= pyglet.image.load('colony.png')
smol_he = he.get_region(x=0 , y= 280, width=32 , height=32)
the = pyglet.sprite.Sprite(smol_he, x = 0, y = 0)

tt= pyglet.image.load('colony.png')
smol_tt = tt.get_region(x=24 , y= 280, width=32 , height=32)
spr = pyglet.sprite.Sprite(smol_tt, x = 0, y = 0)

ii= pyglet.image.load('colony.png')
smol_ii = ii.get_region(x=17 , y= 280, width=32 , height=32)
yui = pyglet.sprite.Sprite(smol_ii, x = 0, y = 0)

pp= pyglet.image.load('terrain-v7.png')
smol_pp = pp.get_region(x=510 , y= 1459, width=35 , height=32)
poi = pyglet.sprite.Sprite(smol_pp, x = 0, y = 0)

uu= pyglet.image.load('torso.png')
smol_uu = uu.get_region(x=2 , y= 5 , width=90 , height=128)
moi = pyglet.sprite.Sprite(smol_uu, x = 300, y = 200)


sprites=[]
def Arena():

  for j in range(5):
    for i in range(19):
      sprites.append(pyglet.sprite.Sprite(smol_he, x = 200, y = i * 30,))

  for y in range(19):
    sprites.append(pyglet.sprite.Sprite(smol_tt, x = 420, y = y * 30,))

  for q in range(19):
    sprites.append(pyglet.sprite.Sprite(smol_ii, x = 232, y = q * 30,))

  for q in range(19):
    sprites.append(pyglet.sprite.Sprite(smol_ii, x = 264, y = q * 30,))

  for q in range(19):
    sprites.append(pyglet.sprite.Sprite(smol_ii, x = 296, y = q * 30,))

  for q in range(19):
    sprites.append(pyglet.sprite.Sprite(smol_ii, x = 328, y = q * 30,))

  for q in range(19):
    sprites.append(pyglet.sprite.Sprite(smol_ii, x = 360, y = q * 30,))

  for q in range(19):
    sprites.append(pyglet.sprite.Sprite(smol_ii, x = 392, y = q * 30,))

def Lava():
  for a in range(6):
    for c in range(19):
      sprites.append(pyglet.sprite.Sprite(smol_pp, x = a * 35, y = c * 32,))

  for c in range(19):
    sprites.append(pyglet.sprite.Sprite(smol_pp, x = 450, y = c * 32,))

  for c in range(19):
    sprites.append(pyglet.sprite.Sprite(smol_pp, x = 485, y = c * 32,))
  
  for c in range(19):
    sprites.append(pyglet.sprite.Sprite(smol_pp, x = 515, y = c * 32,))

  for c in range(19):
    sprites.append(pyglet.sprite.Sprite(smol_pp, x = 550, y = c * 32,))

  for c in range(19):
    sprites.append(pyglet.sprite.Sprite(smol_pp, x = 585, y = c * 32,))

  for c in range(19):
    sprites.append(pyglet.sprite.Sprite(smol_pp, x =615, y = c * 32,))



def update(dt):
  pass

# Start the event loop
@win.event
def on_draw():
    win.clear()
    Arena()
    Lava()
    for i in range(len(sprites)):
      sprites[i].draw()

 
      
 
 
pyglet.clock.schedule(update) 
pyglet.app.run()