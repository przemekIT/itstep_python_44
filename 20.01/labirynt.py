def znajdz_droge(labirynt, x, y, droga):
    if x < 0 or y < 0 or x >= len(labirynt) or y >= len(labirynt[0]) or labirynt[x][y] == 1:
        return False
    if (x,y) == (len(labirynt) - 1, len(labirynt[0]) - 1): # Warunek brzegowy (koniec)
        droga.append((x,y))
        return True
    
    labirynt[x][y] = 1 # Oznacz pole jako odwiedzone
    droga.append((x,y))

    # Przeszukaj wszystkie kierunki
    if (znajdz_droge(labirynt, x+1, y, droga) or
        znajdz_droge(labirynt, x, y+1, droga) or
        znajdz_droge(labirynt, x-1, y, droga) or 
        znajdz_droge(labirynt, x, y-1, droga)):
        return True
    
    droga.pop() # Usuń ślepą uliczkę
    labirynt[x][y] = 0 # Cofnąć oznaczenie
    return False


labirynt = [
    [0,0,1,0],
    [1,0,1,0],
    [0,0,0,0],
    [1,1,0,1]
]

droga = []
znajdz_droge(labirynt, 0, 0, droga)
print(droga)

