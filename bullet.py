import pygame
from pygame.sprite import Sprite

# Bullet继承了Sprite类，通过使用精灵，可将游戏中的相关元素编组，进而同时操作编组中的所有子弹
class Bullet(Sprite):
    """飞船发射子弹的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹"""
        super(Bullet, self).__init__()
        # super.__init__()
        self.screen = screen

        # 在（0,0）处创建一个表示子弹的矩形，再设置其正确的位置
        # 在（0，0）创建子弹
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        # 调整子弹位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储小数表示子弹的位置
        self.y = float(self.rect.y)

        # 设置子弹的颜色
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)