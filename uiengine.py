import pygame as pg
import time
import math
import random

class Game():

    def __init__(self):

        self.all_surfaces = []

        pg.init() # start PyGame

        self.screen_width, self.screen_height = 960, 540

        self.code_running = True # true until time to stop
        self.game_running = False # game is not running when in start menu

        self.screen = pg.display.set_mode((self.screen_width, self.screen_height), pg.RESIZABLE) # create a screen with specified dimensions
        self.name = 'Monopoly: Cookie Factory Edition' # name of program
        self.icon = pg.image.load('./assets/images/icon.png').convert_alpha() # icon of program
        pg.display.set_caption(self.name) 
        pg.display.set_icon(self.icon) 

        self.baked_version_font = pg.font.Font('./assets/fonts/Kabel-Heavy.ttf', 25)
        self.baked_version_surface = self.baked_version_font.render('v0.2.0-demo', False, (255, 255, 255))


        
    def user_input(self):
        for event in pg.event.get(): # if there is a pygame event:
            if event.type == pg.QUIT: # and it is a quit event:
                self.code_running = False # stop running the python code, which results in pygame closing
            elif event.type == pg.VIDEORESIZE: # if the window is resized by the user:
                self.screen_width, self.screen_height = self.screen.get_size() # update screen width and height values
                for surface in game.all_surfaces: # for all surfaces:
                    surface.resize_event() # update their size based on the window size change
            elif event.type == pg.VIDEOEXPOSE: 
                self.screen_width, self.screen_height = self.screen.get_size()
                for surface in game.all_surfaces:
                    surface.resize_event()


    def click_event(self): # when the user clicks:
        pass

    def bake_version(self): # version number in bottom left, REMOVE ON RELEASE
        self.screen.blit(self.baked_version_surface, (self.screen_width-120, self.screen_height-25))

class Music():

    def __init__(self):

        self.min_volume = 0 # the lowest the music volume will ever reach
        self.max_volume = 0.1 # the highest the music volume will ever reach
        self.volume_up_step = 0.001 # volume fade-in speed
        self.volume_down_step = 0.002 # volume fade-out speed

        self.volume_direction = True # true for volume increase (fade-in), false for volume decrease (fade-out)
        self.volume_update_required = True # true when fade-in or fade-out in progress
        self.volume = 0.002 # start with very little volume, as to not make users deaf

    def load(self, filepath): 
        pg.mixer.music.load(filepath) # load music from the filepath provided
        pg.mixer.music.set_volume(self.volume) # set the volume to the class volume attribute
        pg.mixer.music.play() # start playing the music

    def volume_update(self):

        if self.volume_update_required == True: # if fade-in or fade-out in progress: 

            if self.volume_direction == True and self.volume < self.max_volume: # volume direction is up and not yet reached max_volume:
                self.volume += self.volume_up_step # increase volume by volume_up_step

            elif self.volume_direction == False and self.volume > self.min_volume: # volume direction is down and not yet reached min_volume:
                self.volume -= self.volume_down_step # decrease volume by volume_down_step

            else: # volume has reached max_value or min_value:
                self.volume_update_required = False # therefore volume updates not required anymore

            pg.mixer.music.set_volume(self.volume) # set volume in pygame

    def volume_direction_update(self, direction):

        self.volume_direction = direction # set the direction to the direction provided
        self.volume_update_required = True # tell volume_update() that a fade-in or fade-out is in progress

