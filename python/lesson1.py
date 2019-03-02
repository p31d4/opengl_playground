# based on http://nehe.gamedev.net/tutorial/creating_an_opengl_window_(win32)/13001/
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5 import QtWidgets as qWidget
from PyQt5 import uic
import sys


class Ui(qWidget.QMainWindow):

    def __init__(self, *args):
        
        super(Ui, self).__init__()
        uic.loadUi('./ui_files/OpenGLScreen.ui', self)
        self.title = 'Lesson1'
        
        self.openGLWidget.resizeGL = self.resizeGL
        self.openGLWidget.initializeGL = self.initializeGL
        self.openGLWidget.paintGL = self.paintGL
        
        # Actions
        self.actionClose.triggered.connect(self.closeApp)

    def closeApp(self):
        self.close()

    def resizeGL(self, width, height):

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, width / height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity()

    def initializeGL(self):

        glShadeModel(GL_SMOOTH)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    def paintGL(self):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

app = qWidget.QApplication(sys.argv)
window = Ui()
window.show()
sys.exit(app.exec_())
