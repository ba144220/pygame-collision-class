from vector_operations import *
def ball_block_detect(ball, block):
    ball_x, ball_y = ball.pos
    r = ball.r
    x1 = block.x1-1
    x2 = block.x2+1
    y1 = block.y1-1
    y2 = block.y2+1
    x0 = x1 - r
    x3 = x2 + r
    y0 = y1 - r
    y3 = y2 + r
    block_id = block.id  


    collided = False
    active = True
    action = None


    if block_id in ball.collided:
        active = False
    
    # detect collision
    if not (ball_x < x0 or ball_x > x3 or ball_y < y0 or ball_y > y3):
        
        if ball_x >= x1 and ball_x <= x2:
            if ball_y >= y0 and ball_y <= y1:
                print('block top')

                action = 't'

                collided = True
            elif ball_y <= y3 and ball_y >= y2:
                print('block bottom')

                action = 'b'

                    # ball.v = reflect(ball.v, (0,1))
                
                collided = True
        
        elif ball_y >= y1 and ball_y <= y2:
            if ball_x >= x0 and ball_x <= x1:
                print('block left')

                action = 'l'
                    # ball.v = reflect(ball.v, (-1,0))
                
                collided = True
            elif ball_x <= x3 and ball_x >= x2:
                print('block right')

                action = 'r'

                    # ball.v = reflect(ball.v, (1,0))
                
                collided = True
        
        if collided == False:
            if distance(ball.pos, (x1, y1)) <= r:
                print('block top left')

                action = 'tl'
                    # axis = (ball_x - x1, ball_y - y1) 
                    # ball.v = reflect(ball.v, axis)
                
                collided = True
            elif distance(ball.pos, (x2, y1)) <= r:
                print('block top right')  
                action = 'tr'
                    # axis = (ball_x - x2, ball_y - y1) 
                    # ball.v = reflect(ball.v, axis)
                
                collided = True
            elif distance(ball.pos, (x2, y2)) <= r:
                print('block bottom right')  
                action = 'br'
                    # axis = (ball_x - x2, ball_y - y2) 
                    # ball.v = reflect(ball.v, axis)
                
                collided = True
            elif distance(ball.pos, (x1, y2)) <= r:
                print('block bottom left')  
                action = 'bl'
                    # axis = (ball_x - x1, ball_y - y2) 
                    # ball.v = reflect(ball.v, axis)
                
                collided = True

    if collided == True and active==True:
        ball.collided.append(block_id)
        block.hit()

        if action == 't':
            axis = (0,-1)
        elif action == 'b':
            axis = (0,1)
        elif action == 'l':
            axis = (-1,0)
        elif action == 'r':
            axis = (1,0)
        elif action == 'tl':
            axis = (ball_x - x1, ball_y - y1) 
        elif action == 'tr':
            axis = (ball_x - x2, ball_y - y1) 
        elif action == 'br':
            axis = (ball_x - x2, ball_y - y2)
        elif action == 'bl':
            axis = (ball_x - x1, ball_y - y2)
        
        ball.pos = (ball_x - ball.v[0], ball_y - ball.v[1])
        ball.v = reflect(ball.v, axis)
        
        
    elif collided == False and active == False:
        ball.collided.remove(block_id)