
class Settings():
    """存储外星人入侵的所有设置类"""
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800

        # 屏幕背景颜色设置
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        # 飞船移动速度的设置
        self.ship_speed_factor = 1.5

        # 子弹的设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0,0,255#60, 60, 60
        self.bullets_allowed = 3
        # 连续发射子弹标志
        # self.continue_fire = False

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = 1