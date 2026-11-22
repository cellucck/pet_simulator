
import pygame
import random


class TreatCatcher:

    WIDTH = 650
    HEIGHT = 640

    def __init__(self):
        self.reset()

    def reset(self):

        # Basket position
        self.player_x = self.WIDTH // 2
        self.player_y = 535
        self.player_speed = 7

        self.catch_width = 130
        self.catch_height = 35

        # Falling bones
        self.bones = []
        self.bone_speed = 2
        self.spawn_timer = 0
        self.spawn_delay = 65

        # Game information
        self.score = 0
        self.lives = 3
        self.missed_bones = 0
        self.max_misses = 8

        self.completed = False
        self.reward_claimed = False

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r and self.completed:
                self.reset()

    def update(self, keys=None):

        if self.completed:
            return

        if keys is None:
            keys = pygame.key.get_pressed()

        # Move basket
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player_x -= self.player_speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player_x += self.player_speed

        # Keep basket inside screen
        half_width = self.catch_width // 2

        self.player_x = max(
            half_width,
            min(self.WIDTH - half_width, self.player_x)
        )

        # Spawn bones
        self.spawn_timer += 1

        if self.spawn_timer >= self.spawn_delay:

            bone_x = random.randint(10, self.WIDTH - 45)

            self.bones.append(
                pygame.Rect(bone_x, -30, 35, 20)
            )

            self.spawn_timer = 0

        # Basket collision area
        basket_rect = pygame.Rect(
            self.player_x - half_width,
            self.player_y,
            self.catch_width,
            self.catch_height
        )

        # Move bones and check collisions
        for bone in self.bones[:]:

            bone.y += self.bone_speed

            if bone.colliderect(basket_rect):

                self.bones.remove(bone)
                self.score += 1

                # Gradually increase difficulty
                if self.score % 10 == 0:

                    self.bone_speed += 0.3

                    self.spawn_delay = max(
                        35,
                        self.spawn_delay - 3
                    )

            elif bone.top > self.HEIGHT:

                self.bones.remove(bone)
                self.missed_bones += 1

                # Lose a life every 3 missed bones
                if self.missed_bones % 3 == 0:
                    self.lives -= 1

        # Game ends after 8 missed bones
        if self.missed_bones >= self.max_misses:
            self.completed = True

    def draw_bone(self, surface, bone):

        bone_color = (255, 255, 245)

        # Bone middle
        pygame.draw.line(
            surface,
            bone_color,
            (bone.x + 7, bone.y + 10),
            (bone.x + 28, bone.y + 10),
            7
        )

        # Bone ends
        for x in (bone.x + 7, bone.x + 28):

            pygame.draw.circle(
                surface,
                bone_color,
                (x, bone.y + 5),
                6
            )

            pygame.draw.circle(
                surface,
                bone_color,
                (x, bone.y + 15),
                6
            )

    def draw_basket(self, surface):

        basket_x = self.player_x - self.catch_width // 2
        basket_y = self.player_y

        basket_rect = pygame.Rect(
            basket_x,
            basket_y,
            self.catch_width,
            self.catch_height
        )

        # Basket body
        pygame.draw.rect(
            surface,
            (110, 157, 158),
            basket_rect,
            border_radius=10
        )

        # Basket outline
        pygame.draw.rect(
            surface,
            (45, 75, 75),
            basket_rect,
            3,
            border_radius=10
        )

        # Basket top edge
        pygame.draw.line(
            surface,
            (255, 245, 225),
            (basket_x + 5, basket_y + 5),
            (basket_x + self.catch_width - 5, basket_y + 5),
            4
        )

        # Decorative basket lines
        for x in range(basket_x + 25, basket_x + self.catch_width, 30):

            pygame.draw.line(
                surface,
                (160, 195, 190),
                (x, basket_y + 12),
                (x, basket_y + 28),
                2
            )

    def draw(self, surface, font, points):

        # Background
        surface.fill((190, 224, 226))

        instruction_font = pygame.font.SysFont(
            "Comic Sans MS", 18
        )

        small_font = pygame.font.SysFont(
            "Comic Sans MS", 16
        )

        # Title
        title = font.render(
            "Bone Catcher!",
            True,
            (45, 75, 75)
        )

        surface.blit(title, (37, 25))

        # Instructions
        instructions = instruction_font.render(
            "Use LEFT and RIGHT arrows to catch the bones!",
            True,
            (45, 75, 75)
        )

        surface.blit(instructions, (37, 67))

        # Score
        score_text = font.render(
            f"Bones: {self.score}",
            True,
            (45, 75, 75)
        )

        surface.blit(score_text, (440, 25))

        # Lives
        lives_text = instruction_font.render(
            f"Lives: {self.lives}",
            True,
            (45, 75, 75)
        )

        surface.blit(lives_text, (440, 65))

        # Missed bones
        missed_text = small_font.render(
            f"Missed: {self.missed_bones}/{self.max_misses}",
            True,
            (45, 75, 75)
        )

        surface.blit(missed_text, (37, 105))

        # Draw falling bones
        for bone in self.bones:
            self.draw_bone(surface, bone)

        # Draw visible basket
        self.draw_basket(surface)

        # Game over screen
        if self.completed:

            message = font.render(
                "Game Over!",
                True,
                (180, 75, 75)
            )

            final_score = instruction_font.render(
                f"You caught {self.score} bones!",
                True,
                (45, 75, 75)
            )

            restart = instruction_font.render(
                "Press R to play again!",
                True,
                (45, 75, 75)
            )

            surface.blit(
                message,
                message.get_rect(center=(325, 270))
            )

            surface.blit(
                final_score,
                final_score.get_rect(center=(325, 320))
            )

            surface.blit(
                restart,
                restart.get_rect(center=(325, 355))
            )


# Run independently for testing
if __name__ == "__main__":

    pygame.init()

    screen = pygame.display.set_mode((650, 640))

    pygame.display.set_caption("Bone Catcher")

    font = pygame.font.SysFont(
        "Comic Sans MS", 28
    )

    game = TreatCatcher()

    clock = pygame.time.Clock()
    running = True

    while running:

        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            game.handle_event(event)

        game.update()
        game.draw(screen, font, game.score)

        pygame.display.flip()

    pygame.quit()
