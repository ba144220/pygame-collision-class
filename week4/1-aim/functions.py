import numpy as np

def reflect(a, b):
    print(f"reflect {b}")
    p = np.array(b) * (np.dot(a, b) / np.dot(b, b))
    return a - 2*p

def collision(ball, block):
    block_hw = block.rect.width / 2
    block_hh = block.rect.height / 2
    ball_radius = ball.rect.width / 2

    ball_v = ball.v
    ball_rect_center = np.array(ball.rect.center)

    u = ball_rect_center - block.rect.center
    u_abs = np.abs(u)
    u_sign = np.sign(u)
    
    if (u_abs <= (block_hw, block_hh)).any():
        (dir_x, dir_y) = (u_abs <= (block_hw + ball_radius, block_hh + ball_radius)) & np.flip(u_abs <= (block_hw, block_hh))
        if dir_x:
            ball.rect.center = np.around(ball_rect_center - ball_v)
            ball.v = reflect(ball_v, (1,0))
            return
        elif dir_y:
            ball.rect.center = np.around(ball_rect_center - ball_v)
            ball.v = reflect(ball_v, (0,1))
            return

    dist = np.linalg.norm(u_abs - (block_hw, block_hh))

    if dist <= ball_radius:
        ball.rect.center = np.around(ball_rect_center - ball_v)
        if np.dot(ball_v * u_sign, (1, 1)) < 0:
            ball.v = reflect(ball_v, u_sign)
        elif np.dot(ball_v * u_sign, (1, 0)) < 0:
            ball.v = reflect(ball_v, (1, 0))
        else:
            ball.v = reflect(ball_v, (0, 1))
        return