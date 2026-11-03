import pygame


class MazeGame:

    GRID = [
        "111111111111",
        "100000000001",
        "101111011101",
        "100001000001",
        "111101110101",
        "100000010001",
        "101110010101",
        "100010000001",
        "101011110101",
        "111111111111",
    ]

    CELL_SIZE = 48
    LEFT = 37
    TOP = 125

    START = (1, 1)
    EXIT = (10, 8)

    def __init__(self):
        self.player_pos = self.START
        self.completed = False
        self.reward_claimed = False

    def reset(self):
        self.player_pos = self.START
        self.completed = False
        self.reward_claimed = False

    def move(self, dx, dy):

        if self.completed:
            return

        x, y = self.player_pos

        new_x = x + dx
        new_y = y + dy

        # Check that the player stays inside the maze
        if (
            0 <= new_y < len(self.GRID)
            and 0 <= new_x < len(self.GRID[0])
            and self.GRID[new_y][new_x] == "0"
        ):

            self.player_pos = (new_x, new_y)

            # Check if the player reached the exit
            if self.player_pos == self.EXIT:
                self.completed = True

    def draw(self, surface, font, points):

        surface.fill((190, 224, 226))

        # Game title
        title = font.render(
            "Walk Your Pet!",
            True,
            (45, 75, 75)
        )

        surface.blit(title, (37, 25))

        # Instructions
        instruction_font = pygame.font.SysFont(
            "Comic Sans", 18
        )

        instructions = instruction_font.render(
            "Use arrow keys to find the exit. Press ESC to go home.",
            True,
            (45, 75, 75)
        )

        surface.blit(instructions, (37, 67))

        # Draw the maze
        for row_index, row in enumerate(self.GRID):

            for col_index, cell in enumerate(row):

                rect = pygame.Rect(
                    self.LEFT + col_index * self.CELL_SIZE,
                    self.TOP + row_index * self.CELL_SIZE,
                    self.CELL_SIZE,
                    self.CELL_SIZE
                )

                if cell == "1":
                    color = (82, 112, 91)
                else:
                    color = (239, 239, 215)

                pygame.draw.rect(
                    surface,
                    color,
                    rect
                )

                pygame.draw.rect(
                    surface,
                    (160, 185, 175),
                    rect,
                    1
                )

        # Draw the exit
        exit_rect = pygame.Rect(
            self.LEFT + self.EXIT[0] * self.CELL_SIZE + 8,
            self.TOP + self.EXIT[1] * self.CELL_SIZE + 8,
            self.CELL_SIZE - 16,
            self.CELL_SIZE - 16
        )

        pygame.draw.rect(
            surface,
            (238, 184, 90),
            exit_rect,
            border_radius=8
        )

        # Draw the player
        px, py = self.player_pos

        center = (
            self.LEFT + px * self.CELL_SIZE + self.CELL_SIZE // 2,
            self.TOP + py * self.CELL_SIZE + self.CELL_SIZE // 2
        )

        pygame.draw.circle(
            surface,
            (215, 111, 104),
            center,
            15
        )

        pygame.draw.circle(
            surface,
            (255, 245, 225),
            center,
            15,
            2
        )

        # Display points
        points_text = font.render(
            f"Points: {points}",
            True,
            (45, 75, 75)
        )

        surface.blit(points_text, (485, 25))

        # Victory message
        if self.completed:

            message = instruction_font.render(
                "You found the way home!",
                True,
                (45, 105, 65)
            )

            surface.blit(
                message,
                message.get_rect(center=(325, 600))
            )