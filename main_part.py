import sys
import pygame

from pygame.rect import Rect


pygame.init()

'Задаём размеры экрана'

width = 1000
height = 600

'Параметры игры'

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('VOLLEYBALL')
clock = pygame.time.Clock()

'Описываем класс операций с векторами'

class Vector:

    def __init__(self, x , y ):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, f):
        return Vector(self.x * f, self.y * f)

    def __rmul__(self, f):
        return Vector(f * self.x, f * self.y )

    def __neg__(self):
        return Vector(-1 * self.x, -1 * self.y )

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def intpair(self):
        return (int(self.x), int(self.y))


'Описываем класс шариков'

class Ball:

    def __init__(self, x, y, vx, vy):
    
        self.vcoord = Vector(x, y)
        self.vspeed = Vector(vx, vy)

    def render_ball(self, canvas):
    
        pygame.draw.circle(canvas, (40, 113, 62), ball.vcoord.intpair(), 30)

    def update_ball(self, dt):

        def hit(self, dt):
        
            for player in [player1, player2]:
                if ((ball.vcoord.x - player.vcoord.x) ** 2 + (ball.vcoord.y - player.vcoord.y) ** 2) <= 110 ** 2:
                    ball.vspeed += 0.5 * player.vspeed
                else:
                    ball.vspeed.y -= 0.005 * ball.vspeed.y
                    ball.vcoord.y = ball.vcoord.y + ball.vspeed.y * dt - 0.1 * dt * dt / 2
                    ball.vcoord.x = ball.vcoord.x + ball.vspeed.x * dt

        def point(self):
        
            if ball.vcoord.y > 520:
                player1.vcoord.x = 300
                player1.vcoord.y = 520
                player2.vcoord.x = 700
                player2.vcoord.y = 520
            if ball.vcoord.x > 500:
                ball.vcoord.x = 700
                ball.vcoord.y = 300
                player1.vscore += 1
            if ball.vcoord.x < 500:
                ball.vcoord.x = 300
                ball.vcoord.y = 300
                player2.vscore += 1

        def check_bounds_ball(self):
        
            def intersect(obj, ball):
                edges = dict(
                    left=Rect(obj.left, obj.top, 1, obj.height),
                    right=Rect(obj.right, obj.top, 1, obj.height),
                    top=Rect(obj.left, obj.top, obj.width, 1),
                    bottom=Rect(obj.left, obj.bottom, obj.width, 1))
                collisions = set(edge for edge, rect in edges.items() if
                             ball.bounds.colliderect(rect))
                if not collisions:
                    return None

                if len(collisions) == 1:
                    return list(collisions)[0]

                if 'top' in collisions:
                    if ball.centery >= obj.top:
                        return 'top'
                    if ball.centerx < obj.left:
                        return 'left'
                    else:
                        return 'right'

                if 'bottom' in collisions:
                    if ball.centery >= obj.bottom:
                        return 'bottom'
                    if ball.centerx < obj.left:
                        return 'left'
                    else:
                        return 'right'

        # Удар об потолок

                if self.ball.top < 0:
                    ball.vspeed.y = -1 * ball.vspeed.y

        # Удар об стену

                if self.ball.left < 0 or self.ball.right > 1000:
                    ball.vspeed.x = -1 * ball.vspeed.x

        self.vcoord += self.vspeed * dt

class Player:

    def __init__(self, x, y, vx, vy, score):
        self.vcoord = Vector(x, y)
        self.vspeed = Vector(vx, vy)
        self.state = 10000
        self.vscore = 0
        self.onGround = False

    def render_players(self, canvas):
    
        pygame.draw.circle(canvas, (150, 10, 50), player1.vcoord.intpair(), 80)
        pygame.draw.circle(canvas, (150, 100, 200), player2.vcoord.intpair(), 80)

    def update_players(self):

        GROUND = 10000
        AIR1 = 10001
        AIR2 = 10002

        left = False
        right = False
        up = False

        MOVE_SPEED = 0.6
        GRAVITY = 0.4
        JUMP_POWER = 12
        LIMIT_SPEED = 40


        if left:

            # Изменение self.xvel для более быстрого набора скорости.
            if player1.vspeed.x == 0:
                player1.vspeed.x = -5

            # Основное изменение скорости.
                player1.vspeed.x -= MOVE_SPEED

            # Создание лимитирующей скорости (иначе при большом разгоне герой может вылететь за пределы уровня).
            if abs(player1.vspeed.x) > LIMIT_SPEED:
                player1.vspeed.x += MOVE_SPEED
            # Ослабление движения по инерции.
            if player1.vspeed.x > 15:
                player1.vspeed.x = 15

        if right:
            if player1.vspeed.x == 0:
                player1.vspeed.x = 5
                player1.vspeed.x += MOVE_SPEED
            if abs(player1.vspeed.x) > LIMIT_SPEED:
                player1.vspeed.x -= MOVE_SPEED
            if player1.vspeed.x < -15:
                player1.vspeed.x = -15


        # Контролируемое ликвидирование инерции.
        if not (left or right):
            player1.vspeed.x = 0

        # Выполнение прыжка.
        if up:
            if player1.onGround:
                player1.vspeed.y = -JUMP_POWER

        #ПРОПИСЫВАЮ ДВИЖЕНИЕ ОДНОГО ИЗ ИГРОКОВ, НО ПОЧЕМУ-ТО ВЫПОЛНЯЕТСЯ ТОЛЬКО ДВИЖЕНИЕ ВЛЕВО

        if pygame.key.get_pressed()[pygame.K_d] and player2.vcoord.x < 920:
            player2.vspeed.x += 100
        else:
            player2.vspeed.x = 0
        if pygame.key.get_pressed()[pygame.K_a] and player2.vcoord.x > 600:
            player2.vspeed.x -= 100
        else:
            player2.vspeed.x = 0

        if pygame.key.get_pressed()[pygame.K_w] and player2.vcoord.y >= 520:
            if player2.state == GROUND:
                player2.state = AIR1
                player2.vspeed.y -= 100
            else:
                player2.vspeed.y += 100
            if player2.state == AIR1:
                player2.state = AIR2
                player2.vspeed.y -= 2
            else:
                player2.vspeed.y += 100

        self.vcoord += self.vspeed * dt

'Создаём шарики'

player1 = Player(300, 520, 0, 0, 0)
player2 = Player(700, 520, 0, 0, 0)
ball = Ball(300, 100, 0, 0)

while True:
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    'Рисуем игроков, поле и мяч'
    screen.fill((216, 186, 11))
    pygame.draw.line(screen, (0, 0, 0), (500,600), (500,300), 30)
    ball.update_ball(dt)
    ball.render_ball(screen)
    for player in [player1, player2]:
        player.update_players()
        player.render_players(screen)
    for e in pygame.event.get():

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                left = True
            if e.key == pygame.K_RIGHT:
                right = True
            if e.key == pygame.K_UP:
                up = True

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_RIGHT:
                right = False
            if e.key == pygame.K_UP:
                up = False

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(format(player1.vscore), False, (0, 0, 0))
    screen.blit(textsurface, (30, 30))
    textsurface = myfont.render(format(player2.vscore), False, (0, 0, 0))
    screen.blit(textsurface, (970, 30))

    pygame.display.flip()