class Image_Surface():

    def __init__(self, filepath: str, percent_screen_size):

        self.percent_screen_size = percent_screen_size

        if filepath.endswith('.png'): # if image is png:
            self.original_surface = pg.image.load(filepath).convert_alpha() # create surface with alpha channel
        else: # otherwise:
            self.original_surface = pg.image.load(filepath).convert() # create surface with no alpha channel

        self.original_rect = self.original_surface.get_rect() # create surface rect
        self.original_surface_width = self.original_rect.width # get image width
        self.original_surface_height = self.original_rect.height # get image height

        self.aspect_ratio = self.original_surface_height / self.original_surface_width # calculate aspect ratio for later image rescaling

        self.resize_event() 

        game.all_surfaces.append(self) # add the surface name to all_surfaces array


    def resize_event(self):

        self.surface = pg.transform.scale(self.original_surface, ((game.screen_width * self.percent_screen_size), (game.screen_width * self.aspect_ratio * self.percent_screen_size))) # resize the surface width to full current screen width times the percent of the screen you want the surface to ocupy; resize the surface height to full current screen width times aspect ratio (to retain aspect ratio and not stretch it) times the percent of the screen you want the surface to ocopy
        
        self.rect = self.surface.get_rect() # create a new surface rect based on the resized image
        self.surface_width = self.rect.width # get the new surface width
        self.surface_height = self.rect.height # get the new surface height

class Cookie_Surface(Image_Surface):

    def __init__(self):
        start_menu.cookies.append(self) # add the cookie name to cookies array
        super().__init__('./assets/images/cookie.png', 0.05) # call the Image_Surface superclass __init__ function
        self.x_percent = random.randint(-10, 110)/100 # assign a random x position
        self.y_percent = random.randint(-10, 110)/100 # assign a random y position
        self.angle = random.randint(1, 359) # assign a random angle
        self.x_velocity = random.randint(-10, 10)/1000 # assign a random x velocity
        self.y_velocity = random.randint(-10, 10)/1000 # assign a random y velocity
        self.angle_velocity = random.randint(-10, 10) # assign a random spin velocity



