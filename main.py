import pyglet # import the library
win= pyglet.window.Window() # create the window

he= pyglet.image.load('Overworld.png')
smol_he = he.get_region(x=265 , y= 75, width=32 , height=32)
the = pyglet.sprite.Sprite(smol_he, x = 0, y = 0)


 

sprites = []
for j in range(30):
  for i in range(30):
    sprites.append(pyglet.sprite.Sprite(smol_he, x = i * 25, y = j * 25))



 

def update(dt):
  pass

# Start the event loop
@win.event
def on_draw():
    win.clear()
    the.draw()
    for i in range(len(sprites)):
      sprites[i].draw()
      
 
 
pyglet.clock.schedule(update) 
pyglet.app.run()