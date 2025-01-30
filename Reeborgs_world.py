
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def jump1():
    
    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
goal_pos=at_goal()

while not goal_pos:
    front=front_is_clear()
    front_wall=wall_in_front()
    
    if front:
       move()
    if front_wall:
        turn_left()
        wall_in_right=wall_on_right()
        while wall_in_right:
            move()
            wall_in_right=wall_on_right()
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        turn_left()
        
        
        
        
        
    
    goal_pos=at_goal()











