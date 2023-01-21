import pygame, time, asyncio

#backend code
async def main():
    inventory = []
    for i in range (0, 8):
        inventory.append("")
    worldmap = [
        ["@", 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        ]
    x = worldmap[0].index("@")
    z = 0
#graphical interface
    pygame.init()
    screen = pygame.display.set_mode((400,500))
    _clock = pygame.time.Clock()
    _run = True
    _screenWidth = 400
    _screenHeight = 500
    _grass = (0, 255, 0)
    _player = (255, 255, 255)
    _cellSize = 32
    _img = pygame.image.load("game/player.png").convert_alpha()
    while _run:
        for event in pygame.event.get():
            _clock.tick(30)
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x-1, z-1, _screenWidth+1, _screenHeight+1))
            screen.blit(_img, (x*_cellSize, z*_cellSize))
            for i in range(len(worldmap)):
                for j in range(len(worldmap[i])):
                    if worldmap[i][j] == 1:
                        pygame.draw.rect(screen, _grass, pygame.Rect(j*_cellSize, i*_cellSize, _cellSize, _cellSize))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    z -= 1
                    worldmap[z+1][worldmap[z+1].index("@")] = 1
                    worldmap[z][x] = "@"
                if event.key == pygame.K_s:
                    z += 1
                    worldmap[z-1][worldmap[z-1].index("@")] = 1
                    worldmap[z][x] = "@"
                if event.key == pygame.K_a:
                    x -= 1
                    worldmap[z][x+1] = 1
                    worldmap[z][x] = "@"
                if event.key == pygame.K_d:
                    x += 1
                    worldmap[z][x-1] = 1
                    worldmap[z][x] = "@"
            if event.type == pygame.QUIT:
                _run = False
        pygame.display.flip()
        await asyncio.sleep(0)
asyncio.run(main())
