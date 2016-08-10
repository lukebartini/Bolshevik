"""
    Bolshevik
    By Luke Bartini  2015
"""

import time, sys, random, difflib, kremlinMap
from sleep import load_3
from parse import parseText
from spellCheck import seeIfCloseMatch
'''from kremlinMap import kremlinMapPrint_1_1, kremlinMapPrint_1_2,
kremlinMapPrint_2_2, kremlinMapPrint_1_2_second, kremlinMapPrint_1_3,
kremlinMapPrint_1_4, kremlinMapPrint_1_5, kremlinMapPrint_2_4,
kremlinMapPrint_2_5'''
from kremlinMap import *

#******GLOBAL DATA******

xList = [] #used for input, and erased using del and add using append
xList2 = [] #used for yes no and 1 2 questions
xList3 = [] #used for directionals in forest
inventory = {'weapons': ''}

i = True

#when storing 1 and 2, 1 = yes and 2 = no

stats = {'x': 1,
         'y': 1,
         'x2': 1,
         'y2': 1, #used for in kremlin
         'movesTaken1': 1,
         'character': '',
         'name': '',
         'health': 100,
         'intelligence': 0,
         'strength': 0,
         'charm': 0,} #dictionary to record stats

#dictionary to record monsters.
monsters = {'Kremlin Guard': {'desc': ('Oh no! You have encountered a Kremlin Guard. They are heavily armed but only use deadly force '
                                       'when absolutely necceasary. You should be able to kill him quickly.'),
                              'health': 100,
                              'strength': 2},
            'Vladimir Putin': {'desc': ('You have finally encountered the legend himself, Vlad Putin. He is not armed, but is extremely '
                                        'strong.'),
                               'health': 100,
                               'strength': 7}}  

roomData = {}

#******GENERAL FUNCTIONS******

def slowPrint(s, delay = 0.025, maxLineLength = 80, deleteNewLines = True):
    
    import time, sys

    if deleteNewLines:
        s = s.replace('\n', ' ')
        s = s.replace('~', '\n')
    
    length = 0
    index = 0

    for c in s:
        index += 1
        length += 1
        if c == ' ':
            #Don't print the space if it is the first line character
            if length == 1:
                length -=1
                continue
            #If space is last character or would start next line don't print it
            if length >= maxLineLength - 1:
                length = 0
                print 
                continue
            nextWord = s[index:].find(' ')
            nextLine = s[index:].find('\n')
            if nextLine < nextWord and nextLine != -1:
                nextWord = nextLine
            if length + nextWord > maxLineLength and length > maxLineLength - 20:
                length = 0
                print
                continue
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
        if c == '\n':
            length = 0
        if length == maxLineLength:
            print
            length = 0
    print

def instruction():
    global xList #not local
    
    print
    x = raw_input('Instruction >> ').lower() #main use for input
    print
    
     #add to xList

    if x == 'stats':
        printStats()
    elif x == 'location':
        printLocation()
    elif x == 'help':
        Help()

    xList.append(x)

def instruction2():
    global xList2 #not local
    
    print
    x2 = raw_input('Instruction >> ').lower() #main use for yes/no
    print

    xList2.append(x2) #add to xList
    
    if x2 == 'yes':
        xList2.append('1')

    elif x2 == 'no':
        xList2.append('2')

    elif x2 == 'stats':
        printStats()
    elif x2 == 'location':
        printLocation()
    elif x2 == 'help':
        Help()

    else:
        slowPrint("I'm sorry, %s is not a valid command'" %xList2)
            


def moves2():
    one = raw_input('Instruction >> ')
    
    if one == 'w' or 'west':
        stats['x'] += 1 #adds 1 to xCoord

    elif one == 'n' or 'north':
        stats['y'] -= 1

    elif one == 'e' or 'east':
        stats['x'] += 1

    elif one == 's' or 'south':
        stats['y'] += 1

    elif one == 'stats':
        printStats()
    elif one == 'location':
        printLocation()
    elif one == 'help':
        Help()

    else:
        slowPrint("I'm sorry, %s is not a valid command'" %one)

