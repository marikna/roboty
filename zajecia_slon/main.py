#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Direction, Color, Button
from pybricks.tools import wait, StopWatch
from pybricks.media.ev3dev import SoundFile

##################### TUTAJ TWORZYSZ OBIEKTY #################

# INICjAlIZACJA kostki EV3
ev3 = EV3Brick()

# TUTAJ ZAINICJALIZUJ SILNIKI -> wywyołaj klase Motor()
motor_move = Motor(Port.A)
motor_snout = Motor(Port.B)
motor_head = Motor(Port.D)

# TUTAJ ZAINICJALIZUJ CZUJNIK DOTYKU -> wywołaj klasę TouchSensor()
touch_sensor = TouchSensor(Port.S1)

# TUTAJ ZAINICJALIZUJ CZUJNIK KOLORU -> wywołaj klasę ColorSensor()
color_sensor = ColorSensor(Port.S4)

#################### GŁÓWNY PROGRAM  #########################

# wywołaj funkcje, któe robot ma robić
def snout_movement():
    motor_snout.run(-227)

    while not touch_sensor.pressed():
        wait(2)
    motor_snout.brake()

    ev3.speaker.play_file(SoundFile.ELEPHANT_CALL)


def attack():
    for _ in range(10):
        motor_snout.run(-727)
        wait(2)
        motor_snout.brake()
        motor_snout.run(727)
        wait(2)
        motor_snout.brake()
# Po uruchomieniu robota, wydaje on dźwięk
ev3.speaker.beep()

# USTAWIENIE TIMER'a.  Służy do wychodzenia z pętli wejściowej po 1 sekundzie

timer = StopWatch()


# Zad. 1. Zdefiniuj funkcję reset(), która przywraca słonia do pozycji wyjściowej
def reset():

    # Dopóki kolor nie jest czerwony
    # Podnoś głowę do góry (funkcja run() z klasy Motor)
    
    # while UZUPEŁNIJ POLECENIE:
        #czekaj
    #zatrzymaj silnik szyi

    
    while True:
        motor_head.run(750)
        while color_sensor.color() != Color.RED:
            wait(5)
        else:
            break
    motor_head.brake()
    # Podnoś trąbę do momentu naciśnięcia czujnika dotyku
    # skorzystaj z funkcji pressed() z klasy TouchSensor
    # while not UZUPEŁNIJ POLECENIE:
        #czekaj
    while not touch_sensor.pressed():
        motor_snout.run(-227)
    
    motor_snout.brake()

    ev3.speaker.play_file(SoundFile.ELEPHANT_CALL)
    #zatrzymaj silnik trąby

    # Wydaj dźwięk
    #ev3.speaker.play_file(SoundFile.ELEPHANT_CALL)

    # Równocześnie opuść trąbę i głowę
    # Skorzystaj z funkcji run_angle() z klasy Motor    
    wait(0.2)

    # Zresetuj kąt silników trąby i głowy do 0
    # Skorzystaj z funkcji reset_angle z klasy Motor
    # motor_head.reset_angle(0)
    # motor_snout.reset_angle(0)

    motor_head.run_angle(500, -750, wait=True)
    motor_snout.run_angle(500, 227, wait=True)


# Zad. 2. Zdefiniuj funkcję grab() do podnoszenia trąbą przedmiotu
def grab():
    #Uzyj zdefiniowanej wcześniej funkcji reset() do przywrócenia pozycji wyjściowej
    reset()
    motor_snout.run_angle(500, -327, wait=True)
    wait(5)
    motor_snout.run_angle(500, 327, wait=True)

    # Uzyj sekwencji ruchów głowy i trąby do złapania i podniesienia przedmiotu
    # W tym zadaniu mona skorzystać z funkcji run_angle() lub run_time() z klasy Motor

# Główna część programu.
#Zaczynamy od zresetowania ustawień (wywołanie funkcji reset()).

# W pętli while zamieszczamy funkcje, które chcemy wywołać

# This is the main part of the program.  It is a loop that repeats
# endlessly.
#
# First, it resets the Timer and the steps variable.
# Second, it waits for commands given by pressing the Brick Buttons.
# Finally, it runs the legs motor if the steps variable is not "0."
#
# Then the process starts over, so it can accept new commands.

while True:

    # Resetujemy timer i ustawiamy zmienną step na 0
    timer.reset()
    steps = 0

    # Zad. 3. Sterowanie przyciskami na kostce EV3
    # Czekaj do momentu przyciśnięcia dowolnego przycisku na kostce
    # skorzystaj z funkcji buttons.pressed() z klasy EV3Brick
    while not ev3.buttons.pressed():
        buttons = ev3.buttons.pressed()
    
    

    # Pętla while zawiera informację jak robot ma się zachować po 
    # naciśnięciu poszczególnych przycisków na kostce
    while timer.time() < 1000:
        # Jeśli wciśnięty jest przycisk UP:
            #zwiększ wartość steps o 1
            #inna opcja: idz do przodu 5 kroków
            if Button.UP in buttons:
                motor_move.run_time(-900, 7000)
            elif Button.DOWN in buttons:
                motor_move.run_time(900, 7000)
            elif Button.RIGHT in buttons: 
                snout_movement()
                reset()
            elif Button.LEFT in buttons:
                grab()

            motor_move.brake()
            wait(1)
            buttons = ev3.buttons.pressed()
            
            timer.reset()
            # ev3.speaker.beep(600)

            # Czekaj az przycisk UP zostanie zwolniony
            # uzyj pętli while i polecenia wait

        # rozpisz warunki if dla pozostałych przycisków (np down - idz do tylu
        # center - podnies i przenies przedmiot, itp.)
        

    # jeśli steps != 0:
    # Zrób tyle kroków, ile wynosi wartość zmiennej steps
    # Kazdy krok wymaga obrotu silnika o 900 stopni
    # uzyj funkcji run_angle() z klasy motors i zmiennej steps

