import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 初始化设置类
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen)
    # 开始游戏主循环
    while True:
        # 监视鼠标和键盘事件
        gf.check_event(ship)
        # 更新飞船位置
        ship.update()
        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship)

run_game()