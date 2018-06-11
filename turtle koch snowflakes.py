import turtle
def koch(kame,length,level):
  if level <0:
    return
  elif level==0:
    kame.forward(length)
    return
  else:   
    t=length/3
    koch(kame,t,level-1)
    kame.left(60)
    koch(kame,t,level-1)
    kame.right(120)
    koch(kame,t,level-1)
    kame.left(60)
    koch(kame,t,level-1)
kame=turtle.Turtle()
kame.shape('turtle')
for i in range(3):
  koch(kame,150,3)
  kame.right(120)
