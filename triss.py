# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:16:31 2023

@author: UTENTE
"""
def controllo_diagonale(matrice,giocatore):
    prima_riga   = matrice[0]
    seconda_riga = matrice[1]
    terza_riga    = matrice[2]
    
    if prima_riga[0] == seconda_riga[1] == terza_riga[2] or prima_riga[2] == seconda_riga[1] == terza_riga[0]:
        print(f"Hai vinto {giocatore}")
        return 1

        
        
def controllo_verticale(matrice,giocatore):
    prima_riga    = matrice[0]
    seconda_riga  = matrice[1]
    terza_riga    = matrice[2]
    
    if prima_riga[0] == seconda_riga[0] == terza_riga[0] or prima_riga[1] == seconda_riga[1] == terza_riga[1] or prima_riga[2] == seconda_riga[2] == terza_riga[2]:
        print(f"Hai vinto {giocatore}")
        return 1

def controllo_orizzontale(matrice,giocatore):
    prima_riga    = matrice[0]
    seconda_riga  = matrice[1]
    terza_riga    = matrice[2]
    
    if prima_riga[0] == prima_riga[1] == prima_riga[2] or seconda_riga[0] == seconda_riga[1] == seconda_riga[2] or terza_riga[0] == terza_riga[1] == terza_riga[2]:
        print(f"Hai vinto {giocatore}")
        return 1



def mossa_giocatore(mossa,matrice,simbolo):
    
   
    prima_riga    = matrice[0]
    seconda_riga  = matrice[1]
    terza_riga    = matrice[2]
    
    #prima riga
    if mossa == 0:
        if prima_riga[0] == "X" or prima_riga[0] == "O":
            print("riga già occupata")
        else:
            prima_riga[0] = simbolo
        
    if mossa == 1:
        if prima_riga[1] == "X" or prima_riga[1] == "O":
            print("riga già occupata")
        else:
            prima_riga[1] = simbolo
            
    if mossa == 2:
        if prima_riga[2] == "X" or prima_riga[2] == "O":
            print("riga già occupata")
        else:
            prima_riga[2] = simbolo
    
   #seconda riga     
    if mossa == 3:
        if seconda_riga[0] == "X" or seconda_riga[0] == "O":
            print("riga già occupata")
        else:
            seconda_riga[0] = simbolo
        
    if mossa == 4:
        if seconda_riga[1] == "X" or seconda_riga[1] == "O":
            print("riga già occupata")
        else:
            seconda_riga[1] = simbolo
            
    if mossa == 5:
        if seconda_riga[2] == "X" or seconda_riga[2] == "O":
            print("riga già occupata")
        else:
            seconda_riga[2] = simbolo
    
    #terza riga
    if mossa == 6:
        if terza_riga[0] == "X" or terza_riga[0] == "O":
            print("riga già occupata")
        else:
            terza_riga[0] = simbolo
        
    if mossa == 7:
        if terza_riga[1] == "X" or terza_riga[1] == "O":
            print("riga già occupata")
        else:
            terza_riga[1] = simbolo
            
    if mossa == 8:
        if terza_riga[2] == "X" or terza_riga[2] == "O":
            print("riga già occupata")
        else:
            terza_riga[2] = simbolo
    
    return matrice




def stampa_matrice(matrice):
    prima_riga    = matrice[0]
    seconda_riga  = matrice[1]
    terza_riga    = matrice[2]
    
    print(f"""
          |{prima_riga[0]}|{prima_riga[1]}|{prima_riga[2]}|
          |{seconda_riga[0]}|{seconda_riga[1]}|{seconda_riga[2]}|
          |{terza_riga[0]}|{terza_riga[1]}|{terza_riga[2]}|
          """)


def gioco():
    
    tavolo_gioco = [  
                        [0,1,2],
                        [3,4,5],
                        [6,7,8]
        
                   ]

    #scelta nomi giocatore
    giocatore1 = str(input("inserisci nome giocatore 1: "))
    giocatore2 = str(input("inserisci nome giocatore 2: "))
    
    #mosse fatte, max turni si possono fare = 9
    turni = 0 #1 #2 #3 #4 #5 #6 #7 #8 #9
    stampa_matrice(tavolo_gioco)
    while True:
        

        
        #mossa giocatore 1
        scelta = int(input(f"{giocatore1} scrivi il numero della posizione dove mettere la X: "))
        mossa_giocatore(scelta, tavolo_gioco, "X")
        #controlli
        if controllo_diagonale(tavolo_gioco,giocatore1) == 1:
            stampa_matrice(tavolo_gioco)
            break
        if controllo_orizzontale(tavolo_gioco,giocatore1) == 1:
            stampa_matrice(tavolo_gioco)
            break
        if controllo_verticale(tavolo_gioco,giocatore1) == 1:
            stampa_matrice(tavolo_gioco)
            break
        turni += 1
          
        if turni == 9:
            print("PAREGGIO!")
            stampa_matrice(tavolo_gioco)
            break
        
        #mossa giocatore 2
        stampa_matrice(tavolo_gioco)
        scelta = int(input(f"{giocatore2} scrivi il numero della posizione dove mettere il O: "))
        mossa_giocatore(scelta, tavolo_gioco, "O")
        
        #controlli
        if controllo_diagonale(tavolo_gioco,giocatore2) == 1:
            stampa_matrice(tavolo_gioco)
            break
        if controllo_orizzontale(tavolo_gioco,giocatore2) == 1:
            stampa_matrice(tavolo_gioco)
            break
        if controllo_verticale(tavolo_gioco,giocatore2) == 1:
            stampa_matrice(tavolo_gioco)
            break
        
        turni += 1
        
     
        #ristampa per giocatore1
        stampa_matrice(tavolo_gioco)
        
        
gioco()



    
