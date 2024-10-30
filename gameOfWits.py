# Setup
# Menu
# Typewriter
# Overworld
# Invintory
# Hints
# Savegame
# Cheatcodes




# Import Modules and Initialise
import os
import math
import moviepy.video
import moviepy.video.VideoClip
import pygame
import random as rand
from pygame import mixer
from moviepy.editor import *
import moviepy
from varname import nameof

pygame.init()

#Some usefull defenitions for you 
class time:
    def sleep(time):
        pygame.time.wait(time*1000)

def tf():
    return bool(rand.getrandbits(1))

def rot_center(image, angle):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect()

    return rotated_image, new_rect

#Button Class
        
class Button:
    #Init
    def __init__(self, x, y, image, tilted=False):
        self.image = image
        self.x = x
        self.y = y
        if not tilted:
            self.rect = self.image.get_rect(center=(self.x, self.y))
        elif tilted:
            self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.clicked = False
        
    #Draw the button and return wether it has been clicked once
    def draw(self):
        action = False
        screen.blit(self.image, self.rect)

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]== 1 and self.clicked == False:
                self.clicked = True
                action = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action
    
    def rect(self):
        return self.rect

#########################################################################################################

"--Menu Effect--"

blue_XL = VideoFileClip("VIDS/interpol-XL.mp4") # (or .webm, .avi, etc.)



def getVidioSnap(clip, t, srf=None, snip_off_end=0):
    clip_duration = clip.duration - snip_off_end
    while t>clip_duration:
        t-=clip_duration

    frame = clip.get_frame(t=t)  # t is the time in seconds
    
    if srf is None:
        # Transpose the array and create the Pygame surface
        return pygame.surfarray.make_surface(frame.swapaxes(0, 1))
    else:
        pygame.surfarray.blit_array(srf, frame.swapaxes(0, 1))
        return srf

video_element = getVidioSnap(clip=blue_XL, t=0)
video_element_frame = 0

"--Menu buttons--"

menufont = pygame.font.Font("TNR.ttf", 32)

New = menufont.render("New Game", 1, (255,255,255))
New_button = Button(212, 450, New)

Load = menufont.render("Load Game", 1, (255,255,255))
Load_button = Button(425, 450, Load)

Load_grey = menufont.render("Load Game", 1, (100,100,100))
Load_grey_button = Button(425, 450, Load_grey)


Help = menufont.render("Help", 1, (255,255,255))
Help_button = Button(637, 450, Help)

Credits = menufont.render("Credits", 1, (255,255,255))
Credits_button = Button(212, 550, Credits)

Knowledge = menufont.render("Knowledge", 1, (255,255,255))
Knowledge_button = Button(425, 550, Knowledge)

Exit = menufont.render("Exit", 1, (255,255,255))
Exit_button = Button(637, 550, Exit)

"--Credits--"
credits_scrolled_pixles = 0

creditfont = pygame.font.Font("TNR.ttf", 26)

creditmusic = None

creditslist=[]
creditslist.append(Credit0 := pygame.font.Font("TNR.ttf", 36).render("--CREDITS--", 1, (255, 255,255)))
creditslist.append(Credit1 := creditfont.render("Programed by Gabriel van Rijn Jordaan", 1, (255, 255,255)))
creditslist.append(Credit2 := creditfont.render("Lots of the location images by Gabe with IMG2GO image generation", 1, (255, 255,255)))
creditslist.append(Credit3 := creditfont.render("Some icons and sprites by Gabe with IMG2GO", 1, (255, 255,255)))
creditslist.append(Credit4 := creditfont.render("Frame interpolation gifs made by Gabe with software from runway", 1, (255, 255,255)))
creditslist.append(Credit5 := creditfont.render("Some icons by flaticon.com", 1, (255, 255,255)))
creditslist.append(Credit6 := creditfont.render("Some sound effects by pixbay and mixkit", 1, (255, 255,255)))
creditslist.append(Credit7 := creditfont.render("Thanks to florasonic for the hint noise and to Freepick for the button", 1, (255, 255,255)))
creditslist.append(Credit8 := creditfont.render("Arrow icon made by O.moonsttd", 1, (255, 255,255)))
creditslist.append(Credit9 := creditfont.render("Song: \"The Wrong Cat\" by Alexandra Harwood", 1, (255, 255,255)))
creditslist.append(Credit10:= creditfont.render("Song: \"Peer Gynt Suite No. 1, Op. 46 - Morning Mood\" by Edvard Grieg", 1, (255, 255,255)))
creditslist.append(Credit11:= creditfont.render("Music: \"State Anthem of the Russian Federation\" by Alexandr Alexandrov", 1, (255, 255,255)))
creditslist.append(Credit12:= creditfont.render("Lyrics: \"State Anthem of the Russian Federation\" by Sergei Mikhalkov", 1, (255, 255,255)))
creditslist.append(Credit13:= creditfont.render("Melody: \"Die Stem\" by Marthinus Lourens de Villiers", 1, (255, 255,255)))
creditslist.append(Credit14:= creditfont.render("Lyrics: \"Die Stem\" by Cornelis Jacobus Langenhoven", 1, (255, 255,255)))
creditslist.append(Credit15:= creditfont.render("Song: \"The Yellow Rose Of Texas\" by Cornelis Mitch Miller", 1, (255, 255,255)))

#Scene 0 - Creation of Stuff

#Create Screen
screen = pygame.display.set_mode((850, 800))

# Title and Icon
pygame.display.set_caption("Menu")
icon = pygame.image.load("IMAGES/virus.png")
pygame.display.set_icon(icon)


#######################
###################################
###############################################
############################################################
###########################################################################
#################################################################################################
#########################################################################################################
#########################################################################################################
###################################################################################################
##########################################################################
#########################################################
############################################ 
######################
############


## TYPEWRIGHTER "CLASS"

#The placeholder variable that shows what charecter is being added
tothis = 0

#Logical values for lines BEING THERE AND COMPLETE ("" for false "Text" for true)
charatextline = [""]*10


#Function
def chara_print_begin(text, line, wait=0.5, xcoord=100, ycoord=100, speedbonus=2, size=32, do_click=True, do_ding = True, ding_file = "SOUNDS/return.wav", click_files_without_number = "write", insta=False, sound="Normal", volume=0.2, speedmultiplier=0.02, mute_lightly=True):

    #Globalise
    global tothis
    global charatextline
    global finished_printing

    finished_printing = True

    #if you are (not not) supposed to do something
    if (charatextline[line-1] == "" and line != 0) or charatextline[line]!="":
        pass
    #Do it
    else:

        #Skip?
        if insta:
            charatextline[line] = text
            tothis = 0


        #Print everything you need that's done
        charafont = pygame.font.Font("TNR.ttf", size)    
        for i in range(len(charatextline)):
            if charatextline[i] != "":
                printing = charafont.render(charatextline[i], True, (255, 255, 255))
                screen.blit(printing,(xcoord,ycoord+(size*i)))

        #If not finished     
        if charatextline[line] == "":
            printed=text[0:tothis]
            printing = charafont.render(printed, True, (255, 255, 255))
            screen.blit(printing, (xcoord, ycoord+(size*line)))

            #If not complete
            if tothis < len(text)+1:                
                #add a charicter
                tothis = tothis+1
                finished_printing = False

                #And play the correct sound    
                if tothis > 1 and text[tothis-2] != " " and do_click:
                    if sound=="Normal":
                        click = mixer.Sound("".join(["SOUNDS/",(click_files_without_number+str(rand.randint(1,2))+".wav")]))
                        click.set_volume(volume)
                    else:                        
                        click=mixer.Sound(sound)
                        click.set_volume(volume)
                    if not (mute_lightly and tf()):
                        click.play()

                #Then wait to make it look natural
                pygame.time.wait(int((speedmultiplier*((rand.randint(3,4))-speedbonus)*1000)))
                

            #Otherwise finish off this line and make a return-y sound
            else:
                charatextline[line] = text
                pygame.time.wait(int((0.1*1000)))
                tothis=0
                if text != " " and do_ding:
                    ding = mixer.Sound(ding_file)
                    ding.set_volume(volume)
                    ding.play()
                pygame.time.wait(int((wait*1000)))
    

