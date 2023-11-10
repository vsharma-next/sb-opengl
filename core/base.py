import pygame
import sys

from core.input import Input


class Base(object):
    ##
    def __init__(
        self, screenSize=[512, 512]
    ):  # screensize is an input to the constructor
        # initialize all pygame modules
        pygame.init()

        # indicate rendering details
        ## DOUBLEBUF: a rendering technique called double buffering will be used that uses TWO image buffers.
        ## The pixel data from one image buffer will be used to display on screen while the other image is used
        ## for taking in new data. When the 2nd (background) image buffer is ready, the app switches the buffers:buffer to write becomes buffer to display and vice-versa.
        ## this flip is accomplished by pygame.display.flip()

        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL

        ## initialize buffers to perform antialiasing
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)

        ## use a core OpenGL profile for cross-platform compatibility
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE
        )
        ## Create and display the window
        self.screen = pygame.display.set_mode(screenSize, displayFlags)

        ## set the text that appears in the title bar of the window
        pygame.display.set_caption("Graphics God")

        ## determine if the main loop is active
        self.running = True
        ## manage tile-related data and operations
        self.clock = pygame.time.Clock()

        ## Get the input class constructor
        self.input = Input()

    ## implemented by children classes
    def initialize(self):
        pass

    ## implemented by children classes
    def update(self):
        pass

    def run(self):
        ## Startup ##

        self.initialize()

        ## main loop
        while self.running:
            ## Process input from peripherals ##
            self.input.update()

            if self.input.quit:
                print("App closing")
                self.running = False

            ## update ##
            self.update()

            ## render ##
            # display image on screen
            pygame.display.flip()

            # pause if neccessary to achieve 60 FPS
            self.clock.tick(60)

        ## shutdown ##
        pygame.quit()
        sys.exit()
