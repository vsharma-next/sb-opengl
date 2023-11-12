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
        glLineWidth(1)

        ### set up vertex array object for vaoRefTri ###
        self.vaoRefTri = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRefTri)

        ### set up vertex attribute ###
        positionData = [[0.8, 0.0, 0.0], [0.4, 0.6, 0.0], [-0.4, 0.6, 0.0]]
        self.vertexCountTri = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")

        ### set up vertex array object for vaoRefTri ###
        self.vaoRefSquare = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRefSquare)

        ### set up vertex attribute ###
        positionData = [
            [0.0, 0.0, 0.0],
            [0.1, 0.0, 0.0],
            [0.1, 0.1, 0.0],
            [0.0, 0.1, 0.0],
        ]
        self.vertexCountSquare = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")

    def update(self):
        glUseProgram(self.programRef)

        glBindVertexArray(self.vaoRefSquare)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertexCountTri + 20)

        glBindVertexArray(self.vaoRefTri)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertexCountTri)


Test().run()
