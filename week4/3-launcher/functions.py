import numpy as np

def reflect(a, b):
    p = np.array(b) * (np.dot(a, b) / np.dot(b, b))
    return a - 2*p

def collision(ball, block):
    block_hw = block.rect.width / 2
    block_hh = block.rect.height / 2
    ball_radius = ball.rect.width / 2

    v = np.array(ball.rect.center) - np.array(block.rect.center)
    v_abs = np.abs(v)

    if (v_abs <= (block_hw, block_hh)).any():
        (dir_x, dir_y) = (v_abs <= (block_hw + ball_radius, block_hh + ball_radius)) & np.flip(v_abs <= (block_hw, block_hh))
        if dir_x:
            print("reflect x")
            ball.v = reflect(ball.v, (1,0))
            return
        elif dir_y:
            print("reflect y")
            ball.v = reflect(ball.v, (0,1))
            return
            
    dist = np.linalg.norm(v_abs - (block_hw, block_hh))

    if dist <= ball_radius:
        if np.prod(v) > 0:
            print("reflect (1, 1)")
            ball.v = reflect(ball.v, (1,1))
        else:
            print("reflect (1, -1)")
            ball.v = reflect(ball.v, (1,-1))