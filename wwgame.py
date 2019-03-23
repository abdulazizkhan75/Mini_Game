import sys, pygame, random
from ww import *
pygame.init()

ww=Stage(20, 20, 24)
ww.set_player(KeyboardPlayer("icons/face-cool-24.png", ww))
ww.add_actor(Monster("icons/face-devil-grin-24.png", ww, 7, 4, 5))
ww.add_actor(Monster("icons/face-devil-grin-24.png", ww, 4, 10, 3))
ww.add_actor(Monster("icons/face-devil-grin-24.png", ww, 5, 20, 2))
ww.add_actor(sticky("icons/edit-delete-8.png",ww,1,1))
ww.add_actor(sticky("icons/edit-delete-8.png",ww,10,10,))
ww.add_actor(sticky("icons/edit-delete-8.png",ww,8,15,))
ww.add_actor(sticky("icons/edit-delete-8.png",ww,9,1,))

# The Loop is constructing a random width and height as x and y coordinates
# following that the loop then sets the boxes at these random x and y
# coordinates and adds 1 to counter and then continues to unitl there are 99
# boxes.

num_boxes=0
while num_boxes<100:
    x=random.randrange(ww.get_width())
    y=random.randrange(ww.get_height())
    if ww.get_actor(x,y) is None:
        ww.add_actor(Box("icons/emblem-package-2-24.png", ww, x, y))
        ww.add_actor(Wall("icons/wall.jpg", ww, 3, 4))
        ww.add_actor(Wall("icons/wall.jpg", ww, 3, 5))
        ww.add_actor(Wall("icons/wall.jpg", ww, 3, 6))
        ww.add_actor(Wall("icons/wall.jpg", ww, 9, 9))
        ww.add_actor(Wall("icons/wall.jpg", ww, 9, 8))
        ww.add_actor(Wall("icons/wall.jpg", ww, 12, 12))
        num_boxes+=1

# The Loop is checking the what buttons the user is clicking. If the player
# clicks the quit then this loop goes through to the quit part and exits
# closing the window. Else if the user presses a key button then the player
# moves in that direction. As well it refreshes the pygame everytime a move is
# made by the Actors.

while True:
    pygame.time.wait(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            ww.player_event(event.key)
    ww.step()
    ww.draw()







            