class Start_Menu():
    

    def __init__(self):
        self.cookies = [] # create the array for all cookies
        self.tick = 0 # initialise tick to 0 (tick used for sine function)
        pg.mouse.set_visible(False)


    def get_cookies(self, cookie_number):
        for n in range(cookie_number): # for the number of cookies wanted:
            self.temp_cookie_name = 'cookie' + str(n) # create a ['cookie' + number] name
            self.temo_cookie_name = Cookie_Surface() # create an object instance under that name

    def loop(self):
        

        for cookie in self.cookies: # for each cookie created: 
            cookie.x_percent += cookie.x_velocity # move the cookie along x based on its velocity
            cookie.y_percent += cookie.y_velocity # move the cookie along y based on its velocity
            cookie.angle += cookie.angle_velocity # rotate the cookie based on its spin velocity

            if cookie.x_velocity > 0: # if the cookie is moving right:
                if cookie.x_percent > 1.1: # and it is right of the screen
                    cookie.x_percent -= 1.2 # bring it back to left of the screen
            else: # otherwise (if the cookie is moving left):
                if cookie.x_percent < -0.1: # and it is left of the screen
                    cookie.x_percent += 1.2 # bring it back to right of the screen

            if cookie.y_velocity > 0: # if the cookie is moving down:
                if cookie.y_percent > 1.1: # and it is below the screen
                    cookie.y_percent -= 1.2 # bring it back to above the screen
            else: # otherwise (if the cookie is moving up)
                if cookie.y_percent < -0.1: # and it is above the screen
                    cookie.y_percent += 1.2 # bring it back below the screen

            if cookie.angle_velocity > 0: # if the cookie's angle is increasing:
                if cookie.angle > 360: # and the angle is greater than 360 degrees
                    cookie.angle -= 360 # bring it back to normal range (0-360)
            else: # otherwise (if the cookie's angle is decreasing)
                if cookie.angle < 0: # and the angle is less than 0 degrees
                    cookie.angle += 360 # bring it back to normal range (0-360)

        self.tick += 0.02 # increase tick for change in sine function
        self.logo_surface = pg.transform.scale(s_logo.surface, (s_logo.surface_width * (0.2 * math.sin(self.tick) ** 2 +0.8), s_logo.surface_height * (0.2 * math.sin(self.tick) ** 2 +0.8))) # do cool math and calculate the size of the bouncing logo
        self.logo_width, self.logo_height = self.logo_surface.get_size() # get the width and height of the new resized logo


        game.screen.blit(s_cf.surface, (game.screen_width//2 - s_cf.surface_width//2, game.screen_height//2 - s_cf.surface_height//2)) # do some math that centers the cookie factory background, and blit it on the screen
        for cookie in self.cookies: # for each cookie created:
            rotated_cookie = pg.transform.rotate(cookie.surface, cookie.angle) # rotate the cookie based on its angle value
            rotated_cookie_rect = rotated_cookie.get_rect() # get the rectangle of the rotated image (for center calibration to avoid jiggling like in v0.1.0-demo)
            rotated_cookie_width, rotated_cookie_height = rotated_cookie_rect.width, rotated_cookie_rect.height # get the width and height of the image rectangle (which once divided by 2 will give the center)
            game.screen.blit(rotated_cookie, (game.screen_width * cookie.x_percent - rotated_cookie_width/2, game.screen_height * cookie.y_percent - rotated_cookie_height/2)) # do some big brain math that i don't even remember how i did but it works and that's all that matters, ok?
        
        cursor_x, cursor_y = pg.mouse.get_pos()
        
        if (game.screen_width * 0.15 - s_play_button_unpressed.surface_width//2) < cursor_x < (game.screen_width * 0.15 + s_play_button_unpressed.surface_width//2) and (game.screen_height * 0.9 - s_play_button_unpressed.surface_height//2) < cursor_y < (game.screen_height * 0.9 + s_play_button_unpressed.surface_height//2):
            game.screen.blit(s_play_button_pressed.surface, (game.screen_width * 0.15 - s_play_button_unpressed.surface_width//2, game.screen_height * 0.9 - s_play_button_unpressed.surface_height//2))
        else:
            game.screen.blit(s_play_button_unpressed.surface, (game.screen_width * 0.15 - s_play_button_unpressed.surface_width//2, game.screen_height * 0.9 - s_play_button_unpressed.surface_height//2))
        game.screen.blit(self.logo_surface, (game.screen_width//2 - self.logo_width//2, game.screen_height * 0.25 - self.logo_height//2)) # find the screen center and blit the logo
    
        game.screen.blit(s_cursor.surface, (cursor_x - s_cursor.surface_width//2, cursor_y - s_cursor.surface_width//2))


game = Game() # initialise game object
music = Music() # initialise music object
start_menu = Start_Menu() # initialise start menu object

start_menu.get_cookies(200) # make 200 cookies!


###################################
##     Loading images... 61%     ##
###################################

s_cf = Image_Surface('./assets/images/cookiefactory.jpg', 1)
s_logo = Image_Surface('./assets/images/logo.png', 0.6)
s_play_button_unpressed = Image_Surface('./assets/images/buttons/playbutton.png', 0.2)
s_play_button_pressed = Image_Surface('./assets/images/buttons/playbuttondark.png', 0.2)
s_cursor = Image_Surface('./assets/images/cursor.png', 0.04)


music.load('./assets/music/Unreal_Super_Hero_3_by_Kenet_Rez.mp3')
while game.code_running: # until pygame is asked to quit:
   
   
    game.user_input() # check for any events (like quit, window resize, click, etc.)
    music.volume_update() # update the volume of music (could also mean it staying at the same volume)
    game.screen.fill((255, 255, 255)) # set the screen to white (to cover up, or 'refresh', the last frame)
    start_menu.loop() # do the start_menu loop



    game.bake_version() # bake (i think i meant 'burn', but it is too late to change now) the version into the bottom right of the screen

    pg.display.update() # take update the screen based on everything that has happened since last screen update

    time.sleep(0.01) # game speed control (better speed control is required for smooth experience on all window sizes)

    # pygame.quit() is not required and not recommended by pygame, 
    # because pygame can successfully close by itself once python code ends
    # more info: bottom of https://www.pygame.org/docs/tut/ImportInit.html
 
