from vector_operations import *
def ball_block_detect(ball, block):
    ball_x, ball_y = ball.pos
    block_x, block_y = block.rect.center
    r = ball.r
    x1 = block.x1
    x2 = block.x2
    y1 = block.y1
    y2 = block.y2
    x0 = x1 - r
    x3 = x2 + r
    y0 = y1 - r
    y3 = y2 + r

    if ball_x < x0 or ball_x > x3 or ball_y < y0 or ball_y > y3:
        return


    if ball_x >= x1 and ball_x <= x2:
        if ball_y >= y0 and ball_y <= y1:
            print('block top')
            ball.v = reflect(ball.v, (0,-1))
            ball.collided.append(block.id)
            return
        elif ball_y <= y3 and ball_y >= y2:
            print('block bottom')
            ball.v = reflect(ball.v, (0,1))
            ball.collided.append(block.id)
            return
    
    elif ball_y >= y1 and ball_y <= y2:
        if ball_x >= x0 and ball_x <= x1:
            print('block left')
            ball.v = reflect(ball.v, (-1,0))
            ball.collided.append(block.id)
            return
        elif ball_x <= x3 and ball_x >= x2:
            print('block right')
            ball.v = reflect(ball.v, (1,0))
            ball.collided.append(block.id)
            return

    if distance(ball.pos, (x1, y1)) <= r:
        print('block top left')  
        axis = (ball_x - x1, ball_y - y1) 
        ball.v = reflect(ball.v, axis)
        ball.collided.append(block.id)
        return
    elif distance(ball.pos, (x2, y1)) <= r:
        print('block top right')  
        axis = (ball_x - x2, ball_y - y1) 
        ball.v = reflect(ball.v, axis)
        ball.collided.append(block.id)
        return
    elif distance(ball.pos, (x2, y2)) <= r:
        print('block bottom right')  
        axis = (ball_x - x2, ball_y - y2) 
        ball.v = reflect(ball.v, axis)
        ball.collided.append(block.id)
        return
    elif distance(ball.pos, (x1, y2)) <= r:
        print('block bottom left')  
        axis = (ball_x - x1, ball_y - y2) 
        ball.v = reflect(ball.v, axis)
        ball.collided.append(block.id)
        return
    
    