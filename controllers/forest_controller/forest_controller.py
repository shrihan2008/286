from controller import Robot
from controller import Keyboard
import random
robot = Robot()
keyboard = Keyboard()

timestep=64
automode=True
wheel1=robot.getDevice("wheel1")
wheel1.setPosition(float('inf'))
wheel1.setVelocity(0.0)

wheel2=robot.getDevice("wheel2")
wheel2.setPosition(float('inf'))
wheel2.setVelocity(0.0)

wheel3=robot.getDevice("wheel3")
wheel3.setPosition(float('inf'))
wheel3.setVelocity(0.0)

wheel4=robot.getDevice("wheel4")
wheel4.setPosition(float('inf'))
wheel4.setVelocity(0.0)

speed=4
random_direction=0
keyboard.enable(timestep)

while (robot.step(timestep) !=-1):
   
    key_pressed= keyboard.getKey()
    print(key_pressed)
    
    # front movement - press up arrow key
    if(key_pressed== 315):
        wheel1.setVelocity(speed)
        wheel2.setVelocity(speed)
        wheel3.setVelocity(speed)
        wheel4.setVelocity(speed)
        
    # back movement - press down arrow key   
    if(key_pressed== 317):
        wheel1.setVelocity(-speed)
        wheel2.setVelocity(-speed)
        wheel3.setVelocity(-speed)
        wheel4.setVelocity(-speed)
        
    if(prev_key==-1 and key_pressed=65):
        autoMode=not autoMode
    
    # left movement - press left arrow key      
    if(key_pressed== 314):
        wheel1.setVelocity(-speed)
        wheel2.setVelocity(speed)
        wheel3.setVelocity(-speed)
        wheel4.setVelocity(speed)
    
    # right movement - press right arrow key     
    if(key_pressed== 316):
        wheel1.setVelocity(speed)
        wheel2.setVelocity(-speed)
        wheel3.setVelocity(speed)
        wheel4.setVelocity(-speed)
    
    # if no key is pressed   
    if(key_pressed== -1):
        wheel1.setVelocity(0)
        wheel2.setVelocity(0)
        wheel3.setVelocity(0)
        wheel4.setVelocity(0)
    
    if(number_of_turns==0):
        random_direction=random.choice([0,1])
        
    if(number_of_turns>1):
        number_of_turns-=1
        
        if(random_direction==0):
            wheel1.setVelocity(-speed)
            wheel2.setVelocity(speed)
            wheel3.setVelocity(-speed)
            wheel4.setVelocity(speed)
        elif(random_direction==1):
            wheel1.setVelocity(speed)
            wheel2.setVelocity(-speed)
            wheel3.setVelocity(speed)
            wheel4.setVelocity(-speed)
            
        else:
            wheel1.setVelocity(speed)
            wheel2.setVelocity(speed)
            wheel3.setVelocity(speed)
            wheel4.setVelocity(speed)
            
    