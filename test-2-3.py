from core.base import Base
from core.attribute import Attribute
from core.openGLUtils import OpenGLUtils

from OpenGL.GL import *

# render six points in a hexagon arrangement


class Test(Base):
    def initialize(self):
        print("initializing program .. ")

        ## initialize program ##
        vsCode = """
        
        in vec3 position;
        void main()
        {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
            
            }
        
        """

        fsCode = """
        
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0,1.0,0.0,1.0);
            }
        
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        ### render settings (optional) ##
        glLineWidth(4)

        ### set up vertex array object ###
        # vaoRef = glGenVertexArrays(1)
        # glBindVertexArray(vaoRef)

        ### set up vertex attribute ###
        positionData = [
            [0.8, 0.0, 0.0],
            [0.4, 0.6, 0.0],
            [-0.4, 0.6, 0.0],
            [-0.8, 0.0, 0.0],
            [-0.4, -0.6, 0.0],
            [0.4, -0.6, 0.0],
        ]
        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")

    def update(self):
        glUseProgram(self.programRef)
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)


Test().run()