def checkRoom():
    if stats['x'] is 1 and stats['y'] is 1:
        russiaGrassLand_1_1()

def printLocation():
    print
    print 'x: ', stats['x']
    print 'y: ', stats['y']
    print
    
def printStats():
    slowPrint('Character: ' + str(stats['character']))
    slowPrint('Name: ' + str(stats['name']))
    slowPrint('Health: ' + str(int(stats['health'])))
    slowPrint('-' * 40)
    slowPrint('Intelligence: ' + str(int(stats['intelligence'])))
    slowPrint('Strength: ' + str(int(stats['strength'])))
    slowPrint('Charm: ' + str(int(stats['charm'])))
    slowPrint('-' * 40)

def Help():
    slowPrint('At any time during the game, type "stats" to see information about your character. Or type "location" at any '
              'time to see coordinate locations. *Note* location is only a valid command when used in either the Russian Forest, '
              'or in the Kremlin. ')

def moves():
    print
    one = raw_input('Instruction >> ')
    print
    
    if one is 'n':
        stats['y'] += 1
        
    elif one is 'w':
        stats['x'] -= 1

    elif one is 'e':
        stats['x'] += 1

    elif one is 's':
        stats['y'] -= 1

    elif one == 'location':
        printLocation()
        moves()

    elif one == 'stats':
        printStats()
        moves()

    elif one == 'help':
        print Help()
        moves()

    else:
        slowPrint("I'm sorry, %s is not a valid direction" %one)
        moves()

def movesKremlin():
    print
    one = raw_input('Instruction >> ')
    print
    
    if one is 'n':
        stats['y2'] += 1
        
    elif one is 'w':
        stats['x2'] -= 1

    elif one is 'e':
        stats['x2'] += 1

    elif one is 's':
        stats['y2'] -= 1

    elif one == 'stats':
        printStats()
        moves()

    elif one == 'help':
        print Help()
        moves()

    else:
        slowPrint("I'm sorry, %s is not a valid direction" %one)
        moves()


def gameOver():
    dividerEqual = '=' * 35 #adds equals above and below text lines
    print dividerEqual.center(79, ' ')
    gameTitle = 'YOU LOSE! GAME OVER'
    print gameTitle.center(80, ' ') #prints it 80 spaces from the left edge, (center)
    print dividerEqual.center(79, ' ')
    time.sleep(1.5)
    print dividerEqual.center(79, ' ')
    projectName = 'COME BACK SOON!'
    print projectName.center(80, ' ')
    print dividerEqual.center(79, ' ')

    time.sleep(2)

    i = False
    
    sys.exit #terminate python shell

def welcomeScreen(): #starting screen text
    time.sleep(.5)
    dividerEqual = '*' * 35 #adds equals above and below text lines
    print dividerEqual.center(79, ' ')
    gameTitle = 'BOLSHEVIK. VERSION 1.0'
    print gameTitle.center(80, ' ') #prints it 80 spaces from the left edge, (center)
    print dividerEqual.center(79, ' ')
    time.sleep(1.5)
    print dividerEqual.center(79, ' ')
    projectName = 'A CLASSIC TEXT ADVENTURE RPG'
    print projectName.center(80, ' ')
    print dividerEqual.center(79, ' ')
    time.sleep(1.5)
    print dividerEqual.center(79, ' ')
    creatorName = 'BY LUKE BARTINI'
    print creatorName.center(80, ' ')
    print dividerEqual.center(79, ' ')
    time.sleep(1.5)
    print dividerEqual.center(79, ' ')
    copyrightDate = 'COPYRIGHT 2015'
    print copyrightDate.center(80, ' ')
    print dividerEqual.center(79, ' ')
    time.sleep(.5)

