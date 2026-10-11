import os
import math
import pygame
from .marble import Marble
from .wall import Wall

# Color Palette
WHITE = (255, 255, 255)
DARK = (30, 30, 42)
WALL_COLOR = (95, 95, 120)
GOAL_COLOR = (60, 210, 120)
GOAL_RING = (40, 160, 90)
OVERLAY_BG = (18, 18, 28, 220)
TEXT_MUTED = (180, 185, 205)

# Difficulty Configurations (Task 3)
DIFFICULTY_CONFIGS = {
    "Easy": {
        "tilt_strength": 0.80,
        "friction": 0.035,
        "time_limit_ms": 60000,
        "max_speed": 8.0,
        "color": (60, 200, 120),
        "desc": "Easy (60s | High Grip)"
    },
    "Medium": {
        "tilt_strength": 0.60,
        "friction": 0.020,
        "time_limit_ms": 45000,
        "max_speed": 9.0,
        "color": (245, 180, 50),
        "desc": "Medium (45s | Balanced)"
    },
    "Hard": {
        "tilt_strength": 0.45,
        "friction": 0.012,
        "time_limit_ms": 30000,
        "max_speed": 11.0,
        "color": (240, 75, 75),
        "desc": "Hard (30s | Slippery Fast)"
    }
}


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.running = True

        # State management
        self.current_difficulty = "Medium"
        self._apply_difficulty(self.current_difficulty)

        self.marble = Marble(50, 50)
        self.walls = self._build_maze()
        self.goal_x, self.goal_y, self.goal_radius = width - 60, height - 60, 22

        self.start_ticks = pygame.time.get_ticks()
        self.game_over = False
        self.result = None  # "solved" or "timeout"
        self.finish_time_ms = None

        # Fonts (robust fallback)
        self._init_fonts()

        # Task 4: Sound initialization
        self._init_sounds()
        self._last_bounce_sound_time = 0

        # UI interactive buttons for Task 3 replay
        self.buttons = {
            "Easy": pygame.Rect(70, 295, 140, 42),
            "Medium": pygame.Rect(230, 295, 140, 42),
            "Hard": pygame.Rect(390, 295, 140, 42),
            "Quit": pygame.Rect(230, 355, 140, 36)
        }

    def _init_fonts(self):
        try:
            self.font = pygame.font.SysFont("Arial", 24)
            self.large_font = pygame.font.SysFont("Arial", 38, bold=True)
            self.title_font = pygame.font.SysFont("Arial", 46, bold=True)
            self.small_font = pygame.font.SysFont("Arial", 16)
        except Exception:
            self.font = pygame.font.Font(None, 24)
            self.large_font = pygame.font.Font(None, 38)
            self.title_font = pygame.font.Font(None, 46)
            self.small_font = pygame.font.Font(None, 16)

    def _init_sounds(self):
        self.sounds = {}
        sound_dir = os.path.join(os.path.dirname(__file__), "sounds")
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
            for sound_name in ["bounce", "goal", "timeout"]:
                sound_path = os.path.join(sound_dir, f"{sound_name}.wav")
                if os.path.exists(sound_path):
                    self.sounds[sound_name] = pygame.mixer.Sound(sound_path)
        except Exception as e:
            print(f"[Sound System] Audio mixer initialized in silent mode: {e}")

    def play_sound(self, name):
        """Plays loaded procedural sound effect with debouncing."""
        if name in self.sounds:
            try:
                now = pygame.time.get_ticks()
                if name == "bounce":
                    if now - self._last_bounce_sound_time < 90:
                        return
                    self._last_bounce_sound_time = now
                self.sounds[name].play()
            except Exception:
                pass

    def _apply_difficulty(self, diff_name):
        cfg = DIFFICULTY_CONFIGS.get(diff_name, DIFFICULTY_CONFIGS["Medium"])
        self.current_difficulty = diff_name
        self.tilt_strength = cfg["tilt_strength"]
        self.friction = cfg["friction"]
        self.time_limit_ms = cfg["time_limit_ms"]
        self.max_speed = cfg["max_speed"]

    def _build_maze(self):
        walls = []
        t = 16  # wall thickness

        # outer boundary
        walls.append(Wall(0, 0, self.width, t))
        walls.append(Wall(0, self.height - t, self.width, t))
        walls.append(Wall(0, 0, t, self.height))
        walls.append(Wall(self.width - t, 0, t, self.height))

        # Internal labyrinth partitions
        walls.append(Wall(0, 140, self.width - 140, t))
        walls.append(Wall(140, 260, self.width - 140, t))
        walls.append(Wall(0, 380, self.width - 140, t))

        return walls

    def restart(self, difficulty=None):
        """Task 3: Replay game with designated or current difficulty level."""
        if difficulty and difficulty in DIFFICULTY_CONFIGS:
            self._apply_difficulty(difficulty)

        self.marble = Marble(50, 50)
        self.start_ticks = pygame.time.get_ticks()
        self.game_over = False
        self.result = None
        self.finish_time_ms = None
        self._last_bounce_sound_time = 0

    def handle_event(self, event):
        """Handles keyboard and mouse clicks, including replay navigation (Task 3)."""
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_ESCAPE, pygame.K_q):
                self.running = False
            elif self.game_over:
                if event.key in (pygame.K_1, pygame.K_e):
                    self.restart("Easy")
                elif event.key in (pygame.K_2, pygame.K_m):
                    self.restart("Medium")
                elif event.key in (pygame.K_3, pygame.K_h):
                    self.restart("Hard")
                elif event.key in (pygame.K_r, pygame.K_SPACE, pygame.K_RETURN):
                    self.restart(self.current_difficulty)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.game_over:
                mouse_pos = event.pos
                if self.buttons["Easy"].collidepoint(mouse_pos):
                    self.restart("Easy")
                elif self.buttons["Medium"].collidepoint(mouse_pos):
                    self.restart("Medium")
                elif self.buttons["Hard"].collidepoint(mouse_pos):
                    self.restart("Hard")
                elif self.buttons["Quit"].collidepoint(mouse_pos):
                    self.running = False

    def handle_input(self):
        if self.game_over:
            return

        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.width // 2
        dy = mouse_y - self.height // 2
        dist = max(1.0, math.sqrt(dx * dx + dy * dy))
        ax = (dx / dist) * self.tilt_strength
        ay = (dy / dist) * self.tilt_strength
        self.marble.vx += ax
        self.marble.vy += ay

    def update(self):
        if self.game_over:
            return

        elapsed = pygame.time.get_ticks() - self.start_ticks
        if elapsed >= self.time_limit_ms:
            self.game_over = True
            self.result = "timeout"
            self.play_sound("timeout")
            return

        # Damping & Speed Cap
        self.marble.vx *= (1.0 - self.friction)
        self.marble.vy *= (1.0 - self.friction)

        speed = math.sqrt(self.marble.vx ** 2 + self.marble.vy ** 2)
        if speed > self.max_speed:
            scale = self.max_speed / speed
            self.marble.vx *= scale
            self.marble.vy *= scale

        self.marble.x += self.marble.vx
        self.marble.y += self.marble.vy

        # Task 1: Refined Collision Detection
        self._resolve_wall_collisions()

        # Goal check
        gx = self.goal_x - self.marble.x
        gy = self.goal_y - self.marble.y
        if math.sqrt(gx * gx + gy * gy) <= self.goal_radius:
            self.game_over = True
            self.result = "solved"
            self.finish_time_ms = elapsed
            self.play_sound("goal")

    def _resolve_wall_collisions(self):
        """
        Task 1: Precise Circle-vs-AABB Collision Detection & Physical Resolution.
        Replaces inaccurate rectangular bounding-box colliderect with true Euclidean
        clamped distance testing, completely eliminating phantom bounces near corners.
        """
        collision_occurred = False
        restitution = 0.35  # Elastic bounce coefficient

        for wall in self.walls:
            w_rect = wall.rect()

            # Find closest point on rectangle boundary to the marble circle center
            closest_x = max(w_rect.left, min(self.marble.x, w_rect.right))
            closest_y = max(w_rect.top, min(self.marble.y, w_rect.bottom))

            dx = self.marble.x - closest_x
            dy = self.marble.y - closest_y
            dist_sq = dx * dx + dy * dy

            # Collision only occurs when Euclidean distance is strictly less than marble radius
            if dist_sq < (self.marble.radius ** 2):
                collision_occurred = True

                if dist_sq > 0.0001:
                    distance = math.sqrt(dist_sq)
                    penetration = self.marble.radius - distance
                    normal_x = dx / distance
                    normal_y = dy / distance

                    # Displace marble position out of penetration along collision contact normal
                    self.marble.x += normal_x * penetration
                    self.marble.y += normal_y * penetration

                    # Reflect velocity vector along normal
                    v_dot_n = self.marble.vx * normal_x + self.marble.vy * normal_y
                    if v_dot_n < 0:
                        self.marble.vx -= (1.0 + restitution) * v_dot_n * normal_x
                        self.marble.vy -= (1.0 + restitution) * v_dot_n * normal_y
                else:
                    # Rare center penetration inside wall: eject along minimum overlap axis
                    overlap_l = self.marble.x + self.marble.radius - w_rect.left
                    overlap_r = w_rect.right - (self.marble.x - self.marble.radius)
                    overlap_t = self.marble.y + self.marble.radius - w_rect.top
                    overlap_b = w_rect.bottom - (self.marble.y - self.marble.radius)
                    min_o = min(overlap_l, overlap_r, overlap_t, overlap_b)

                    if min_o == overlap_l:
                        self.marble.x = w_rect.left - self.marble.radius
                        self.marble.vx = -abs(self.marble.vx) * restitution
                    elif min_o == overlap_r:
                        self.marble.x = w_rect.right + self.marble.radius
                        self.marble.vx = abs(self.marble.vx) * restitution
                    elif min_o == overlap_t:
                        self.marble.y = w_rect.top - self.marble.radius
                        self.marble.vy = -abs(self.marble.vy) * restitution
                    else:
                        self.marble.y = w_rect.bottom + self.marble.radius
                        self.marble.vy = abs(self.marble.vy) * restitution

        if collision_occurred:
            self.play_sound("bounce")

    def render(self, screen):
        # Draw background and maze
        screen.fill(DARK)

        # Draw walls
        for wall in self.walls:
            pygame.draw.rect(screen, WALL_COLOR, wall.rect())

        # Draw goal with concentric ring
        pygame.draw.circle(screen, GOAL_RING, (self.goal_x, self.goal_y), self.goal_radius + 4, width=3)
        pygame.draw.circle(screen, GOAL_COLOR, (self.goal_x, self.goal_y), self.goal_radius)

        # Draw marble with specular highlight
        mx, my = int(self.marble.x), int(self.marble.y)
        pygame.draw.circle(screen, WHITE, (mx, my), self.marble.radius)
        pygame.draw.circle(screen, (220, 220, 230), (mx, my), self.marble.radius, width=2)
        # Subtle light reflection spot
        pygame.draw.circle(screen, (255, 255, 255), (mx - 3, my - 3), 3)

        # HUD / Timer & Mode display
        elapsed = pygame.time.get_ticks() - self.start_ticks if not self.game_over else (self.finish_time_ms or self.time_limit_ms)
        seconds_left = max(0, int(math.ceil((self.time_limit_ms - elapsed) / 1000.0)))

        timer_color = (245, 90, 90) if seconds_left <= 5 else WHITE
        timer_text = self.font.render(f"⏱ Time: {seconds_left}s", True, timer_color)
        screen.blit(timer_text, (20, 20))

        diff_color = DIFFICULTY_CONFIGS[self.current_difficulty]["color"]
        mode_text = self.small_font.render(f"Difficulty: {self.current_difficulty}", True, diff_color)
        screen.blit(mode_text, (self.width - 150, 24))

        # Task 2 & Task 3: Render Game Over & Replay Screen
        if self.game_over:
            self._render_end_screen(screen)

    def _render_end_screen(self, screen):
        """Task 2 & 3: Render semi-transparent overlay modal with stats and difficulty selectors."""
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((15, 18, 30, 220))
        screen.blit(overlay, (0, 0))

        # Modal Card Box
        card_rect = pygame.Rect(50, 60, self.width - 100, self.height - 120)
        pygame.draw.rect(screen, (28, 32, 48), card_rect, border_radius=14)
        border_color = (60, 220, 130) if self.result == "solved" else (235, 75, 75)
        pygame.draw.rect(screen, border_color, card_rect, width=3, border_radius=14)

        if self.result == "solved":
            title = self.title_font.render("MAZE SOLVED!", True, (60, 220, 130))
            time_str = f"Finished in {self.finish_time_ms / 1000.0:.2f}s"
            sub = self.font.render(time_str, True, WHITE)
        else:
            title = self.title_font.render("TIME'S UP!", True, (240, 75, 75))
            sub = self.font.render("Maze not solved within time limit", True, TEXT_MUTED)

        screen.blit(title, (self.width // 2 - title.get_width() // 2, 85))
        screen.blit(sub, (self.width // 2 - sub.get_width() // 2, 145))

        prompt_text = self.font.render("Select Difficulty to Play Again:", True, (210, 215, 230))
        screen.blit(prompt_text, (self.width // 2 - prompt_text.get_width() // 2, 200))

        # Render Difficulty Buttons (Task 3)
        mouse_pos = pygame.mouse.get_pos()
        for diff_name, rect in [("Easy", self.buttons["Easy"]),
                                ("Medium", self.buttons["Medium"]),
                                ("Hard", self.buttons["Hard"])]:
            cfg = DIFFICULTY_CONFIGS[diff_name]
            is_hover = rect.collidepoint(mouse_pos)
            btn_bg = (45, 52, 75) if not is_hover else (60, 70, 100)
            pygame.draw.rect(screen, btn_bg, rect, border_radius=8)
            pygame.draw.rect(screen, cfg["color"], rect, width=2, border_radius=8)

            btn_label = self.font.render(diff_name, True, cfg["color"])
            screen.blit(btn_label, (rect.centerx - btn_label.get_width() // 2, rect.centery - btn_label.get_height() // 2 - 6))

            desc_label = self.small_font.render(f"{cfg['time_limit_ms'] // 1000}s", True, TEXT_MUTED)
            screen.blit(desc_label, (rect.centerx - desc_label.get_width() // 2, rect.centery + 7))

        # Quit Button
        quit_rect = self.buttons["Quit"]
        is_quit_hover = quit_rect.collidepoint(mouse_pos)
        pygame.draw.rect(screen, (35, 40, 58) if not is_quit_hover else (50, 55, 75), quit_rect, border_radius=8)
        pygame.draw.rect(screen, (130, 135, 155), quit_rect, width=1, border_radius=8)
        quit_label = self.font.render("Exit [ESC]", True, (190, 195, 210))
        screen.blit(quit_label, (quit_rect.centerx - quit_label.get_width() // 2, quit_rect.centery - quit_label.get_height() // 2))

        # Keyboard helper footer
        footer = self.small_font.render("Keyboard: Press [1] Easy  |  [2] Medium  |  [3] Hard  |  [R] Replay  |  [Q] Exit", True, (130, 135, 155))
        screen.blit(footer, (self.width // 2 - footer.get_width() // 2, card_rect.bottom - 24))
