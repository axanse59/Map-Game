import pyglet # import the library
win= pyglet.window.Window() # create the window

he= pyglet.image.load('colony.png')
smol_he = he.get_region(x=0 , y= 280, width=32 , height=32)
the = pyglet.sprite.Sprite(smol_he, x = 0, y = 0)

tt= pyglet.image.load('colony.png')
smol_tt = tt.get_region(x=50 , y= 280, width=32 , height=32)
spr = pyglet.sprite.Sprite(smol_tt, x = 0, y = 0)


 

sprites = []
for j in range(5):
  for i in range(19):
    sprites.append(pyglet.sprite.Sprite(smol_he, x = 200, y = i * 30,))

sprites = []
for t in range(5):
  for y in range(19):
    sprites.append(pyglet.sprite.Sprite(smol_tt, x = 300, y = y * 30,))



 

def update(dt):
  pass

# Start the event loop
@win.event
def on_draw():
    win.clear()
    #the.draw()
    for i in range(len(sprites)):
      sprites[i].draw()

    for y in range(len(sprites)):
      sprites[y].draw()
      
 
 
pyglet.clock.schedule(update) 
pyglet.app.run()