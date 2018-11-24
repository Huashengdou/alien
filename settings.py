
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