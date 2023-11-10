import pygame
import sys

from core.input import Input


class Base(object):
    def __init__(self, screenSize=[512, 512]):
        pygame.init()
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE
        )
        self.screen = pygame.display.set_mode(screenSize, displayFlags)
        pygame.display.set_caption("Graphics God")

        self.running = True
        self.clock = pygame.time.Clock()
        self.input = Input()

    def initialize(self):
        pass

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
                self.running = False

            ## update ##
            self.update()

            ## render ##
            # display image on screen
            pygame.display.flip()

            # pause if neccessary to achieve 60 FPS

        ## shutdown ##
        pygame.quit()
        sys.exit()
