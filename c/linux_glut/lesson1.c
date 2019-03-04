// rust:1.78.0, libglut-dev, freeglut3-dev
#include <stdio.h>
#include <stdlib.h>
#include <GL/gl.h>  // /usr/lib/x86_64-linux-gnu/libGL.so.1.7.0, libGLU.so.1.3.1
#include <GL/freeglut.h>  // /usr/lib/x86_64-linux-gnu/libglut.so.3.12.0

// docs: lynx /tmp/OpenGL-Refpages/gl2.1/xhtml/index.html

void display_func() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    // error handling example, should be everywhere
    //-------------------------------------------------------------------------
    GLenum gl_error = GL_NO_ERROR;
    gl_error = glGetError();
    if (GL_NO_ERROR != gl_error) {
        printf("Error: %s\n", gluErrorString(gl_error));
        exit(EXIT_FAILURE);
    }
    //-------------------------------------------------------------------------

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    glutSwapBuffers();
}

void reshape_func(int w, int h) {
    glViewport(0, 0, w, h);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitContextVersion(2, 1);
    glutInitContextProfile(GLUT_CORE_PROFILE);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH);
    glutInitWindowSize(620, 620);
    glutInitWindowPosition(0, 0);
    glutCreateWindow("Lesson1");
    glutDisplayFunc(display_func);
    glutReshapeFunc(reshape_func);

    glutMainLoop();

    return EXIT_SUCCESS;
}
