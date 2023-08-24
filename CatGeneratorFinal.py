size(500, 500)
no_fill()
color_mode(HSB, 100)

#BackgroundStuff


#Variables
magic_number = 1
user_name = "dog"
lowercase_name = user_name.lower()
for character in lowercase_name:
    magic_number *= ( ord(character) - 96)
    print(magic_number)

random_seed(magic_number)

background(random(255), random(10, 30), random(80, 100))
#Catsilhouette
no_stroke
fill(random(255), random(10,30), random(80,100))
begin_shape()
vertex(155, 70)
vertex(165, 15)
vertex(207.5, 50)
bezier_vertex(207.5, 50, 250, 30, 292.5, 50)
vertex(335, 15)
vertex(345, 70)
bezier_vertex(345, 70, 400, 120, 345, 175)
vertex(345, 175)
vertex(353,175)
bezier_vertex(353, 175, 500, 370, 380, 460)
bezier_vertex(380, 460, 370, 480, 250, 477)
bezier_vertex(250, 477, 130, 480, 120, 460)
bezier_vertex(120, 460, -5, 380, 147, 175)
vertex(147, 175)
vertex(157, 175)
bezier_vertex(157,175, 100, 120, 155, 70)
end_shape(CLOSE)

#Patterns!!!
pattern = load_image('CatBody/pattern' + str( int(random(1,5)) ) + '.png')
tint(random(255),random(10,30), random(80,100))
image(pattern,0,0)


CatBody = load_image('CatBody/CatBody.png')
image(CatBody,0,0)

CatNose = load_image('CatBody/nose.png')
image(CatNose,0,0,)

#CatRef = load_image('CatBody/catplacement.png')
#image(CatRef,0,0)


stroke_weight(5)
stroke('#000000')
fill('#FFFFFF')


x = random(30, 50)
c = random(100, 115)
d = random(125, 130)
f = random(30, 50)

#mouth!
print( int(random(3)) == 1)
if int(random(3)) == 1:
    Mouth1 = load_image('CatBody/Mouth1.png')
    image(Mouth1,0,0)
elif int(random(3)) == 2:
    Mouth2 = load_image('CatBody/Mouth2.png')
    image(Mouth2,0,0)
else:
    Mouth3 = load_image('CatBody/Mouth3.png')
    image(Mouth3,0,0)

#lefteye
print( int(random(5)) == 1)
if int(random(3)) == 1:
    ellipse(200, 120, x, 30)

elif int(random(3)) == 2:
    #no_fill()
    begin_shape()
    vertex(170, c)
    vertex(210, 120)
    vertex(170, d)
    end_shape()

elif int(random(3)) == 3:
    CryEyeLeft = load_image('CatBody/cryeyeleft.png')
    image(CryEyeLeft,0,0)
elif int(random(4)) == 3:
    CloseEyeLeft = load_image('CatBody/closeeyeleft.png')
    image(CloseEyeLeft,0,0)
else:
    #fill('#FFFFFF')
    rect(180,100, f, 30)

#righteye
j = random(30, 50)
u = random(100, 115)
h = random(125, 130)
y = random(30, 50)

print( int(random(5)) == 1)
if int(random(3)) == 1:
    ellipse(300, 120, y, 30)
elif int(random(3)) == 2:
    begin_shape()
    vertex(330, u)
    vertex(290, 120)
    vertex(330, h)
    end_shape()
elif int(random(3)) == 3:
    CryEyeRight = load_image('CatBody/cryeyeright.png')
    image(CryEyeRight,0,0)
elif int(random(4)) == 3:
    CloseEyeRight = load_image('CatBody/closeeyeright.png')
    image(CloseEyeRight,0,0)
else:
    rect(285,100, j, 30)
    
#Fancy?
print( int(random(3)) == 1)
if int(random(3)) == 1:
    CatHat = load_image('CatAccessories/catHat.png')
    image(CatHat,0,0)
elif int(random(3)) == 2:
    CatBow = load_image('CatAccessories/catBow.png')
    image(CatBow,0,0)
else:
    bare = load_image('CatAccessories/none.png')
    image(bare,0,0)

#Blush!
    '''
print( int(random(3)) == 1)
if int(random(3)) == 1:
    Blush1 = load_image('CatBody/blush1.png')
    image(Blush1,0,0)
elif int(random(3)) == 2:
    Blush2 = load_image('CatBody/blush2.png')
    image(Blush2,0,0)
else:
    Blush3 = load_image('CatBody/blush3.png')
    image(Blush3,0,0)
    '''
blush = load_image('CatBody/blush' + str( int(random(1,4)) ) + '.png')
tint(255,random(10,30), random(80,100), (40))
image(blush,0,0)
    
#SmartCat!
print( int(random(5)) == 1)
if int(random(5)) == 1:
    Monocle = load_image('CatAccessories/monocle.png')
    tint(255,random(10,30), random(80,100), (100))
    image(Monocle,0,0)
elif int(random(5)) == 2:
    Glasses = load_image('CatAccessories/glasses.png')
    tint(255,random(10,30), random(80,100), (100))
    image(Glasses,0,0)
elif int(random(5)) == 3:
    HalfGlasses = load_image('CatAccessories/catHalfGlasses.png')
    tint(255,random(10,30), random(80,100), (100))
    image(HalfGlasses,0,0)
elif int(random(5)) == 4:
    EyePatch = load_image('CatAccessories/EyePatch.png')
    tint(255, random(10,30), random(80,100), (100))
    image(EyePatch,0,0)
else:
    bare = load_image('CatAccessories/none.png')
    image(bare,0,0)

#Brow
print( int(random(3)) == 1)
if int(random(3)) == 1:
    brows1 = load_image('CatBody/brows1.png')
    image(brows1,0,0)
    
elif int(random(3)) == 2:
    brows2 = load_image('CatBody/brows2.png')
    image(brows2,0,0)
else:
    bare = load_image('CatAccessories/none.png')
    image(bare,0,0)
    
    
#Funky accessories!!!
print( int(random(3)) == 1)
if int(random(3)) == 1:
    flower = load_image('CatAccessories/flower.png')
    tint(255, random(10,30), random(80,100), (100))
    image(flower,0,0)
elif int(random(3)) == 2:
    collar = load_image('CatAccessories/collar.png')
    tint(255, random(10,30), random(80,100), (100))
    image(collar,0,0)
else:
    bare = load_image('CatAccessories/none.png')
    image(bare,0,0)

#TabbyCat?
    #either draw the pattern in thonny and randomise the fill + transparency(i know how to do that...
    #or draw the pattern externally and apply a fill to tint it? is that possible?


    
