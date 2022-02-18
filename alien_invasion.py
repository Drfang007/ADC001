import sys
import pygame

class AlienInvasion:
	"""管理游戏资源和行为的类"""
	def __init__(self):
		"""初始化游戏并创建资源"""
		pygame.init()

		self.screen = pygame.display.set_mode((1200,800))
		pygame.display.set_caption("Alien Invasion")
		self.bg_color = (230, 230, 230)

	def run_game(self):
		"""开始游戏主循环"""
		while True:
			# 监视键盘和鼠标事件。
			for enent in pygame.enent.get():
				if enent.type ==pygame.QUIT:
					sys.exit()
			self.screen.fill(self.bg_color)

			"""让最近绘制的屏幕可见"""
			pygame.display.flip()

if __name__ == '__main__':
	#创建游戏实例并运行游戏。
	ai = AlienInvasion()
	ai.run_game()