def printIntro():

    print
    slowPrint('You wake up in a delirious state, eyes refusing to open, and suddenly you hear a knock on your door. '
              'You get up to go see who is waking you at this ungodly hour. Before you can get to the door of your '
              'small Washington D.C. apartment, a SWAT team has burst through the double lock enforced door. Six '
              'strange men dressed in all black advance towards you, hit you over the head with their battering ram. '
              'And that is all you remember.')
    print
    print
    slowPrint('And so it begins...')
    print
    print
    time.sleep(2)

def acceptDecline():
    #need to say yes in order to play the game
    slowPrint('Will you accept your duty or not and decline only to pay the penalty of five years in prison?(yes/no)')
    instruction2()

    if '1' in xList2:
        airplane_1()
    else:
        slowPrint('You have disgraced not only yourself, but your country. You will inevitably pay for this while '
                  'you rot in prison...')
        gameOver()

def checkForestLocation():
    if stats['x'] is 1 and stats['y'] is 1:
        slowPrint('You are in the forest. The ground is covered in 1 foot of snow. There are trees on all sides of you, the airport is '
                  'to the south.')
    elif stats['x'] is 2 and stats['y'] is 1:
        slowPrint('You are in the forest. You are surrounded by trees, and can hear crackling of branches over the howling wind.')

def characterRoll():
    slowPrint('Before we start the adventure, you will need to pick a character, and a name. ')
    print
    slowPrint('What is your preferred character:')
    print
    slowPrint('Engineer ')
    slowPrint('Chemist ')
    slowPrint('Lawyer ')
    slowPrint('Computer Scientist ')
    print
    print
    slowPrint('To see stats/descriptions of characters, type "character stats". ')
    
    instruction()
    
    if 'character stats' in xList:
        slowPrint('Engineer: ')
        slowPrint('The engineer is clever character, and can think on their feet.')
        slowPrint('Intellignece: 8')
        slowPrint('Strength: 4')
        slowPrint('Charm: 6')
        slowPrint(' ')
        slowPrint('Chemist: ')
        slowPrint('The chemist is a logical thinker, and has high strength, due to the supplements they take.')
        slowPrint('Intelligence: 8')
        slowPrint('Strength: 8')
        slowPrint('Charm: 2')
        slowPrint(' ')
        slowPrint('Lawyer: ')
        slowPrint('The lawyer is a calm, witty person, who dresses well but easily stands out in public.')
        slowPrint('Intelligence: 6')
        slowPrint('Strength: 4')
        slowPrint('Charm: 8')
        slowPrint(' ')
        slowPrint('Computer Scientist: ')
        slowPrint('The computer scientist is a genuis, who easily manipulates people, but is not well liked.')
        slowPrint('Intelligence: 8')
        slowPrint('Strength: 8')
        slowPrint('Charm: 2')
        slowPrint(' ')
        time.sleep(2)
        del xList[:]
        instruction()
    else:
        pass
        
    if 'engineer' in xList:
        slowPrint('What is your name, Engineer: ')
        print
        name = raw_input('Instruction >> ').title()
        print
        stats['name'] += name
        stats['intelligence'] += 8
        stats['strength'] += 4
        stats['charm'] += 6
        stats['character'] += 'Engineer'
    elif 'chemist' in xList:
        slowPrint('What is your name, Chemist: ')
        print
        name = raw_input('Instruction >> ').title()
        print
        stats['name'] += name
        stats['intelligence'] += 8
        stats['strength'] += 8
        stats['charm'] += 2
        stats['character'] += 'Chemist'
    elif 'lawyer' in xList:
        slowPrint('What is your name, Lawyer: ')
        print
        name = raw_input('Instruction >> ').title()
        print
        stats['name'] += name
        stats['intelligence'] += 6
        stats['strength'] += 4
        stats['charm'] += 8
        stats['character'] += 'Lawyer'
    elif 'computer scientist' in xList:
        slowPrint('What is your name, Computer Scientist: ')
        print
        name = raw_input('Instruction >> ').title()
        print
        stats['name'] += name
        stats['intelligence'] += 8
        stats['strength'] += 8
        stats['charm'] += 2
        stats['character'] += 'Computer Scientist'
    else:
        slowPrint("I'm sorry, %s is not a valid command." %xList)
        del xList[:]
        instruction()

