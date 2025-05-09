from sys import exit
from random import randint
from textwrap import dedent

class Scene():
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine():

    def __init__(self, scene_map):
        #Assign a Map object to scene_map
        self.scene_map = scene_map
    
    def play(self):
        #Using the Map object assigned to scene_map, assign the value of opening_scene method to current_scene
        current_scene = self.scene_map.opening_scene()

        #Assign the Finished() class declaration to last_scene
        last_scene = self.scene_map.next_scene('finished')
        

        #Loop through rooms until current_scene has the same value as last_scene
        while current_scene != last_scene:
            #Enter the current scene
            next_scene_name = current_scene.enter()
            #Assign the value of the next scene to current_scene
            current_scene = self.scene_map.next_scene(next_scene_name)

        #Run the final room
        current_scene.enter()

class Death(Scene):
    quips = [ "You died. You kinda suck att his.",
                 "Your mom would be proud...if she were smarter.",
                 "Such a loser.",
                 "I have a small puppy that's better at this.",
                 "You're worse than your Dad's jokes."
            ]
    
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    
    def enter(self):
        print(dedent(""""
                     The Gothons of Planet Percal #25 have invaded your ship
                     and destroyed your entire crew. You are the last surviving memeber and your
                     last mission is to get the neutron destruct bomb from the Weapons Armory,
                     put it in the bridge, and blow up the ship after getting into an escape pod.

                     You're running down the central corridor to the Weapons Armory when a Gothon jumps
                     out, red scaly skin, dark grimy teeth, and evil clown custom flowing around his
                     hate filled body. He's blocking the door to the Armory and about to pull a
                     weapon to blast you.
                     """))
        
        action = input("> ")

        if 'shoot' in action:
            print(dedent("""
                         Quick on the draw you yank out your blaster and fire at the Gothon. His clown
                         costume is flowing and moving around his body, which throws off your aim.
                         Your laser hits his costume but misses him entirely. This completely ruins his brand
                         new custome his mother brought him, which makes him fly into an insane rage
                         and blast you repeatedly in the face until you are dead. Then he eats you.
                         """))
            return 'death'
        
        elif 'dodge' in action:
            print(dedent("""Like a world class boxer you dodge, weave, slip and slide right as thr Gothon's blaster
                         cranks a laster past your head. In the middle of your artful dodge your foot slips and you bang
                         your head on the metal wall and pass out. You wake up shortly after only to die as the Gothon stomps on your 
                         head and eats you.
                         """))
            return 'death'
        
        elif 'tell a joke' in action:
            print(dedent("""Luckily for you they made you learn Gothon insults in the academy. You tell the one 
                         Gothon joke you know: Lbhezbgurevffbsng, jurafurfvgfnebhaqgurubhfr. The Gothon stops, tries 
                         not to laugh, then busts out laughing and can't move. While he's laughing you run up and shoot him, putting him down. 
                         Then you jump through the Weapon Armory door.
                         """))
            return 'laser_weapon_armory'
        
        else: 
            print("DOES NOT COMPUTE")
            return 'central corridor'

class LaserWeaponArmory(Scene):
    
    def enter(self):
        print(dedent("""
                     You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons
                     that might be hiding. It's dead quiet, too quiet. You stand up and run to the far side of the room
                     and find the netruon bomb in its container. There's a keypad lock on the box and you need the code 
                     to get the bomb out. If you get the code wrong 10 times then the lock closes forever 
                     and you can't get the bomb. The code is 3 digits long. 
                     """))
        
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("Enter code> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZT! WRONG!")
            guesses += 1
            guess = input("Enter code> ")
        
        if guess == code:
            print(dedent("""The container clicks open and the seal breaks, letting gas out. 
                         You grab the neutron bomb and run as fast as you can to the bridge where you must
                         place it in the right spot.
                         """))
            return 'the_bridge'
        else:
            print(dedent("""The lock buzzes one last time and then you hear a sickening melting sound 
                         as the mechanism is fused shut. You decide to sit there, defeated, and finally the Gothons blow
                         up the ship from their ship and you die.
                         """))
            return 'death'

class TheBridge(Scene):
    
    def enter(self):
        print(dedent(""""You burst onto the Bridge with the neutron destruct bomb under
                     your arm and surprise 5 Gothons who are trying to take control of the ship. Each
                     of them has an even uglier clown costume than the last. They haven't pulled their weapons out yet, as 
                     they see the active bomb under your arm and don't want to set it off."""))
    
        action = input("> ")
        
        if 'throw' in action:
            print(dedent("""In a panic you throw the bomb at the group of Gothons and make a leap for the door.
                         Right as you drop it a Gothon shoots you in the back, killing you. As you die you see another Gothon
                         frantically try to disarm the bomb. You die knowing they will probably blow up when it goes off.
                         """))
            return 'home'
        
        elif 'place bomb' in action:
            print(dedent("""You point your blaster at the bomb under youe arm and the Gothon's put their hands up and 
                         start to sweat. You inch backward to the door, open it, and then carefully place the bomb on the floor,
                         pointing your blaster at it. You then jump back through the door, punch the close button 
                         and blast the lock so the Gothons can't get out. Now that the bomb is palced you run to the escape pod to get off
                         this tin can."""))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE")
            return 'the_bridge'

class EscapePod(Scene):
    
    def enter(self):
        print(dedent("""You rush through the ship desperately trying to make it to the escape pod
                     before the whole ship explodes. It seems like hardly any Gothons are on the ship, so your run
                     is clear of interference. You get to the chamber with the escape pods, and now need to pick one to take.
                     Some of them could be damaged but you don't have time to check. There are three pods, which one will you take?"""))
        
        good_pod = randint(1,3)
        guess = input("Pod #: ")

        if int(guess) != good_pod:
            print(dedent("""You jump into pod {guess} and hit the eject button. The pod escapes into the void of space,
                         then implodes as the hull ruptures, curshing your body. """))
            return 'death'
        else:
            print(dedent("""You jump into pod {guess} and hit the eject button. The pod easily slides out into space heading
                         to the planet below. As it flies to the planet, you look back and see the ship implode then explode like a bright
                         star, taking out the Gothon ship in the explosion. You won and survived!"""))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job!")
        return 'finished'

class Map(object):


    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    scenes = {'central_corridor': CentralCorridor(),
              'laser_weapon_armory':LaserWeaponArmory(),
              'the_bridge':TheBridge(),
              'escape_pod':EscapePod(),
              'death':Death(),
              'finished':Finished(),
              }
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


#Create a Map object with its start_scene attribute set to the passed argument (a key from scenes dictionary).
a_map = Map('central_corridor')

#Create an Engine object with the scene_map attribute assigned to a Map object to access methods and the scenes attribute/dictionary.
a_game = Engine(a_map)

#Begin the game. 
a_game.play()