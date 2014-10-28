import libtcodpy as libtcod

from entity import Entity

#actual size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
 
def handle_keys():
    global playerx, playery
        
    key = libtcod.console_wait_for_keypress(True)  #turn-based
    
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
            
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game
    
    #movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        player.move(0, -1)

    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        player.move(0, 1)
            
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        player.move(-1, 0)
            
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        player.move(1, 0)
            
 
#############################################
# Initialization & Main Loop
#############################################
 
libtcod.console_set_custom_font(b'arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, b'python/libtcod tutorial', False)

# Define an off-screen console called con, just in case we want to mess
# with transparency, etc.
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

player = Entity(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, b'@', libtcod.white, con)
npc = Entity(SCREEN_WIDTH//2 + 3, SCREEN_HEIGHT//2, b'@', libtcod.yellow, con)

entities = [player, npc]

while not libtcod.console_is_window_closed():
        
    for entity in entities:
        entity.draw()
    
    # Since we are drawing to an off-screen console, we need to "blit"
    # it to the actual console - this just means we copy it over
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    # This flushes the changes in the console to the screen itself
    libtcod.console_flush()
    
    for entity in entities:
        entity.clear()
    
    #handle keys and exit game if needed
    exit = handle_keys()
    if exit:
        break