def callMap():
    global i
    
    if stats['x'] is 1 and stats['y'] is 1:
        pass

    openingText()
    acceptDecline() #see if you play the game, or quit
    russia_1()
   
    while True:
        checkForestLocation()
        moves()
        stats['movesTaken1'] += 1
        
        if stats['x'] is -1 and stats['y'] is 4:
            slowPrint('You have reached the exit of the forest, and ahead of you is the beloved Russian Kremlin.')
            print
            slowPrint('You slowly proceed to the entrance, where you are taken into the vistor region')
            print
            slowPrint('Look at the view!')
            print
            break
        
        elif stats['movesTaken1'] is 6:
            slowPrint('Slow down! *The Kremlin is in the northwest corner of the forest! The coordinates are (-1, 4)!!! Remember to check location using "location"')
            print
        slowPrint(random.choice(possibleDescForest))

    kremlin_1()


    ##As of now, you need to follow precise directions, or else you will not be able to finish the game, alternate endings will be created.##

    while i is True:
        kremlinMapPrint_1_1()
        slowPrint('You have entered the Kremlin, below is a map. You are represented by X, and need to make it to the room of Vladimir Putin.')
        print
        print
        time.sleep(2)
        movesKremlin()
        if stats['x2'] is 1 and stats['y2'] is 2:
            kremlinMapPrint_1_2()
            print
            print
            slowPrint('**Go and grab the gun, in the western corridor.**')
            print
            print
            movesKremlin()
            if stats['x2'] is 0 and stats['y2'] is 2:
                kremlinMapPrint_2_2()
                print
                print
                slowPrint('The gun is straight ahead, type "gun" to take it')
                print
                instruction()
                if 'gun' in xList:
                    print
                    slowPrint('You have obtained the gun')
                    print
                    inventory['weapons'] += 'gun'
                    slowPrint('You travel back to the hallway:')
                    stats['x2'] += 1
                    kremlinMapPrint_1_2_second()
                    print
                    print
                    slowPrint('Now go north to reach the room')
                    movesKremlin()
                    if stats['x2'] is 1 and stats['y2'] is 3:
                        kremlinMapPrint_1_3()
                        print
                        print
                        slowPrint('Now, go north.')
                        movesKremlin()
                        if stats['x2'] is 1 and stats['y2'] is 4:
                            kremlinMapPrint_1_4()
                            print
                            print
                            slowPrint('Now go west to reach the room')
                            movesKremlin()
                            if stats['x2'] is 0 and stats['y2'] is 4:
                                kremlinMapPrint_2_4()
                                print
                                print
                                slowPrint('Oh no, you encountered a Kremlin Guard! You will have to fight and kill him to reach Putin!')
                                print
                                slowPrint('As of right now, this is the end of the game, I made a battle function but could not get it working.')
                                break
                            else:
                                slowPrint('You made a disturbance messing around! The gaurds quickly catch you, and lock you up.')
                                print
                                gameOver()
                                break
                        else:
                            kremlinMapPrint_1_5()
                            slowPrint('You made a disturbance messing around! The gaurds quickly catch you, and lock you up.')
                            print
                            gameOver()
                            break
                            
                else:
                    slowPrint('You made a disturbance messing around! The gaurds quickly catch you, and lock you up.')
                    print
                    gameOver()
                    break
        else:
            slowPrint('You made a disturbance messing around! The gaurds quickly catch you, and lock you up.')
            print
            gameOver()
            break

    gameOver()
    
                
                          
                
#******ROOMS******

