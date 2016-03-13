import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
ex = False
x1 = 0.3
x2 = -0.3
y1 = 0.3
y2 = 0
def key_callback(window, key, scancode, action, mods):
    if action == glfw.PRESS and key == glfw.KEY_DOWN:
        y2 -= 0.1
    if action == glfw.PRESS and key == glfw.KEY_W:
        y2 += 0.1
    if action == glfw.PRESS and key == glfw.KEY_LEFT:
        x2 -= 0.1
    if action == glfw.PRESS and key == glfw.KEY_D:
        x2 += 0.1
    if action == glfw.PRESS and key == glfw.KEY_UP:
        y1 += 0.1
    if action == glfw.PRESS and key == glfw.KEY_S:
        y1 -= 0.1
    if action == glfw.PRESS and key == glfw.KEY_RIGHT:
        x1 += 0.1
    if action == glfw.PRESS and key == glfw.KEY_A:
        x1 -= 0.1
    if action == glfw.PRESS and key == glfw.KEY_ESCAPE:
        ex = True
        return         
def draw():
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_TRIANGLES)
        glColor3f(0, 0, 1)
        glVertex3f(x2,y2,0)
        glColor3f(1,0,0)
        glVertex3f(0,y1,0.0)
        glColor3f(0,1,0)
        glVertex3f(x1,y2,0)
        glEnd()
def main():
    if not glfw.init():
        return
    window = glfw.create_window(640, 480, "Lab2", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    while not glfw.window_should_close(window) and not ex:
        draw()
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()
 
if __name__ == '__main__':
    main()
