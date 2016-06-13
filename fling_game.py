import os
import pygame
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
WIDTH=20
HEIGHT=20
MARGIN=5
grid=[]
for row in range(8):
    grid.append([])
    for column in range(7):
        grid[row].append(0)

# set row 1 ,cell 5 to one (remember row and columns starts at zero)
grid[1][5]=1
grid[6][5]=1
grid[5][2]=1

# intialize pygame
pygame.init()
#set heaight and width of the screen
WINDOW_SIZE=[100,205]
screen=pygame.display.set_mode(WINDOW_SIZE)
# set title of Screen
pygame.display.set_caption('Array Back Grid')
# loop until the user click the close button
done=False
# used to manage how fast the screen updates
#clock=pygame.time.clock()
# main program LOOP
while not done:
    for event in pygame.event.get():     # user did something
        if event.type==pygame.QUIT:      #if user clicked done
           done=True                       # Flag that we are done so we exits this loop

        elif event.type==pygame.MOUSEBUTTONDOWN:     #user click the mouse  to get the position
           pos=pygame.mouse.get_pos()
#         change the X/y screen coordinates to grid coordinates
           column=pos[0]//(WIDTH + MARGIN)
           row=pos[1]//(HEIGHT + MARGIN)
#         set that location  to one

           grid[row][column]=1
           print ("Click",pos,"Grid-Co-ordinates:",row ,column)

           if grid[row][column+1] == 1:
               grid[row][column+1]=0
               grid[row][column]=1

           if grid[row][column-1]==1:
               grid[row][column-1]=0
               grid[row][column]=1


           if grid[row+1][column]==1:
               grid[row+1][column]=0
               grid[row][column]=1

           if grid[row-1][column]==1:
                   grid[row-1][column]=0
                   grid[row][column]=1


#                    set the screen background

    screen.fill(BLACK)
#     Draw the grid
    for row in range(8):
        for column in range(7):
            color=WHITE
            if grid[row][column]==1:

                color=GREEN
            pygame.draw.rect(screen,
                             color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                             (MARGIN + HEIGHT) * row + MARGIN,
                             WIDTH,
                             HEIGHT
                              ])
#                 limit to 60 frame per second


       # clock.tick(60)

#         GO ahead and update the screen with what we have drawn.

        pygame.display.flip()

# be idle friendly .if you forget this time  , the program will hang

# on exit

pygame.quit()
















