def openingText():
    slowPrint('Good morning, %s. You have been randomly selected by the US Government to fulfill your taxes, and prove your American '
              'citizenship. Each day, one human is randomly selected to carry out an action or plan created by the Government, whether '
              'it be a civil duty or military duty.' %stats['name'])
    time.sleep(2)
    print
    slowPrint('Instruction >> ')
    time.sleep(.7) #turn console off for .7 seconds
    print #adding two blank lines for aesthetics
    slowPrint('Before you can speak or move, you are cutoff by the agent, and you realize you are handcuffed to the chair you are sitting '
              'in. You wiggle your arms, but nothing can be done. You are trapped. ** Your only (smart) option is to talk to the agent.')
    print
    slowPrint('Would you like to talk to the agent? (yes/no)')
    
    instruction2()

    if '1' in xList2:
        slowPrint('AGENT: You are under arrest, and will be held under government watch if you decline your duty, and will be brainwashed. '
        'Your options are to complete the mission that is currently disclosed, or stay under government arrest for 5 years. ')
        print
        print
        #slowPrint('Will you accept or decline the request?')
    elif '2' in xList2:
        slowPrint('How dare you disresepct the agent by not speaking to him?')
        slowPrint('You are hit by the Agent.')
        print
        slowPrint('You lose 10 points of health.')
        print
        stats['health'] -= 10
        slowPrint('Health: ' + str(int(stats['health'])))
        print
        slowPrint('AGENT: You are under arrest, and will be held under government watch if you decline your duty, and will be brainwashed. '
                  'Your options are to complete the mission that has is currently disclosed, or stay under government arrest for 5 years. ')
        print
        pass #leave function
        
    else:
        slowPrint('You cannot do that here, doing so can and will jeopardize your life.')
        instruction()
        if xList is 'quit':
            gameOver()
        else:
            openingText()

def airplane_1():
    slowPrint('You accept the challenge nobley. You are taken by agents to the nearest airport, Ronald Reagan National Airport, where '
              'you will meet with President Obama. ')
    print
    slowPrint('You will be escorted at top speed to the airport, and the roads will be blocked to ensure the mission is completely ASAP')
    print
    slowPrint('While in the convoy to the airport, the agents forgot to tie you down to your seat, and your door is unlocked. '
              'For a quick second, you have the option to either talk to the agent, jump out of the car, or stay silent. '
              '(jump/talk/silent)')

    instruction() #Get input

    if 'jump' in xList:
        slowPrint('You jump out of the car. Due to its high speed, right when you hit the ground you are quickly thrown back, sliding '
                  'against the pavement, and eventually hit by a car. You are left in critical condition.')
        print
        slowPrint('Instruction >> ')
        time.sleep(.7)
        print
        slowPrint('Before you can do anything, you are fired at from all directions, bringing you to your death. ')

        gameOver()

    elif 'talk' in xList:
        slowPrint('You speak out to the agent in the front.')
        print
        time.sleep(.7)
        slowPrint("AGENT: 'Shutup peasant, do not speak unless spoken to.'")
        print
        del xList[:]
        slowPrint('You arrive at the airport shortly after.')
        print
        airplane_2()

    elif 'silent' in xList:
        slowPrint('You arrive at the airport shortly.')
        del xList[:]
        print
        airplane_2()

    elif 'cheat' in xList:
        print 'WINNER... WINNER...'
        

    else:
        slowPrint('I do not understand what you want to do... ')
        print
        del xList[:]
        slowPrint('Before long, you reach the airport, where you now will meet with Mr. Obama.')
        airplane_2()

