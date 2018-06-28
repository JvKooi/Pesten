#!/usr/bin/python3
import sys
import random
import time
import klassen
import spelstarten
import spelspelen
import computer
import pestkaarten
instelling_aantal_spelers = spelstarten.instelling_aantal_spelers
instelling_aantal_kaarten = spelstarten.instelling_aantal_kaarten

if __name__ == '__main__':   
    volgorde = spelstarten.speelvolgorde(instelling_aantal_spelers)
    beurt=0
    gespeeld = []
    deck = spelstarten.deck_aanmaken()
    handen=spelstarten.handen_aanmaken(volgorde,deck,instelling_aantal_kaarten)
    pot = klassen.hand()
    spelspelen.kaart_pakken(pot,deck)
    start = time.time()
    spelspelen.spel_spelen(beurt,deck,gespeeld,pot,handen,volgorde)
    end = time.time()
    print('Dit spel duurde' ,int(end-start)//60,'minuten en',int(end-start)-60*(int(end-start)//60),'seconden')
