import turtle as tr
# import model_for_gesture
def draw(shape):
    sc = tr.Screen()
    sc.setup(width = 1.0, height = 1.0)
    tr.position
    if shape=="circle":
        tr.circle(50)
        # tr.done()
    elif shape=="rectangle":
        tr.forward(50)
        tr.left(90)
        tr.forward(50)
        tr.left(90)
        tr.forward(50)
        tr.left(90)
        tr.forward(50)
        # tr.done()
    elif shape=="triangle":
        tr.left(60)
        tr.forward(60)
        tr.right(120)
        tr.forward(60)
        tr.right(120)
        tr.forward(60)
        # tr.done()
    elif shape=="triangle":
        tr.left(60)
        tr.forward(60)
        tr.right(120)
        tr.forward(60)
        tr.right(120)
        tr.forward(60)
        # tr.done()
    elif shape=="turn Left":
        tr.left(30)
        # tr.done()
    elif shape=="turn Right":
        tr.right(30)
        
    else:
        tr.clear()
        tr.backward(50)
        tr.color("red")
        tr.write("Sorry,But I cant draw the Shape, "+"' "+shape+" '")
        # tr.done()   
    


# start('triangle')