import pygame
import sys
import random

# Pygameの初期化
pygame.init()

# 画面のサイズと色
WIDTH, HEIGHT = 600, 400
BG_COLOR = (0, 0, 0)
GRID_SIZE = 20

# 色の定義
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 方向の定義
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# 蛇のクラス
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = WHITE

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % WIDTH), (cur[1] + (y * GRID_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], GRID_SIZE, GRID_SIZE))

# 食べ物のクラス
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                         random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

# ゲームの初期化
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

snake = Snake()
food = Food()

# ゲームループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    for key in keys:
        if keys[pygame.K_UP]:
            snake.direction = UP
        elif keys[pygame.K_DOWN]:
            snake.direction = DOWN
        elif keys[pygame.K_LEFT]:
            snake.direction = LEFT
        elif keys[pygame.K_RIGHT]:
            snake.direction = RIGHT

    snake.update()

    # 蛇が食べ物を食べたかどうかの判定
    if snake.get_head_position() == food.position:
        snake.length += 1
        food.randomize_position()

    # 画面の描画
    screen.fill(BG_COLOR)
    snake.render(screen)
    food.render(screen)
    pygame.display.flip()

    # フレームレートの制御
    pygame.time.Clock().tick(10)