print("Demarrage 'CLAVIER.py'")
def CLAVIER_get():
    stdscr=curses.initscr()
    stdscr.nodelay(True)
    curses.cbreak()
    curses.flushinp()
    _touche=-1
    while (_touche==-1):
        _touche=int(str(stdscr.getch()))
    curses.flushinp()
    curses.endwin()
    return _touche

#modification du 17/05/2022 par C'tautomatiyx: En cas de changement d'état de présence de carte, les fonctions ne renvoie plus 0 mais None et ceux pour pouvoir utiliser la touche "calculator de certain clavier"
def CLAVIER_getRFID():
    if config.debugging:
        print("CLAVIER_getRFID")
    stdscr = curses.initscr()
    stdscr.nodelay(True)
    curses.cbreak()
    curses.flushinp()
    _touche=-1
    while (_touche==-1):
        if not(RFID_carteCheck()):
            _touche=None
        else:
            _touche=int(str(stdscr.getch()))
    curses.flushinp()
    curses.endwin()
    return _touche
def CLAVIER_getNotRFID():
    if config.debugging:
        print("CLAVIER_getNotRFID")
    stdscr = curses.initscr()
    stdscr.nodelay(True)
    curses.cbreak()
    curses.flushinp()
    _touche=-1
    while (_touche==-1):
        if (RFID_carteCheck()):
            _touche=None
        else:
            _touche=int(str(stdscr.getch()))
    curses.flushinp()
    curses.endwin()
    return _touche
def CLAVIER_confirmation():
    return CLAVIER_get()==10
