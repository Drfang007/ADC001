import pygame
class Ship:
	"""管理飞船的类"""


	
	def __init__ (self,ai_game):
		"""初始化飞船并初始其位置"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		"""加载飞船图像并获取其外形矩形"""
		self.image = pygame.image.load('image/ship.bmp')
		self.rect = self.image.get_rect()

		"""对于每艘新飞船，都将重置在屏幕底部"""
		self.rect.midbottom = self.screen_rect.midbottom
		#移动标志
		self.moving_right = False
		self.moving_left = False
		self.x =float(self.rect.x)

	def blitme(self):
		"""在指定区域绘制飞船"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left >0:
			self.x -= self.settings.ship_speed
		self.rect.x = self.x
