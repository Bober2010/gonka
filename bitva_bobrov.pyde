z = 0
x = 0
c = 0
b = 255
def setup():
    size(600,1000)
def draw():
    background(0)
    global z,x,c,b
    m = loadImage("DIO.png")
    image(m,x,0,200,200)
    m = loadImage("kakqein.png")
    image(m,z,200,200,200)
    m = loadImage("ctar platinym.jpg")
    image(m,c,400,200,200)
    z += 4
    x += 3
    c += 7
    if c >= 400:
        x = 200
        c = 400
        z = 300
        textSize(60)
        fill(random(b),random(z),random(x))
        text("win Jotaro!", 100,800)