def keepinplace(lastline, size=32, xcoord=100, ycoord=100):
    if charatextline[lastline]!="":
        charafont = pygame.font.Font("TNR.ttf", size)    
        for i in range(len(charatextline)):
            if charatextline[i] != "":
                printing = charafont.render(charatextline[i], True, (255, 255, 255))
                screen.blit(printing,(xcoord,ycoord+(size*i)))



#Clear Lines Of Chara
def clearlines(start, stop, wait=0):
    global charatextline
    global tothis
    tothis = 0
    for i in range(start,stop+1):
        charatextline[i] = ""
        pygame.time.wait(int((wait*1000)))

####################################################################################################################################

# Haha me just being too lazy to actually make a class like a real programmer lol
tothislazy = 0
charatextlinelazy = [""]*10

def chara_print_lazy(text, line, wait=0.5, xcoord=100, ycoord=100, speedbonus=2, size=32, do_click=True, do_ding = True, ding_file = "SOUNDS/return.wav", click_files_without_number = "write", insta=False, sound="Normal", volume=0.2, speedmultiplier=0.02, mute_lightly=True, colour=(0,0,0)):



    #Globalise
    global tothislazy
    global charatextlinelazy

    #if you are (not not) supposed to do something
    if (charatextlinelazy[line-1] == "" and line != 0) or charatextlinelazy[line]!="":
        pass
    #Do it
    else:

        #Skip?
        if insta:
            charatextlinelazy[line] = text
            tothislazy = 0


        #Print everything you need that's done
        charafont = pygame.font.Font("TNR.ttf", size)    
        for i in range(len(charatextlinelazy)):
            if charatextlinelazy[i] != "":
                printing = charafont.render(charatextlinelazy[i], True, colour)
                screen.blit(printing,(xcoord,ycoord+(size*i)))

        #If not finished     
        if charatextlinelazy[line] == "":
            printed=text[0:tothislazy]
            printing = charafont.render(printed, True, colour)
            screen.blit(printing, (xcoord, ycoord+(size*line)))

            #If not complete
            if tothislazy < len(text)+1:                
                #add a charicter
                tothislazy = tothislazy+1

                #And play the correct sound    
                if tothislazy > 1 and text[tothislazy-2] != " " and do_click:
                    if sound=="Normal":
                        click = mixer.Sound("SOUNDS/"+click_files_without_number+str(rand.randint(1,2))+".wav")
                        click.set_volume(volume)
                    else:                        
                        click=mixer.Sound(sound)
                        click.set_volume(volume)
                    if not (mute_lightly and tf()):
                        click.play()

                #Then wait to make it look natural
                pygame.time.wait(int((speedmultiplier*((rand.randint(3,4))-speedbonus)*1000)))
                

            #Otherwise finish off this line and make a return-y sound
            else:
                charatextlinelazy[line] = text
                pygame.time.wait(int((0.1*1000)))
                tothislazy=0
                if text != " " and do_ding:
                    ding = mixer.Sound(ding_file)
                    ding.set_volume(volume)
                    ding.play()
                pygame.time.wait(int((wait*1000)))
    

def keepinplacelazy(lastline, size=32, xcoord=100, ycoord=100, colour=(0,0,0)):
    if charatextlinelazy[lastline]!="":
        charafont = pygame.font.Font("TNR.ttf", size)    
        for i in range(len(charatextlinelazy)):
            if charatextlinelazy[i] != "":
                printing = charafont.render(charatextlinelazy[i], True, colour)
                screen.blit(printing,(xcoord,ycoord+(size*i)))



#Clear Lines Of Chara
def clearlineslazy(start, stop, wait=0):
    global charatextlinelazy
    global tothislazy
    tothislazy = 0
    for i in range(start,stop+1):
        charatextlinelazy[i] = ""
        pygame.time.wait(int((wait*1000)))

#######################
###################################
###############################################
############################################################
###########################################################################
#################################################################################################
#########################################################################################################
#########################################################################################################
###################################################################################################
##########################################################################
#########################################################
############################################ 
######################
############
    
#Overworld "CLASS"

class Photo:
    def __init__(self, file):
        self.file = file

    def show(self):
        screen.blit(pygame.image.load(self.file), (0,0))


def overworld_rectangle():
    pygame.draw.rect(screen, (255,255,255), (30, 615, 790, 165), 2)


def overworld_print(textus, linus, waitus=0.1, xcoordus=55, ycoordus=640, soundus=None, icon=None, loud=False, volumeboost=0):
    if soundus==None:
        do_clickus=False
    else:
        do_clickus=True

    if icon!=None:
        global charatextline
        if not ((charatextline[linus-1] == "" and linus != 0) or charatextline[linus]!=""):
            xcoordus=xcoordus+100
            bliting_icon = pygame.image.load(icon)
            screen.blit(bliting_icon, bliting_icon.get_rect(center=(100, 700)))

    chara_print_begin(text=textus, wait=waitus, line=linus, speedbonus=2, xcoord=xcoordus, ycoord=ycoordus, size=16, do_click=do_clickus, do_ding=False, sound=soundus, mute_lightly=not loud, volume=0.2+volumeboost)


def overworld_keep(lastline, iconades=None):
    if charatextline[lastline]!="":
        xco=55

        if iconades != None:
            xco = xco + 100
            bliting_icon = pygame.image.load(iconades)
            screen.blit(bliting_icon, bliting_icon.get_rect(center=(100, 700)))
        


        keepinplace(lastline, 16, xco, 640)


advancingbutton = Button(780, 740, pygame.image.load("IMAGES/DoubleYou.png"))

def advancing(line):
    GIT_GIT_GIT_GIT_GOo = False

    if charatextline[line]!="":
        if pygame.key.get_pressed()[pygame.K_w] or advancingbutton.draw():
            GIT_GIT_GIT_GIT_GOo = True
        
    return GIT_GIT_GIT_GIT_GOo


def displaymouse():
    mouse = pygame.image.load("IMAGES/Mouse.png")
    screen.blit(mouse, (760, 715))



class Clickable:
    def __init__(self, upper_left, bottom_right):
        self.upper_left = upper_left
        self.bottom_right = bottom_right

        self.low_x = upper_left[0]
        self.high_x = bottom_right[0]

        self.low_y = upper_left[1]
        self.high_y = bottom_right[1]

        self.clickedi=False
        

    def clicked(self):
        action = False
        if pygame.mouse.get_pos()[0] > self.low_x and pygame.mouse.get_pos()[0]<self.high_x and pygame.mouse.get_pos()[1]>self.low_y and pygame.mouse.get_pos()[1]<self.high_y and finished_printing and Focus_Object==None and not inv.get_open() and cooldownmisc==0 and inv.get_dirty()==0 and not (pygame.mouse.get_pos()[1]<82 and pygame.mouse.get_pos()[1]>20 and pygame.mouse.get_pos()[0]<830 and pygame.mouse.get_pos()[0]>770):
            if pygame.mouse.get_pressed()[0]== 1 and self.clickedi == False:
                self.clickedi = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clickedi = False
        return action
    
    def dev_show_hitbox(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.low_x, self.low_y, self.high_x-self.low_x, self.high_y-self.low_y), 2)

#######################
###################################
###############################################
############################################################
###########################################################################
#################################################################################################
#########################################################################################################
#########################################################################################################
###################################################################################################
##########################################################################
#########################################################
############################################ 
######################
############

# Invintory Class

def printininvabridged(item, i):

    while i>=40:
        i-=40    
                
    if i<=9:
        charafont = pygame.font.Font("TNR.ttf", 30)  
        blitting = charafont.render(item.name, True, (0,0,0))
        btng = Button(125, 170+38*i, blitting, True)
        if btng.draw():
            inv.viewing_item = item
        #screen.blit(blitting, (115, 160+38*i))
    elif i<=19:
        charafont = pygame.font.Font("TNR.ttf", 30)  
        blitting = charafont.render(item.name, True, (0,0,0))
        btng = Button(275, 170+38*(i-10), blitting, True)
        if btng.draw():
            inv.viewing_item = item
        #screen.blit(blitting, (265, 160+38*(i-10)))


    elif i<=29:
        charafont = pygame.font.Font("TNR.ttf", 30)  
        blitting = charafont.render(item.name, True, (0,0,0))
        btng = Button(425, 170+38*(i-20), blitting, True)
        if btng.draw():
            inv.viewing_item = item
        #screen.blit(blitting, (415, 160+38*(i-20)))

    elif i<=39:
        charafont = pygame.font.Font("TNR.ttf", 30)  
        blitting = charafont.render(item.name, True, (0,0,0))
        btng = Button(575, 170+38*(i-30), blitting, True)
        if btng.draw():
            inv.viewing_item = item
        #screen.blit(blitting, (565, 160+38*(i-30)))

