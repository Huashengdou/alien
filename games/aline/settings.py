
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
        # self.ship_speed_factor = 1.5
        # 总的飞船数量
        self.ship_limit = 3

        # 子弹的设置
        # self.bullet_speed_factor = 3
        self.bullet_width = 1200
        self.bullet_height = 15
        self.bullet_color = 0,0,255#60, 60, 60
        self.bullets_allowed = 3
        # 连续发射子弹标志
        # self.continue_fire = False

        # 外星人设置
        # self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示右移，为-1表示左移
        # self.fleet_direction = 1

        # 提升游戏难度
        self.speedup_scale = 1.1
        # 击落外星人时分数提高的速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
