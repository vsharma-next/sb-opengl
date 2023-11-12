from core.base import Base
from core.openGLUtils import OpenGLUtils

from OpenGL.GL import *


# render a single point
class Test(Base):
    def initialize(self):
        print("Initializing Program")

        OpenGLUtils.printSystemInfo()
        ### Initializing program ###

        ## Vertex shader code ##

        vsCode = """
        
        void main()
        {
            gl_Position = vec4(1,1,1,1);
        }
        
        
        """

        fsCode = """
        
        out vec4 fragColor;
        
        void main(){
            
            fragColor = vec4(1,0,0,1);
        }
        
        
        """

        # send code to GPU and compile + store program reference

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        ### set up vertex array object ###

        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        ### render settings ###

        glPointSize(100)

    def update(self):
        # select program to use when rendering
        glUseProgram(self.programRef)

        # renders geometeric objects using selected program
        glDrawArrays(GL_POINTS, 0, 1)


Test().run()
