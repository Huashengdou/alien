import sys
import pygame
from bullet import Bullet

def fire_bullet(ai_settings, screen, ship, bullets):
    """发射子弹函数"""
    if len(bullets) < ai_settings.bullets_allowed:
        # 创建子弹，并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keydown_event(event, ai_settings, screen, ship, bullets):
    """相应按键按下"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()

def check_keyup_event(event, ship):
    """相应按键松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_event(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

def update_bullets(bullets):
    """更新子弹位置，并删除已经消失的子弹"""
    # 更新子弹位置
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(ai_settings, screen, ship, alien, bullets):
    """更新屏幕图像，并切换到新屏幕"""
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 绘制飞船
    ship.blitme()
    # 绘制外星人
    alien.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()