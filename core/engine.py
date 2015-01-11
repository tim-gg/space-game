#
# engine.py - handles generally running the game
# can set a game resolution (iwidth, iheight) as well as a screen resolution
# the screen scales to fit
# also has a builting framerate counter
#


import pygame

def fit(surf,size):
    surf = pygame.transform.scale(surf,size)
    return surf

class Engine:
    def __init__(self):
        self.fullscreen = False
        #The screen width, what resolution the screen is scaled to
        self.swidth = 640
        self.sheight = 480
        #The interactive width, what resolution the game is actually rendered at
        self.iwidth = 320
        self.iheight = 240
        self.window = None   #The window is the actual window
        self.surface = None   #The surface is what will be displayed, most of the time draw to this
        self.blank = None
        self.running = False   #If this is set to false, the game will quit
        self.paused = False   #Not implemented, should be controlled by the world
        self.framerate = 60    #What framerate the game runs at
        self.dt = 0
        self.show_fps = True
        self.clock = None
        self.world = None   #Change what world is set to to change between scenes or modes
        self.next_tick = 0.0
    def start(self):
        """Separate from __init__ in case we want to make the object before making the screen"""
        pygame.init()
        self.make_screen()
        self.running = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("fonts/vera.ttf",12)
    def stop(self):
        self.running = False
    def pause(self):
        self.paused = True
    def unpause(self):
        self.paused = False
    def update(self):
        """One tick, according to dt"""
        self.next_tick += self.dt
        if self.world:
            while self.next_tick>0:
                self.next_tick -= 1
                self.world.update()
    def make_screen(self):
        flags = pygame.RESIZABLE|pygame.FULLSCREEN*self.fullscreen
        self.window = pygame.display.set_mode([self.swidth,self.sheight],flags)
        self.surface = pygame.Surface([self.iwidth,self.iheight]).convert()
        self.blank = self.surface.convert()
        self.blank.fill([0,0,0])
        pygame.display.set_icon(pygame.image.load("art/icons/ico.png"))
    def clear_screen(self):
        self.surface.blit(self.blank,[0,0])
    def draw_screen(self):
        showfps = self.show_fps
        self.window.fill([10,10,10])
        def draw_segment(dest,surf,pos,size):
            rp = [pos[0]*self.swidth,pos[1]*self.sheight]
            rs = [size[0]*self.swidth,size[1]*self.sheight]
            surf = fit(surf,rs)
            dest.blit(surf,rp)
        draw_segment(self.window,self.surface,[0,0],[1,1])
        if showfps:
            self.window.blit(self.font.render(str(self.clock.get_fps()),1,[255,0,0]),[0,self.window.get_height()-12])
        pygame.display.flip()