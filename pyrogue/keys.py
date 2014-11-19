import pyrogue.libtcodpy as libtcod

def handleKeys(player):
    """
    Handles key presses from the user; including movement, exiting,
    and toggle fullscreen. It takes the player so that it can update
    the player's state.
    """
    # Our game is turnbased so we wait for a keypress every turn
    # before executing more code.
    key = libtcod.console_wait_for_keypress(True)

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # M-Return (Alt+Enter) toggles fullscreen
        libtcod.console_set_fullscreen(not
                                       libtcod.console_is_fullscreen())
        return False
    elif key.vk == libtcod.KEY_ESCAPE:
        return True # which we handle by exiting the game loop
    # Useful alias for a long fn name
    keyPressed = libtcod.console_is_key_pressed
    if keyPressed(libtcod.KEY_UP):
        player.move(0, -1)
        return False
    elif keyPressed(libtcod.KEY_DOWN):
        player.move(0, 1)
        return False
    elif keyPressed(libtcod.KEY_LEFT):
        player.move(-1, 0)
        return False
    elif keyPressed(libtcod.KEY_RIGHT):
        player.move(1, 0)
        return False