class item():
    def __init__(self, name="", disc_line_1="", disc_line_2="", junk=True, usefull=True, func=None, usetext1="", usetext2="", consumable=False, disc_line_3="", disc_line_4=""):
        self.name = name
        self.disc_line_1 = disc_line_1
        self.disc_line_2 = disc_line_2
        self.disc_line_3 = disc_line_3
        self.disc_line_4 = disc_line_4
        self.junk = junk
        self.usefull=usefull
        self.func=func
        self.usetext1=usetext1
        self.usetext2=usetext2
        self.itemstate="unused"
        self.consumable=consumable

    def display(self):

        if self.itemstate=="unused":
            charafont = pygame.font.Font("TNR.ttf", 30)  

            blitting = charafont.render(self.disc_line_1, True, (0,0,0))
            screen.blit(blitting, (125, 170))

            blitting = charafont.render(self.disc_line_2, True, (0,0,0))
            screen.blit(blitting, (125, 200))

            blitting = charafont.render(self.disc_line_3, True, (0,0,0))
            screen.blit(blitting, (125, 230))

            blitting = charafont.render(self.disc_line_4, True, (0,0,0))
            screen.blit(blitting, (125, 260))

            
            if self.junk:
                discard = Button(525,470, charafont.render("Discard", True, (0,0,0)))
                if discard.draw():
                    for i in inv.items:
                        if i.name==self.name:
                            inv.items.remove(i)
                            inv.viewing_item=None
                            break

            if self.usefull:
                use = Button(425,470, charafont.render("Use", True, (0,0,0)))
                if use.draw():
                    self.itemstate="using"
                    self.func()
                    if self.consumable:
                        for i in inv.items:
                            if i.name==self.name:
                                inv.items.remove(i)
                                break

            back = Button(325,470, charafont.render("Back", True, (0,0,0)))
            if back.draw():
                inv.viewing_item = None
    
        elif self.itemstate=="using":
            pygame.draw.rect(screen,(199,199,199),(100,50,650,500))
            pygame.draw.rect(screen,(0,0,0),(100,50,650,500), 10)

            chara_print_lazy(self.usetext1, 0, 0, 133, 80)
            chara_print_lazy(self.usetext2, 1, 0, 133, 80)
            keepinplacelazy(1, 32, 133, 80)
            

            backtoinv=Button(700, 500, pygame.image.load("IMAGES/DoubleYou.png"))
            if backtoinv.draw() or pygame.key.get_pressed()[pygame.K_w]:
                inv.viewing_item=None
                self.itemstate="unused"
                clearlineslazy(0,1)



def biltongfunc():
    print("YOU ATE THE [biltong]")
biltong = item("Biltong", "A yummy South African Snack", "", True, True, biltongfunc, "Munch munch munch. Delicious...", "Plus some ammount of heath I guess...", True)

def babotifunc():
    print("BABOTI")
baboti = item("Baboti", "A yummy South African meal", "", True, True, babotifunc, "Munch munch munch. BABOTI...", "Plus some ammount of heath I guess...", True)

def vetkoekfunc():
    print("VETKOEK")
vetkoek = item("Vetkoek", "A yummy South African thing^ck", "", True, True, vetkoekfunc, "Munch munch munch. VETKOEK...", "Plus some ammount of heath I guess...", True)

shock = item("Shock Baton", "Shock batons were invented in 2137", "as a way around bulletproof armour. They are", False, False, disc_line_3="a close range and less costly alternative to ", disc_line_4="piercing bullets. This one is civilian grade.")

class invintory():
    items = []
    money = 10
    armour = "None"

    viewing_item = None

    page=1

    def __init__(self):
        self.reading=False
        self.invintory_is_dirty = 0

    def get_open(self):
        return self.reading
    
    def get_dirty(self):
        return self.invintory_is_dirty

    def avalable(self):
        if self.reading:
            Invintory_Button = Button(720, 80, pygame.image.load("IMAGES/X_out.png"))

            pygame.draw.rect(screen,(199,199,199),(100,50,650,500))
            pygame.draw.rect(screen,(0,0,0),(100,50,650,500), 10)

            charafont = pygame.font.Font("TNR.ttf", 30) 

            try:
                if country=="Texas":
                    money_symb = "$"
                    
                elif country=="Russia":
                    money_symb="₽"
                else:
                    money_symb="R"
            except:
                money_symb="R"

            
            blitting = charafont.render("Money:"+money_symb+str(inv.money), True, (0,0,0))
            screen.blit(blitting, (115, 65))

            blitting = charafont.render("Armour:"+inv.armour, True, (0,0,0))
            screen.blit(blitting, (367, 65))

            blitting = charafont.render("Items and weapons:", True, (0,0,0))
            screen.blit(blitting, (115, 125))


            if len(inv.items)>(35*(inv.page+1)) and inv.viewing_item==None:
                right = charafont.render("->", True, (0,0,0))
                rightb = Button(710, 515, right)
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    inv.page+=1
                if rightb.draw():
                    inv.page+=1


            if inv.page !=1 and inv.viewing_item==None:
                left = charafont.render("<-", True, (0,0,0))
                leftb = Button(660, 515, left)

                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    inv.page-=1
                if leftb.draw():
                    inv.page-=1
            
            if inv.viewing_item==None:
                for item, i in zip(inv.items, range(len(inv.items))):

                    if 0+(40*(inv.page-1))<=i<=39+(40*(inv.page-1)):
                        printininvabridged(item,i)

            if inv.viewing_item!=None:
                inv.viewing_item.display()



            if Invintory_Button.draw():
                self.reading=False
                self.invintory_is_dirty = 30
            

        else:
            Invintory_Button = Button(800, 50, pygame.image.load("IMAGES/INV.png"))
            if Invintory_Button.draw():
                self.reading=True
            if self.invintory_is_dirty>0:
                self.invintory_is_dirty-=1
        
inv=invintory()
        

#######################
###################################
###############################################
############################################################
###########################################################################
#################################################################################################
#########################################################################################################
#########################################################################################################
###################################################################################################
##########################################################################
#########################################################
############################################ 
######################
############

# "Hints"

hinting = False
cooldownmisc=0
def hint():
    global hinting
    global cooldownmisc

    if not hinting and cooldownmisc==0 and not inv.get_open() and inv.get_dirty()==0:
        hintbutton = Button(720, 53, pygame.image.load("IMAGES/hint.png"))
        if hintbutton.draw():
            hinting=True
            compchime = mixer.Sound("SOUNDS/compchime.mp3")
            compchime.play()
            cooldownmisc = 60
    elif hinting and not inv.get_open() and inv.get_dirty()==0:
        hintbutton = Button(720, 53, pygame.image.load("IMAGES/X_out_circle.png"))
        if hintbutton.draw() and cooldownmisc==0:
            hinting=False
            cooldownmisc = 60

    if cooldownmisc!=0:
        cooldownmisc-=1
    return hinting

def W_hint():
    if hint():
        screen.blit(pygame.transform.scale_by(pygame.transform.rotate(pygame.image.load("IMAGES/Arrow.png"), 90), 0.2), (640, 690))

#######################
###################################
###############################################
############################################################
###########################################################################
#################################################################################################
#########################################################################################################
#########################################################################################################
###################################################################################################
##########################################################################
#########################################################
############################################ 
######################
############


def savegame():
    SAVING_VARIABLES = ["scene", "subscene", "country", "field", "lcfield", "Focus_Object", "hasnotplayedmusic", "goal", "inv.money",
                        "inv.armour", "inv.items"]


    for variable_number in range(len(SAVING_VARIABLES)):   # Plz forgive, the modle[sic] is crap
        try:
            File_object = open("SAVES/"+SAVING_VARIABLES[variable_number]+".txt","w")
            File_object.write(str(globals()[SAVING_VARIABLES[variable_number]]))
            File_object.close()
        except:
            File_object = open("SAVES/"+SAVING_VARIABLES[variable_number]+".txt","w")
            File_object.write(str("Ome wa mau shinderu nani baka konichiwa hich ni san shi go roku sheeeeeeesh hach Q jew he he shogun"))
            File_object.close()

    
    File_object = open("SAVES/"+"inv.items.txt","w")
    File_object.write(str(inv.items))
    File_object.close()
    File_object = open("SAVES/"+"inv.money.txt","w")
    File_object.write(str(inv.money))
    File_object.close()
    File_object = open("SAVES/"+"inv.armour.txt","w")
    File_object.write(str(inv.armour))
    File_object.close()


        
