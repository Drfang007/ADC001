import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
	"""管理游戏资源和行为的类"""
	def __init__(self):
		"""初始化游戏并创建资源"""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")
		
		self.ship =Ship(self)
		self.bullets = pygame.sprite.Group()

		

	def _check_enents(self):
		# 监视键盘和鼠标事件。
		for event in pygame.event.get():
			if event.type ==pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
				
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
				
				

	def _check_keydown_events(self,event):
		"""按键响应"""
		if event.key == pygame.K_RIGHT:
			#向右移动飞船
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			#向左移动飞船
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self,event):
		"""按键松开"""
		if event.key == pygame.K_RIGHT:
			#取消向右移动飞船
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			#取消向左移动飞船
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""创建一颗子弹并发射出去"""
		if len(self.bullets)< self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
	def _update_bullets(self):
		self.bullets.update()
		#删除消失的子弹
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
				print(len(self.bullets))			

	def _update_screen(self):
		self.bg_color = (self.settings.bg_color)
		self.screen.fill(self.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		"""让最近绘制的屏幕可见"""
		pygame.display.flip()

	def run_game(self):
		"""开始游戏主循环"""
		while True:
			self._check_enents()
			self._update_screen()
			self.ship.update()
			self._update_bullets()
			

if __name__ == '__main__':
	#创建游戏实例并运行游戏。
	ai = AlienInvasion()
	ai.run_game()