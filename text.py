from cluedo import Cluedo

class Text:
    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos
        self.fontName = None
        self.fontSize = 64
        self.fontColor = Color('black')
        self.set_font()
        self.render()
    def set_font(self):
        self.font = pygame.font.Font(self.fontName, self.fontSize)
    def render(self):
        self.img = self.font.render(self.text, True, self.fontColor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
    def draw(self):
        Cluedo.screen.blit(self.img, self.rect)