"""""""""""""VALUES FOR CHEAT CODE BUUG FIXES"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
if True:
    field="Physics"
    lcfield="physics"
    country="South Africa"


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


#Start running, set the opening scene, begin loop

running = True

scene = "Opening Animation(s0)"
scene = "menu"



subscene = -1

Focus_Object = None

hasnotplayedmusic=True

clock = pygame.time.Clock()

#########################################################################################################

while running:
    

    #Fill the screen/background
    screen.fill((0,0,0))
    
    ##EVENTS
    for event in pygame.event.get():

        #Quit?
        if event.type == pygame.QUIT:
            pygame.quit()

        #Keys
        if event.type == pygame.KEYDOWN:
            #Skip 0th Screen?
            if event.key==pygame.K_q:
                savegame()
            if event.key == pygame.K_s:
                if scene == "Opening Animation(s0)":
                    scene = "Opening Animation(s1)"
                    clearlines(0, 8)
                try:
                    if scene=="Opening Animation %s"%country:
                        clearlines(0, 8)
                        scene= "Field Picker"
                        text = [""]*19
                        text[0] = "Click on a field to learn more about it, than select it by clicking \"pick\""
                except:
                    pass
            if event.key == pygame.K_m:
                if scene=="Wake up (ZA)":
                    scene="Car (ZA)"
                    subscene=-1
                    field="Physics"
                    lcfield="physics"
                    country="South Africa"
            if event.key == pygame.K_n:
                if scene=="Wake up (ZA)":
                    scene="Briefing"
                    subscene=-1
                    field="Physics"
                    lcfield="physics"
                    country="South Africa"
            if event.key==pygame.K_d:
                clearlines(0, 8)
                scene = "Wake up (ZA)"

        if event.type== pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    #########################################################################################################

    if scene=="menu":

        if subscene==-1:

            if video_element_frame>(blue_XL.duration-0.8):
                video_element_frame-=(blue_XL.duration-0.8)

            screenshot = getVidioSnap(clip=blue_XL, t=video_element_frame, srf=video_element, snip_off_end=0.8)

            screenshotsmall = pygame.transform.rotozoom(screenshot, 0, 0.5)

            screen.blit(screenshotsmall, (244, 0))
            video_element_frame+=1/60


            fat_transparent_rectangle = pygame.Surface((370,370))
            fat_transparent_rectangle.set_alpha(150)
            fat_transparent_rectangle.fill((0,0,0))

            #screen.blit(fat_transparent_rectangle, (200,0))

            pygame.draw.circle(screen, (0,0,0),(424,182), 245, 85)

            #screen.blit((pygame.font.Font("TNR.ttf", 16).render(str(video_element_frame), True, (255,255,255))),(0,0))

            if New_button.draw():
                scene = "Opening Animation(s0)"

            if len(os.listdir("SAVES")) != 1:

                if Load_button.draw():
                    subscene = "Load"
            else:
                Load_grey_button.draw()

            if Help_button.draw():
                subscene="Help"

            elif Credits_button.draw():
                subscene="Credits"

            elif Knowledge_button.draw():
                subscene="Knowlage"

            elif Exit_button.draw():
                pygame.quit()

        if subscene=="Credits":
            credits_scrolled_pixles+=0.5

            for i in range(len(creditslist)):
                screen.blit(creditslist[i], (20,(credits_scrolled_pixles-50-(50*i))))

            if creditmusic==None:
                try:
                    if country=="South Africa":
                        pygame.mixer.music.load("SOUNDS/_Die Stem van Suid-Afrika_ - National Anthem of South Africa.mp3")
                    if country=="Russia":
                        pygame.mixer.music.load("SOUNDS/Roccia.mp3")
                    if country=="Texas":
                        pygame.mixer.music.load("SOUNDS/The Yellow Rose of Texas - Texan Patriotic Song.mp3")
                    creditmusic = 1
                except:
                    creditmusic = rand.choice(["SOUNDS/_Die Stem van Suid-Afrika_ - National Anthem of South Africa.mp3","SOUNDS/Roccia.mp3","SOUNDS/The Yellow Rose of Texas - Texan Patriotic Song.mp3"])
                    pygame.mixer.music.load(creditmusic)

                pygame.mixer.music.play(-1)

            if credits_scrolled_pixles>(930+(50*len(creditslist))):
                credits_scrolled_pixles=0
                pygame.mixer.music.fadeout(4000)
                subscene = -1
                creditmusic=None


        "Knowledge"

        "Help"

        "Load"










        





































    #Print out intro 0th screen
    if scene == "Opening Animation(s0)":
        if hasnotplayedmusic:
            pygame.mixer.music.load("SOUNDS/wind.mp3")
            pygame.mixer.music.play(-1) 
            hasnotplayedmusic=False    


        #Print out all lines
        chara_print_begin("The year is 2147.", 0, wait=2, speedbonus= 1)
        chara_print_begin("The wars of the 21st century are over,",1)
        chara_print_begin("and the world enjoys peace and prosperity.", 2, 2.2)
        chara_print_begin(" ", 3)
        chara_print_begin("Five main superpowers rule the world:", 4, 1.2)
        chara_print_begin("Russia, South-Africa, The Republic of Texas,", 5, 0.2)
        chara_print_begin("(containing 7 southern states that seperated",6, speedbonus=2, wait=0)
        chara_print_begin("from the US in the late 21st century,)",7, 1, 100, 100, 2)
        chara_print_begin("India, and China.",8, 2)

        #Skip notice
        if charatextline[0] == "":
            screen.blit((pygame.font.Font("TNR.ttf", 20).render("Press S to skip forward.",True,(255,255,255))), (20, 770))

        #Next
        if charatextline[8] != "":
            scene = "Opening Animation(s1)"
            clearlines(0, 8)
            hasnotplayedmusic=True

    #Second Screen
    if scene == "Opening Animation(s1)":
        chara_print_begin("You are from one of these nations:", 0, 1.3)

        if charatextline[0] != "":
            scene = "Nationpicker"
            screen.fill((0,0,0))
            pygame.display.update()
    
    ######################################################################################################

    #Nationpicker Loops

    #If picking nation
    if scene == "Nationpicker":

        #SET UP SCENE IF NOT ALREADY
        try:
            za
        except:
            za = pygame.image.load("IMAGES/south-africa.png")

            russia = pygame.image.load("IMAGES/russia.png")

            texas = pygame.image.load("IMAGES/texas.png")

            buttonfont = pygame.font.Font("TNR.ttf", 32)

            country = ""

            buttontext = buttonfont.render(" ", True, (255, 255, 255))

            za_button = Button(225, 690, za)

            rus_button = Button(425, 690, russia)

            tex_button = Button(625, 690, texas)

            pick_button = Button(700, 600, buttontext)

            #Default Picker Lore Text
            text = [""]*19
            text[0] = "Click on a country to learn more about it, than select"
            text[1] = ""
            text[2] = "it by clicking \"pick\"."
            text[3] = ""
            text[4] = "Make sure to read all the lore before proceding!!!"

            for i in range(14):
                text[i+5] = ""

            sisma = 32

            hasreadrussialore, hasreadtexaslore, hasreadzalore = False, False, False
        

        #Get Mouse Pos
        PICKER_MOUSE_POS = pygame.mouse.get_pos()

        #Get text "elements"
        printinfotext = [""]*19
        for i in range(19):
            printinfotext[i] = pygame.font.Font("TNR.ttf", sisma).render(text[i],  True, (255, 255, 255))
        

        #Blit said elements
        for i in range(19):
            screen.blit(printinfotext[i], (20+3*sisma-50, (20+18*i+2*sisma-36)))


        #Make a box for the buttons
        pygame.draw.rect(screen, (255,255,255), (90, 625, 700, 125), 2)

        #Country Change Buttons
        if za_button.draw():
            sisma = 18
            text[0] ="South Africa has a sad history, but its issues are (mostly) behind it. In the mid-21st century, it became a"
            text[1] ="communist dictatorship and instituted the second apartheid. This lasted for 51 years, before a revolution"
            text[2] ="spirred on by religeous revival crushed the tyranical regieme and instituted a new political party:"
            text[3] ="The Verenigde."
            text[4] ="Shortly after the reformation of the Republic of South Africa, an important discovery was made which"
            text[5] ="launched this nation to new heights of prosparity never before seen --Not even in the 19-hundreds--"
            text[6] ="This discovery was a naturaly occurring chemical element called pretorium, which was named after the"
            text[7] ="home city of the miner who unerthed the first deposit. Pretorium is located on the periodic table's island"
            text[8] ="of stability, it is very light, and excelent for making alloys of all types. A complete monopoly on "
            text[9] ="pretorium has made south africa very wealthy."
            text[10]=""
            text[11]="You will start the game as a Verenigde veteren and reasercher -- as such, you will begin with"
            text[12]="extra money, en 'n bitjie bleddie lekker kos! (Soos Biltong)"
            text[13]=""
            text[14]="Choosing South Africa also may has its downsides, as your heroics during the civil war have made you"
            text[15]="hated by the surviving members of the old party. Expect terror attacks."
            text[16]=""
            text[17]=""
            text[18]=""
            country = "South Africa"
            hasreadzalore = True

        if rus_button.draw():
            sisma = 18
            text[0]= "Russia has adopted a new political and economic policy called Volkovisim, which is a right-wing"
            text[1]= "political phylosophy that combindes the best elements of capitalisim, socialisim, "
            text[2]= "and a constitutional republic. Volkovisim has been extremely sucsessful and has resulted in"
            text[3]= "Russia becoming a paragon of the prosparity that marks the 22nd century."
            text[4]= "Its close connections with South Africa through BRICS have given Russia easy access to pretorium,"
            text[5]= "enabeling it to become the world's leader in technology -- especially weapons technology"
            text[6]= ""
            text[7]= "As a Russian spy and reasercher, you will begin the game with some extra pretorium based"
            text[8]= "technology, and some nice Russian food from your Babushka"
            text[9]= ""
            text[10]=""
            text[11]=""
            text[12]=""
            text[13]=""
            text[14]=""
            text[15]=""
            text[16]=""
            text[17]=""
            text[18]=""
            country = "Russia"
            hasreadrussialore = True

        if tex_button.draw():
            sisma = 18
            text[0]= "When sombody says \"America\" in the year 2147, they no longer mean the United States."
            text[1]= "The American Republic of Texas (A*R*T) is essentialy a new version of the confederate" 
            text[2]= "states. In the late 21st century, seven states split off of the US because the rest of the"
            text[3]= "country was killing itself with corruption and insanity." 
            text[4]= "There would have been a second civil war, but the United States was too weak to put"
            text[5]= "up any kind of resistance to the secession and decided to leave it be."
            text[6]= "With the economic powerhouse states gone, the United States has all but collapsed and has"
            text[7]= "reverted to \"Wild west-isim.\""
            text[8]= ""
            text[9]= "With the dead weight gone, the A°R°T has successfully become the world's centre for reaserch"
            text[10]="and academia. Scientists travel from around the world to participate in the groundbreaking"
            text[11]="studies at the nation's pride and joy: The University Of Houston. "
            text[12]=""
            text[13]="The Texan Republic is on good terms with South Africa and Russia, but sometimes worries the"
            text[14]="people of those two nations with its seming disregard for safety in the practice of science."
            text[15]=""
            text[16]="As a Texan reasercher, you will begin the game with a gun, and some fancy hors d'oeuvres"
            text[17]=""
            text[18]="And yes, they deported the californians."
            country = "Texas"
            hasreadtexaslore = True

        #Make the pick button and blit
        if hasreadrussialore and hasreadzalore and hasreadtexaslore:
            buttonfont = pygame.font.Font("TNR.ttf", 32)
            buttontext = buttonfont.render("Pick %s"%country, True, (255, 255, 255))
            pick_button = Button(700, 600, buttontext)

            if pick_button.draw():
                clearlines(0, 0)
                scene = "Opening Animation %s"%country
                screen.fill((0,0,0))
                pygame.display.update()
        elif hasreadrussialore or hasreadzalore or hasreadtexaslore:
            buttonfont = pygame.font.Font("TNR.ttf", 32)
            buttontext = buttonfont.render("Read all lore before proceding", True, (255, 255, 255))
            pick_button = Button(600, 600, buttontext)
            pick_button.draw()
    

    
    ###########################################################################################
    
    #Charaprint for each country

    if scene == "Opening Animation South Africa":        
        chara_print_begin("You are from one of these nations:", 0, insta=True)
        chara_print_begin("South Africa.", 1)
        chara_print_begin(" ", 2)
        chara_print_begin("This is good, because your country greatly needs", 3)
        chara_print_begin("your specific skill set for an important mission.", 4, 1)
        if charatextline[4] != "":
            scene = "Line Before Field Select"
            clearlines(0,4)
        


    if scene == "Opening Animation Russia":
        chara_print_begin("You are from one of these nations:", 0, insta=True)
        chara_print_begin(country+".", 1)
        chara_print_begin(" ", 2)
        chara_print_begin("This is good, because your country greatly needs", 3)
        chara_print_begin("your specific skill set for an important mission.", 4, 1)
        if charatextline[4] != "":
            scene = "Line Before Field Select"
            clearlines(0,4)

    if scene == "Opening Animation Texas":
        chara_print_begin("You are from one of these nations:", 0, insta=True)
        chara_print_begin(country+".", 1)
        chara_print_begin(" ", 2)
        chara_print_begin("You are in the perfect place to", 3)
        chara_print_begin("conduct your reaserch.", 4, 1)

        if charatextline[4] != "":
            scene = "Line Before Field Select"
            clearlines(0,4)
        

    if scene == "Line Before Field Select":
        chara_print_begin("Choose your field now:", 0, wait=2)
        if charatextline[0] != "":
            clearlines(0,0)
            scene = "Field Picker"
            text = [""]*19
            text[0] = "Click on a field to learn more about it, than select it by clicking \"pick\""

    #########################################################################################################

    #Field Picker
    if scene == "Field Picker":

        try:
            computer_science_button
        except:
            #Buttons    
            computer_science_button = Button(100, 690, pygame.image.load("IMAGES/computer science icon.png"))

            robotics_button = Button(312, 690, pygame.image.load("IMAGES/robotics icon.png"))

            physics_button = Button(537, 690, pygame.image.load("IMAGES/physics icon.png"))

            virology_button = Button(750, 690, pygame.image.load("IMAGES/virology icon.png"))

            #Empty Field (lol)
            field = ""

        #Get Mouse Pos
        PICKER_MOUSE_POS = pygame.mouse.get_pos()

        #Blit Field Discriptions
        for i in range(19):
            screen.blit(pygame.font.Font("TNR.ttf", 18).render(text[i],  True, (255, 255, 255)), (90, (100+18*i)))


        #Make a box for the buttons
        pygame.draw.rect(screen, (255,255,255), (40, 625, 775, 125), 2)

        if robotics_button.draw():
            field = "Robotics"
            lcfield = "robotics"

            text[0]= "As a doctor of robotics, your work mainly consists of creating autonomous machines."
            text[1]= "Your most recent project has been on an androidal and AI powered bodyguard."
            text[2]= "Begin the game with some high technology, including armour."
            text[3]= ""

            #if country == "Russia" or country == "South Africa":
                #text[4] = "The reaserchers from the Texan Republic have been working on a similar project,"
                #text[5] = "but the artificial intelegence that is going to power it was developed with no attention"
                #text[6] = "whatsoever payed to safety. In fact, Texas is the only country in the world with AI"
                #text[7] = "regulations lax enough to allow it. "
            #else:
                #text[4]=""
                #text[5]=""
                #text[6]=""
                #text[7]=""

        if computer_science_button.draw():
            field = "Computer Science"
            lcfield = "computer science"
            if country == "Russia":
                aiassistant = "Artyom"
            if country == "South Africa":
                aiassistant = "Chesney"
            if country == "Texas":
                aiassistant = "Charles"
            
            text[0]="As a doctor of computer science, your work has been almost entirely on artificial inteligence."
            text[1]="Begin the game with computer spikes and an AI assistant named %s."%aiassistant
            text[2]=""
            text[3]=""
            text[4]=""
            text[5]=""
            text[6]=""
            text[7]=""
            text[8]=""




        if physics_button.draw():
            field = "Physics"
            lcfield = "physics"

            text[0]="As a doctor of physics, your work has mostly been on the new theory of quantum reletivity."
            text[1]="The most starteling discovery you have made so far has been a hyper-efficent way of"
            text[2]="storing energy made possible by pretorium's heavy nucleus."
            text[3]=""
            text[4]=""
            text[5]=""
            text[6]=""
            text[7]=""
            text[8]=""



        if virology_button.draw():
            field = "Virology"
            lcfield = "virology"

            text[0]="As a doctor of virology, your work has been on Gain-of-Function studies in viruses"
            text[1]="and on improvements of CRISPR gene editing. Specificly the aplications of these in"
            text[2]="combating bio-terrorisim."
            text[3]="Start the game with some interesting specimens and concoctions."
            text[4]=""
            text[5]=""
            text[6]=""
            text[7]=""
            text[8]=""


        #Make the pickerbutton and blit
        if field != "":
            buttonfont = pygame.font.Font("TNR.ttf", 32)
            buttontext = buttonfont.render("Pick %s"%field, True, (255, 255, 255))
            pick_button = Button(680, 600, buttontext)

            if pick_button.draw():
                scene = "Briefingintro"
                screen.fill((0,0,0))
                if country=="South Africa":
                    breifingintroaddedtext0 = "General van Dyke will brief you momentarily."
                    breifingintroaddedtext1 = "You remember him, dont you?"
                if country=="Russia":
                    breifingintroaddedtext0 = "General Smyrnov will brief you momentarily."
                    breifingintroaddedtext1 = "You remember him, dont you?"
                    
    #########################################################################################################

    if scene=="Briefingintro":
        chara_print_begin("Good luck...", 0, 1.2)

        if country=="Texas":
            chara_print_begin("Your reaserch project begins tomorrow...", 1)
            if charatextline[1] !="":
                clearlines(0,4)
                scene="Wake up (Texas)"
                pygame.display.set_mode((850, 800))

        if country=="Russia":
            chara_print_begin("General Smyrnov will brief you momentarily.", 1)
            chara_print_begin("You remember him, dont you?", 2, wait=1.2)
            chara_print_begin("His last name means quiet...", 3, 1.2)
            chara_print_begin("Heh heh heh...", 4, 2)
            if charatextline[4] != "":
                clearlines(0,4)
                scene="Wake up (Russia)"
                pygame.display.set_mode((850, 800))
                

        if country=="South Africa":
            chara_print_begin("General van Dyke will brief you momentarily.", 1)
            chara_print_begin("You remember him, dont you?", 2, wait=1.2)
            chara_print_begin("You fought together...", 3, 3)
            if charatextline[3] !="":
                pygame.mixer.music.set_volume(0)
                clearlines(0,4)
                screen.fill((0,0,0))
                scene = "ZA War Dream"
                
    #########################################################################################################
        

    if scene == "ZA War Dream":
        try:
            hasplayedcutscene
        except:
            hasplayedcutscene = False


        if not hasplayedcutscene:

            screen.fill((0,0,0))
            pygame.display.update()

            pygame.time.wait(800)

            boom = mixer.Sound("SOUNDS/boom.mp3")
            boom.play()

            pygame.time.wait(int((0.2*1000)))

            

            if country == "South Africa" or country=="Russia":
                goal = "Mission"
            else:
                goal = "Project"

            clearlines(0,8)

            pygame.display.set_caption("Chapter 1 - The %s"%goal)
            video = VideoFileClip('VIDS/Cutsceneza.mp4')            
            video.preview(fps=20)
            video.close()

            hasplayedcutscene = True

            scene = "Wake up (ZA)"

            pygame.display.set_mode((850, 800))
            pygame.mixer.music.load("SOUNDS/wind.mp3")
            pygame.mixer.music.play(-1)
            
            
        

    #########################################################################################################

    if scene=="Wake up (ZA)":
        
        if subscene==-1:
            if pygame.key.get_pressed()[pygame.K_l]:
                Wakeup_Za1 = Photo("IMAGES/ZA_House.jpeg")
                subscene = "Clicks"



            chara_print_begin("You wake up in a cold sweat.", 0, 1, 200, 300, do_ding=False)
            chara_print_begin("Another nightmare.", 1, 1, 200, 300, do_ding=False)
            chara_print_begin("Your eyes are squeezed shut.", 2, 1, 200, 300, do_ding=False)
            if charatextline[2]!="":
                clearlines(0,2)
                subscene= 0
                pygame.mixer.music.pause()

        if subscene==0:
            screen.fill((0,0,0))
            overworld_rectangle()
            overworld_print("Wake up! Chief!", 0, soundus="SOUNDS/MakhatiniHit.mp3")
            overworld_keep(0)
            screen.blit((pygame.font.Font("TNR.ttf", 20).render("Press the W key or green button to continue in diologue",True,(255,255,255))), (270, 750))

            if advancing(0):
                subscene = 1
                clearlines(0,0)
                morning_song = pygame.mixer.music.load("SOUNDS/MorningMood.mp3")
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play(-1)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()

        if subscene==1:
            Wakeup_Za1 = Photo("IMAGES/ZA_HOUSE.jpeg")
            Wakeup_Za1.show()
            overworld_rectangle()
            overworld_print("You're Going to be late for the general!!!", 0, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            overworld_keep(0, iconades="FACES/Makhatini_Smile.png")

            if advancing(0):
                subscene = 2
                clearlines(0,0)
            if event.type == pygame.QUIT:
                pygame.quit()

            

        if subscene==2:
            buttonfont = pygame.font.Font("TNR.ttf", 32)
            button1text = buttonfont.render("AAAAAAAH!", True, (255,255,255))
            button2text = buttonfont.render("Who are you?", True, (255,255,255))
            screen.blit((pygame.font.Font("TNR.ttf", 20).render("Use your mouse to select a diologue option",True,(255,255,255))), (400, 750))
            button1 = Button(283, 700, button1text)
            button2 = Button(566, 700, button2text) 
            displaymouse()

            Wakeup_Za1.show()
            overworld_rectangle()            
    

            if button1.draw():
                subscene = 3
                clearlines(0,0)

            if button2.draw():
                subscene=4
                clearlines(0,0)

        if subscene == 3:
            Wakeup_Za1.show()
            overworld_rectangle()  
            overworld_print("Have you been dreaming about the war again?", 0, 1.2, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Serious.png")
            overworld_print("Dont worry, man, your best friend Makhatini is here!", 1, 0.8, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smirk.png")
            overworld_print("I see you...",2, waitus=2, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Serious.png")
            overworld_print("NOW GET UP YOU SLEPT IN! GO GO GO.",3, waitus=0, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Yell.png", loud = True, volumeboost=0.8)
            overworld_keep(3, "FACES/Makhatini_Yell.png")

            if advancing(3):
                clearlines(0,3)
                subscene ="Begin click tutorial"

            for event in pygame.event.get():                                                
                if event.type == pygame.QUIT:
                    pygame.quit()

        if subscene == 4:
            Wakeup_Za1.show()
            overworld_rectangle()  
            overworld_print("Dont you know your own best friend Makhatini?", 0, 0.3, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smirk.png")
            overworld_print("You have been dreaming about the war again, ne?", 1, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Serious.png")
            overworld_print("I see you...",2, waitus=3, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Serious.png")
            overworld_print("NOW GET UP YOU SLEPT IN! GO GO GO.",3, waitus=0, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Yell.png", loud=True, volumeboost=0.8)
            overworld_keep(3, "FACES/Makhatini_Yell.png")

            if advancing(3):
                clearlines(0,3)
                subscene ="Begin click tutorial"
            
            for event in pygame.event.get():                                            
                if event.type == pygame.QUIT:
                    pygame.quit()
                

        if subscene=="Begin click tutorial":
            Wakeup_Za1.show()
            overworld_rectangle() 
            overworld_print("Click on an object in a room to inspect it.", 0, waitus=1, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            overworld_print("Drink your oringe juce and come downstairs.", 1, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            overworld_print("By the way, I made some furniture adjustments since this is", 2, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smirk.png")
            overworld_print("my house untill you get back...", 3, 1, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smirk.png")
            overworld_keep(3, "FACES/Makhatini_Smirk.png")

            for event in pygame.event.get():
                            
                if event.type == pygame.QUIT:
                    pygame.quit()

            if advancing(3):                
                clearlines(0,3)
                subscene ="Clicks"
                
                

        if subscene=="Clicks":

            Wakeup_Za1.show()
            overworld_rectangle() 

            try:
                Window
            except:
                Window = Clickable((4,103), (846, 391))
            if Window.clicked() and Focus_Object==None:
                Focus_Object = "Window"

            if Focus_Object=="Window":
                overworld_print("You feel so blessed to be able to live with a view like that.", 0)
                overworld_print("You will miss it while you are gone.", 1)
                overworld_keep(1)

                if advancing(1):
                    clearlines(0, 1)
                    Focus_Object=None
                
            
            if hint():
                Window.dev_show_hitbox()
                Oringe_Juice.dev_show_hitbox()
                Chair1.dev_show_hitbox()
                Chair2.dev_show_hitbox()
                rug.dev_show_hitbox()
                roof.dev_show_hitbox()


            try:
                Oringe_Juice
            except:
                Oringe_Juice = Clickable((110, 417), (212,466))
            if Oringe_Juice.clicked() and Focus_Object==None:
                Focus_Object = "Oringe Juice"
            
            if Focus_Object=="Oringe Juice":
                screen.blit((pygame.font.Font("TNR.ttf", 20).render("Use your mouse to select an action",True,(255,255,255))), (466, 750))
                displaymouse()
                button1 = Button(283, 700, pygame.font.Font("TNR.ttf", 32).render("Keep looking", True, (255,255,255)))
                button2 = Button(566, 700, pygame.font.Font("TNR.ttf", 32).render("Drink and go down", True, (255,255,255))) 

                if button1.draw():
                    Focus_Object=None

                if button2.draw():
                    Focus_Object = None
                    scene = "Downstairs (ZA)"
                    subscene = -1

                

            

            try:
                Chair1
            except:
                Chair1 = Clickable((600,390),(719,512))
            if Chair1.clicked() and Focus_Object==None:
                Focus_Object = "Chair 1"

            if Focus_Object=="Chair 1":

                try:
                    sitting1
                except:
                    sitting1 = False

                if not sitting1:
                    overworld_print("Its a cozy chair. Would you like to sit in it one last time?", 0)
                    overworld_keep(0)

                if charatextline[0] == "Its a cozy chair. Would you like to sit in it one last time?":
                    button1 = Button(283, 700, pygame.font.Font("TNR.ttf", 32).render("Yes", True, (255,255,255)))
                    button2 = Button(566, 700, pygame.font.Font("TNR.ttf", 32).render("No", True, (255,255,255))) 
                    displaymouse()

                    if button1.draw():
                        if charatextline[0] != "":
                            sitting1=True
                            clearlines(0, 0)

                    if button2.draw():
                        Focus_Object = None
                        clearlines(0, 0)

                elif sitting1:
                    overworld_print("Ahhh... Cozy...", 0)
                    overworld_keep(0)
                    if advancing(0):
                        clearlines(0,0)
                        Focus_Object=None
                        
                        


            



            try:
                Chair2
            except:
                Chair2 = Clickable((719,445),(850,600))
            if Chair2.clicked() and Focus_Object==None:
                Focus_Object = "Chair 2"

                
            if Focus_Object=="Chair 2":

                try:
                    takecash
                except:
                    takecash = False

                try:
                    hastakencash
                except:
                    hastakencash = False

                if not takecash:
                    overworld_print("Its a cozy chair. You keep some spare cash under it.", 0)
                    overworld_print("Would you like to take some with you?", 1)
                    overworld_keep(1)

                    if charatextline[1] == "Would you like to take some with you?":
                        button1 = Button(283, 700, pygame.font.Font("TNR.ttf", 32).render("Yes", True, (255,255,255)))
                        button2 = Button(566, 700, pygame.font.Font("TNR.ttf", 32).render("No", True, (255,255,255)))
                        displaymouse() 

                        if button1.draw():
                            if charatextline[0] != "":
                                takecash=True
                                clearlines(0, 1)

                        if button2.draw():
                            Focus_Object = None
                            clearlines(0, 1)

                elif hastakencash:
                    overworld_print("You have already taken the cash.", 0)
                    overworld_keep(0)
                    if advancing(0):
                        clearlines(0,0)
                        Focus_Object=None


                elif takecash:
                    overworld_print("You take the cash:", 0)
                    overworld_print("+ 20 Rand", 1)
                    overworld_keep(1)
                    if advancing(1):
                        clearlines(0,1)
                        Focus_Object=None
                        hastakencash=True
                        inv.money = inv.money + 20


            try:
                rug
            except:
                rug = Clickable((403,512),(718,599))
            if rug.clicked() and Focus_Object==None:
                Focus_Object = "Rug"

            if Focus_Object=="Rug":
                overworld_print("Its a rug...", 0, waitus= 1)
                overworld_print("A very manly rug...", 1)
                overworld_keep(1)
                if advancing(1):
                    clearlines(0,1)
                    Focus_Object=None

            try:
                bed1
                bed2
                bed3
            except:
                bed1=Clickable((213,415),(400,600))
                bed2=Clickable((2,476),(212,600))
                bed3=Clickable((6,398),(104,464))

            if (bed1.clicked() or bed2.clicked() or bed3.clicked()) and Focus_Object==None:
                Focus_Object="Bed"

            if Focus_Object=="Bed":
                overworld_print("You just got up from your bed.",0)
                overworld_print("Drink the oringe juice that is on it to go downstairs", 1)
                overworld_keep(1)
                if advancing(1):
                    clearlines(0,1)
                    Focus_Object=None

            try:
                whatchamakallitart
            except:
                whatchamakallitart = Clickable((788, 397), (825, 441))

            if whatchamakallitart.clicked() and Focus_Object==None:
                Focus_Object = "whatchamakallitart"
                
            if Focus_Object=="whatchamakallitart":
                overworld_print("It's an animal figurine...",0)
                overworld_print("Probably...",1)
                overworld_keep(1)

                if advancing(1):
                    clearlines(0,1)
                    Focus_Object = None

            try:
                roof
            except:
                roof=Clickable((0,0), (848, 63))
            if roof.clicked() and cooldownmisc==0:
                Focus_Object="Roof"


            if Focus_Object=="Roof":
                overworld_print("Its the roof...", 0)
                overworld_keep(0)
                if advancing(0):
                    clearlines(0,0)
                    Focus_Object=None
        inv.avalable()





    if scene=="Downstairs (ZA)":

        try:
            DownstairsZa
        except:
            DownstairsZa = Photo("IMAGES/DownstairsZa.jpeg")
            pygame.mixer.music.load("SOUNDS/Wrong_Cat.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.3)


        DownstairsZa.show()
        overworld_rectangle()

        if subscene==-1:
            overworld_print("Didn't you set your alarm clock???", 0, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            overworld_keep(0, iconades="FACES/Makhatini_Smile.png")
            if advancing(0):
                subscene=0
                clearlines(0,0)

        if subscene==0:
            
            button1 = Button(300, 650, pygame.font.Font("TNR.ttf", 20).render("Ja, I did, but I din't go off!!! Horrible time for it to break, ne?", True, (255,255,255)))
            button2 = Button(364, 740, pygame.font.Font("TNR.ttf", 20).render("I could have sworn I set it for 6 am, but this morning, it said I set it for 7:14!", True, (255,255,255)))
            displaymouse()
            if button1.draw() or button2.draw():
                
                subscene=1
                clearlines(0, 1)

        if subscene==1:
            overworld_print("That is quite strange...", 0, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smirk.png")
            overworld_print("Well, if you eat your breakfast on the go, maybe we can save some time!", 1, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            overworld_print("Grab the food I made for you, and then look at it in your invintory!", 2, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            overworld_keep(2, "FACES/Makhatini_Smile.png")
            if advancing(2):
                subscene="Clicks"
                clearlines(0,2)

        if subscene=="Clicks":

            try:
                if hint():
                    Food.dev_show_hitbox()
                    weapon.dev_show_hitbox()
                    window1.dev_show_hitbox()
                    window2.dev_show_hitbox()
                    chair1.dev_show_hitbox()
                    chair2.dev_show_hitbox()
                    plant.dev_show_hitbox()
                    door.dev_show_hitbox()
            except:
                pass


            try: 
                Food
            except:
                Food = Clickable((327, 389), (471, 435))
            if Food.clicked():
                Focus_Object="Food"
                clearlines(0, 3)
                try:
                    hasgrabbedfood
                except:
                    hasgrabbedfood = False
            if Focus_Object=="Food":
                if not hasgrabbedfood:


                    overworld_print("You grab your kos:",0)
                    overworld_print("+2 Biltong, +1 Baboti, +2 Vetkoek",1)
                    overworld_keep(1)
                    if advancing(1):
                        clearlines(0,1)
                        Focus_Object="Leaveplz"
                        inv.items.extend([biltong, biltong, baboti, vetkoek, vetkoek])
                        hasgrabbedfood = True
                elif hasgrabbedfood:
                    overworld_print("You already grabbed your kos:",0)
                    overworld_keep(0)
                    if advancing(0):
                        clearlines(0,1)
                        Focus_Object=None


            if Focus_Object=="Leaveplz":
                overworld_print("Click on the door when you are ready to leave.", 0, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
                overworld_print("Dont forget your baton!!!", 1, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
                overworld_keep(1, "FACES/Makhatini_Smile.png")
                if advancing(0):
                    clearlines(0,1)
                    Focus_Object=None
            
            window1 = Clickable((477,236),(696,362))
            window2 = Clickable((40,213), (428,347))
            chair1 = Clickable((128,464),(341,594))
            chair2 = Clickable((357,500),(584,600))
            plant = Clickable((0,110),(124,512))
            weapon = Clickable((725,400),(781,532))
            door = Clickable((789,215),(848,530))

            if window1.clicked():
                Focus_Object="window"

            if window2.clicked():
                Focus_Object="window"

            if chair1.clicked():
                Focus_Object="chair"

            if chair2.clicked():
                Focus_Object="chair"

            if plant.clicked():
                Focus_Object="plant"

            if weapon.clicked():
                Focus_Object="weapon"

            if door.clicked():
                Focus_Object="door"

            if Focus_Object=="window":
                overworld_print("It's a window. More of that wonderfull jungle outside...", 0)
                overworld_keep(0)
                if advancing(0):
                    Focus_Object=None
                    clearlines(0,0)


            
            if Focus_Object=="chair":
                overworld_print("It's a chair...", 0)
                overworld_keep(0)
                if advancing(0):
                    Focus_Object=None
                    clearlines(0,0)

            if Focus_Object=="plant":
                overworld_print("It's a rare species of elephant ear. ", 0)
                overworld_keep(0)
                if advancing(0):
                    Focus_Object=None
                    clearlines(0,0)

            if Focus_Object=="weapon":
                try:
                    hasgrabbedweapon
                except:
                    hasgrabbedweapon=False

                if not hasgrabbedweapon:
                    overworld_print("It is a shock baton.", 0)
                    overworld_print("Makhatini will tell you about it in the car...", 1)
                    overworld_print("+1 Shock Baton", 2)
                    overworld_keep(2)
                    if advancing(2):
                        Focus_Object=None
                        clearlines(0,2)
                        inv.items.append(shock)
                        hasgrabbedweapon=True
                else:
                    overworld_print("You already grabbed the baton...", 0)        
                    overworld_keep(0)
                    if advancing(0):
                        Focus_Object=None
                        clearlines(0,0)   

            if Focus_Object=="door":
                try:
                    hasgrabbedweapon
                except:
                    hasgrabbedweapon=False

                try:
                    hasgrabbedfood
                except:
                    hasgrabbedfood=False

                if hasgrabbedfood and hasgrabbedweapon:
                    Focus_Object=None
                    subscene=-1
                    scene="Car (ZA)"

                else:
                    overworld_print("You are forgetting something...", 0, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smirk.png")
                    overworld_keep(0, "FACES/Makhatini_Smirk.png")
                    if advancing(0):
                        Focus_Object=None
                        clearlines(0,0)
                    
            

        inv.avalable()

        
    if scene == "Car (ZA)":
        carpic = Photo("IMAGES/Zakar.jpeg")
        carpic.show()
        overworld_rectangle()

        if subscene == -1:
            overworld_print("What are you going to do without me when you go to America? Honestly, man...", 0, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            overworld_print("I need to pick you up and drop you at the base, I need to wake you up in the morning...", 1, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png", waitus=0.45)
            overworld_print("OH NO! I FORGOT YOUR SIPPY CUP!!!", 2, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Yell.png", loud=True, volumeboost=0.4)
            overworld_keep(2, "FACES/Makhatini_Yell.png")
            if advancing(2):
                clearlines(0,2)
                subscene = 0

        if subscene==0:
            button1 = Button(130, 650, pygame.font.Font("TNR.ttf", 20).render("Shut up, Mackhatini.", True, (255,255,255)))
            button2 = Button(380, 740, pygame.font.Font("TNR.ttf", 20).render("[distraction] So, do you want to tell me some more about your work on weapons?", True, (255,255,255)))

            if button1.draw():
                subscene = 1

            if button2.draw():
                subscene = 3

        if subscene==1:
            try:
                alpha
            except:
                alpha=0
            mak = pygame.mixer.Sound("SOUNDS/MakhatiniHit.mp3")
            mak.play()
            overworld_print("*Laughs*                                                                                                            ", 0, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            pygame.time.wait(50)
            alpha=alpha+1
            if alpha>21:
                subscene=2
                clearlines(0,0)
                pygame.time.wait(1000)
                overworld_rectangle()
                pygame.display.update()
                pygame.time.wait(1000)

        if subscene==2:
            overworld_print("So, do you want to hear about some of my work on weapons?", 0, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            overworld_print("Of course you do!", 1, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            if charatextline[1]!="":
                pygame.time.wait(700)
                subscene=4
                clearlines(0,1)

        if subscene==3:
            overworld_print("Natuurlik!", 0, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            if charatextline[0]!="":
                pygame.time.wait(700)
                subscene=4
                clearlines(0,1)

        if subscene==4:
            overworld_print("I worked on that shock baton of yours, you know...", 0, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            overworld_print("Regular firearms can't pierce the pretorium alloy armour that the Russians invented,", 1, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            overworld_print("and the new piercing bullets are WAY too expensive, so we came up with that", 2, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            overworld_print("genius device. Pretorium batteries can store enough energy to be lethal a hundred times", 3, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            overworld_print("over. Of course, explosives would probably still be the favoured weapon in a battlefield. ", 4, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            overworld_print("Another plus side of shock batons is that they work great against robotc enemies.", 5, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png")
            overworld_keep(5,"FACES/Makhatini_Smile.png")
            if advancing(5):
                clearlines(0,5)
                subscene=5

        if subscene==5:
            overworld_print("I think the general is going to have some bulletproof clothes in the equiptment he is sending with.", 0, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Serious.png", waitus=0.3)
            overworld_print("I dont like all the secrecy behind this mission, you know. I can't believe you accepted it without", 1, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Serious.png", waitus=0.3)
            overworld_print("even knowing what it was all about.", 2, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Serious.png", waitus=0.6)
            overworld_print("In all my years in the Bureau of State Security, I've never heard of an assignment that violated", 3, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Serious.png", waitus=0.6)
            overworld_print("protocol like this.", 3, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Serious.png", waitus=0.6)
            overworld_print("You know that you are the only doctor of %s that fought in the war, right?" %lcfield, 4, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Serious.png", waitus=0.6)
            overworld_print("That probably has a lot to do with why he picked you...", 5, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Serious.png", waitus=0)
            overworld_keep(5,"FACES/Makhatini_Serious.png")
            if advancing(5):
                clearlines(0,5)
                subscene=6

        

        #if subscene==6:
            #overworld_print("Well, we are almost there, let us see what all this suspense has been about...", 0, soundus="SOUNDS/MakhatiniHit.mp3", icon="FACES/Makhatini_Smile.png", waitus=0)
            #if charatextline[0]!="":
                #pygame.time.wait(1000)
                #clearlines(0,0)
                #subscene=-1

                #scene="Briefing"
                #from moviepy.editor import *
                #pygame.display.set_caption("Chapter 1 - The Mission")
                #video = VideoFileClip('VIDS/BASEZA.mp4')            
                #video.preview(fps=20)
                #video.close()
                #pygame.display.set_mode((850, 800))

    if scene=="Briefing":
        try:
            Base
        except:
            Base = Photo("IMAGES/AfricaBase.jpeg")

        overworld_rectangle()

        Base.show()


    pygame.display.update()  

    clock.tick(60)


