import pygame
from bullet import Bullet
class Ship():
    """与飞船有关的属性"""
    def __init__(self, ai_settings, screen):
        """
        初始化飞船，并初始化其位置
        参数screen是整个游戏的窗口
        """
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像，并获取其外接矩形
        # load函数返回一个表示飞船的surface
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # 获取屏幕的外界矩形
        self.screen_rect = screen.get_rect()

        # 将飞船放在屏幕底部中央
        # centerx->水平居中的意思，rect的对象有center、centerx、centery
        # 还有top、bottom、left和right，还有更加直接的x和y
        # 注意：pygame的原点（0，0）在屏幕的左上角
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 将飞船的属性center中存储为小数
        self.center = float(self.rect.centerx)
        # 飞船是否移动的标志
        self.moving_right = False
        self.moving_left = False

    def update(self, ai_settings, screen, ship, bullets):
        """根据移动标志调制飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)