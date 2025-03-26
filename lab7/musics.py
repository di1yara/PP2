import pygame
import os

pygame.init()

#музыкаларды тізімін алу
playlist = []
playlist_path = 'C:/Users/HUAWEI/PycharmProjects/Python1/lab7/playlist'
music_list = os.listdir(playlist_path)

for song in music_list:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(playlist_path, song))

# Экран параметрлері
screen = pygame.display.set_mode((736, 920))
pygame.display.set_caption("Күйлер")
Clock = pygame.time.Clock()

# Фон
fon = pygame.image.load('C:/Users/HUAWEI/PycharmProjects/Python1/lab7/music buttons/qazgirlbg.jpg')
fon = pygame.transform.scale(fon, (736, 920))

# Басқару панелі
bf = pygame.Surface((480,200,))
bf.set_alpha(180)  # Жартылай мөлдір ету
bf.fill((255, 255, 255))

# Шрифт параметрлері
font = pygame.font.SysFont(None, 20)

# Батырма суреттері
play_b = pygame.image.load('C:/Users/HUAWEI/PycharmProjects/Python1/lab7/music buttons/play.png')
pause_b = pygame.image.load('C:/Users/HUAWEI/PycharmProjects/Python1/lab7/music buttons/pause.png')
next_b = pygame.image.load('C:/Users/HUAWEI/PycharmProjects/Python1/lab7/music buttons/next.png')
prev_b = pygame.image.load('C:/Users/HUAWEI/PycharmProjects/Python1/lab7/music buttons/back.png')


aplay = True
running = True
index=0
clock = pygame.time.Clock()

#баста ойын циклі
while running:
    screen.blit(fon, (0, 0))  # Фонды орналастыру
    screen.blit(bf, (130, 480))  # Басқару панелін орналастыру

    # Ән атауын экранға шығару
    song_name = os.path.basename(playlist[index])
    text2 = font.render(song_name, True, (0, 0, 0))
    text_rect = text2.get_rect(center=(screen.get_width() // 2, 520))
    screen.blit(text2, text_rect)

    # Батырмалардың орындары
    playb = pygame.transform.scale(play_b, (70, 70))
    pausb = pygame.transform.scale(pause_b, (70, 70))
    nextb = pygame.transform.scale(next_b, (70, 70))
    prevb = pygame.transform.scale(prev_b, (75, 75))

    # Батырмаларды экранға шығару
    play_rect = screen.blit(playb, (370, 590))
    pause_rect = screen.blit(pausb, (370, 590))
    next_rect = screen.blit(nextb, (460, 587))
    prev_rect = screen.blit(prevb, (273, 585))

    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

        # Пернетақта басқаруы
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    pygame.mixer.music.pause()
                    play_pause_icon = play_b
                else:
                    pygame.mixer.music.unpause()
                    play_pause_icon = pause_b
                aplay = not aplay

            elif event.key == pygame.K_RIGHT:  # Келесі ән
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                play_pause_icon = pause_b
                aplay = True

            elif event.key == pygame.K_LEFT:  # Алдыңғы ән
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                play_pause_icon = pause_b
                aplay = True

        # Мышкамен басқару
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_rect.collidepoint(mouse_pos):
                if aplay:
                    pygame.mixer.music.pause()
                    play_pause_icon = play_b
                else:
                    pygame.mixer.music.unpause()
                    play_pause_icon = pause_b
                aplay = not aplay

            elif next_rect.collidepoint(mouse_pos):  # Келесі ән
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                play_pause_icon = pause_b
                aplay = True

            elif prev_rect.collidepoint(mouse_pos):  # Алдыңғы ән
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                play_pause_icon = pause_b
                aplay = True

    # Егер музыка аяқталса, автоматты түрде келесіге өту
    if not pygame.mixer.music.get_busy():
        index = (index + 1) % len(playlist)
        pygame.mixer.music.load(playlist[index])
        pygame.mixer.music.play()
        play_pause_icon = pause_b
        aplay = True

    clock.tick(24)