import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

cx, cy = WIDTH // 2, HEIGHT // 2

font = pygame.font.SysFont("Arial", 40)

NUM = 3000
targets = []

# 💖 OUTLINE
for i in range(NUM):
    t = (i / NUM) * 2 * math.pi
    x = 16 * math.sin(t)**3
    y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
    targets.append([cx + x * 15, cy + y * 15])

# 💥 FULL AREA TARGET
fill_targets = []
while len(fill_targets) < 6000:
    x = random.uniform(-18, 18)
    y = random.uniform(-18, 18)
    if (x**2 + y**2 - 1)**3 - x**2 * y**3 <= 0:
        fill_targets.append([cx + x * 20, cy - y * 20])

particles = []

index = 0
phase = "text"
hold_timer = 0
text_alpha = 80   # 🔥 mulai dari semi-visible (NO layar hitam)
text_timer = 0
burst_timer = 0

# sebelum loop
screen.fill((0, 0, 0))
text_surface = font.render("Hi Have a Great Day!", True, (255, 220, 220))
rect = text_surface.get_rect(center=(cx, cy))
screen.blit(text_surface, rect)
pygame.display.flip()

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ✨ TEXT (langsung keliatan + tetap fade in)
    if phase == "text":
        text_timer += 1

        if text_alpha < 255:
            text_alpha += 12  # 🔥 cepat tapi tetap smooth

        text_surface = font.render("Hi Have a Great Day!", True, (255, 220, 220))
        text_surface.set_alpha(min(text_alpha, 255))
        rect = text_surface.get_rect(center=(cx, cy))
        screen.blit(text_surface, rect)

        if text_timer > 60:
            phase = "text_fade"

    elif phase == "text_fade":
        text_alpha -= 10

        text_surface = font.render("Hi Have a Great Day!", True, (255, 220, 220))
        text_surface.set_alpha(max(text_alpha, 0))
        rect = text_surface.get_rect(center=(cx, cy))
        screen.blit(text_surface, rect)

        if text_alpha <= 0:
            phase = "draw"

    # 💖 OUTLINE
    elif phase == "draw":
        if index < NUM:
            tx, ty = targets[index]
            for _ in range(6):
                particles.append([
                    tx, ty,
                    random.uniform(-1, 1),
                    random.uniform(-1, 1),
                    tx, ty,
                    255
                ])
            index += 4
        else:
            phase = "cluster"

    # 💥 GUMPALAN
    elif phase == "cluster":
        burst_timer += 1

        for _ in range(50):
            particles.append([
                cx + random.uniform(-10, 10),
                cy + random.uniform(-10, 10),
                random.uniform(-1, 1),
                random.uniform(-1, 1),
                cx, cy,
                255
            ])

        if burst_timer > 30:
            phase = "burst"

    # 💣 FILL LOVE
    elif phase == "burst":
        for i in range(len(particles)):
            if i < len(fill_targets):
                tx, ty = fill_targets[i]
                particles[i][4] = tx
                particles[i][5] = ty

        phase = "hold"

    elif phase == "hold":
        hold_timer += 1
        if hold_timer > 80:
            phase = "explode"

    # 💥 EXPLODE
    elif phase == "explode":
        for p in particles:
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(3, 12)

            p[2] = math.cos(angle) * speed + random.uniform(-2, 2)
            p[3] = math.sin(angle) * speed + random.uniform(-2, 2)

        phase = "blast"

    # 🌪️ GERAK ACAK
    elif phase == "blast":
        for p in particles:
            p[0] += p[2]
            p[1] += p[3]

            p[0] += random.uniform(-1, 1)
            p[1] += random.uniform(-1, 1)

            p[6] -= 4

    if phase not in ["blast"]:
        for p in particles:
            x, y, vx, vy, tx, ty, alpha = p

            vx += (tx - x) * 0.004
            vy += (ty - y) * 0.004

            x += vx
            y += vy

            vx *= 0.88
            vy *= 0.88

            p[0], p[1], p[2], p[3] = x, y, vx, vy

    for p in particles:
        x, y, vx, vy, tx, ty, alpha = p
        if alpha > 0:
            pygame.draw.circle(screen, (255, 230, 220), (int(x), int(y)), 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()