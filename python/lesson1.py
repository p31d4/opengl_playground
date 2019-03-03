"""
    Based on Lesson 1 from Nehe Productions
    https://nehe.gamedev.net/tutorial/creating_an_opengl_window_(win32)/13001/
"""

import sys
from OpenGL.GL import glViewport, glMatrixMode, glLoadIdentity, \
        glShadeModel, glClearColor, glClearDepth, glEnable, glDepthFunc, \
        glHint, glClear, GL_SMOOTH, GL_DEPTH_TEST, GL_LEQUAL, \
        GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST, GL_PROJECTION, \
        GL_MODELVIEW, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT
from OpenGL.GLU import gluPerspective
from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    """
        Ui class
    """

    def __init__(self):

        super().__init__()
        uic.loadUi('./ui_files/OpenGLScreen.ui', self)

        self.openGLWidget.resizeGL = self.resize_gl
        self.openGLWidget.initializeGL = self.initialize_gl
        self.openGLWidget.paintGL = self.paint_gl

        # Actions
        self.actionClose.triggered.connect(self.close_app)

    def close_app(self):
        """
            close app
        """
        self.close()

    def resize_gl(self, width, height):
        """
            resize window
        """

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, width / height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def initialize_gl(self):
        """
            initialize OpenGL
        """

        glShadeModel(GL_SMOOTH)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    def paint_gl(self):
        """
            paint OpenGL
        """

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
sys.exit(app.exec_())