def airplane_2():
    print
    slowPrint('When you arrive at the airport, you are escorted inside to a private room ')
    time.sleep(1)
    print
    slowPrint('Shortly after, you go and see the President, where he presents the logistics of your journey and duty.')
    print
    slowPrint('Here is your itinerary:')
    time.sleep(.5)
    print
    dividerEqual = '=' * 40 #adds equals above and below text lines
    print dividerEqual.center(79, ' ')
    gameTitle = 'Travel to Russia...'
    print gameTitle.center(80, ' ') #prints it 80 spaces from the left edge, (center)
    print dividerEqual.center(79, ' ')
    time.sleep(1.5)
    print dividerEqual.center(79, ' ')
    projectName = 'Enter the Kremlin...'
    print projectName.center(80, ' ')
    print dividerEqual.center(79, ' ')
    time.sleep(1.5)
    print dividerEqual.center(79, ' ')
    creatorName = 'Find the room of Vladimir Putin...'
    print creatorName.center(80, ' ')
    print dividerEqual.center(79, ' ')
    time.sleep(1.5)
    print dividerEqual.center(79, ' ')
    copyrightDate = 'Execute him...'
    print copyrightDate.center(80, ' ')
    print dividerEqual.center(79, ' ')
    time.sleep(.5)
    print dividerEqual.center(79, ' ')
    copyrightDate2 = 'And make it back safely.'
    print copyrightDate2.center(80, ' ')
    print dividerEqual.center(79, ' ')
    time.sleep(.5)
    print
    airplane_3()

def airplane_3():
    slowPrint('After receiving your itinerary, you slowly make your way on to the plane.')
    print
    slowPrint('You slowly sit down, and can only see an agent ahead of you.')
    print
    slowPrint('The agent does not look in the mood to talk...')
    print
    slowPrint('Instruction >> ')
    time.sleep(.7)
    print
    slowPrint('Before you can speak, you are knocked unconscious for the remainder of the ride.')
    print
    slowPrint('The remainder of the plane ride will be simulated ...')
    print
    time.sleep(5)
    load_3()
    time.sleep(3)
    print
    print


possibleDescForest = ['You are in the forest. The ground is covered in 1 foot of snow. There are trees on all sides of you, the airport is '
                      'to the south.', 'You are in the forest. You are surrounded by trees, and can hear crackling of branches over the '
                      'howling wind.', 'You are nestled deep within the forest, where nothing can be seen on all sides of you. ',
                      'You are trudging through the thick snow, surrounded by trees on all sides.', 'The roars of the wind are trying '
                      'to overcome you. You should find the entrance as quick as possible before you suffer from hypothermia. ', 'You '
                      'are surrounded on all sides, but can nearly smell the Kremlin. ']

possibleDescKremlin = []


def russia_1():
    slowPrint('Once you arrive to Russia, you are in an snow covered forest. You have no sense of direction, and you were aburptly dropped '
              'off at the landing station, where you are left alone, with nothing but yourself, a backpack, and an earpiece')
    print
    slowPrint('Through the earpiece, you are connected to a CIA control room, where people are monitoring your GPS location, and '
              'ready to give you directions and intel.')
    print
    slowPrint('Earpiece communications are denoted with asterisk, i.e: *Hello*.')
    print
    time.sleep(2)
    slowPrint('*Ok, ahead of you is forest, behind is the airport. You need to travel through the forest, and find the Kremlin.*')
    print
    slowPrint('The Kremlin is near the northwest corner of the forest.')
    print
    slowPrint('Please denote direction using cardinal directionals. (n, e, s, w.)')
    print
    """
    checkForestLocation()
    moves()
    checkForestLocation()
    if stats['x'] is 1 and stats['y'] is 1:
        slowPrint('You are in the forest. The ground is covered in 1 foot of snow. There are trees on all sides of you, the airport is '
                  'to the south.')
    """
                  

def kremlin_1():
    slowPrint('While in the vistor region, you are given a map of the Kremlin. *Little do they know that you are not an ordinary visitor!*')
    print
    print
    slowPrint('You are now inside of the Kremlin, where you now need to obtain a weapon, and kill Putin.')
    print
    pass


#******MAIN******
    
def main():
    #Start game

    if stats['x'] is 1 and stats['y'] is 1:
        welcomeScreen()
        printIntro()
        slowPrint('At any time during the game, type "stats" to see information about your character. And "location" to see coordinates')
        print
        slowPrint('You may also type "help" for a list of commands.')
        print
        time.sleep(2)
        characterRoll()
        pass

    
    callMap() #initiate room sequencing

    if xList is 'print stats':
        printStats()
    
if __name__ == '__main__':
    #If run as primary (not imported) call main
    pass
    main()

