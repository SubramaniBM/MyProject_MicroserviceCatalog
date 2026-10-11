# 🎮 Marble Tilt Maze — Lab 4 Vibe Coding Solutions

**Course:** Software Engineering Lab 4 (VibeCoding) — PES University  
**Student Name:** Subramani B M  
**SRN:** PES1UG24CS473  
**Section:** H  
**Assigned Repository:** [SETAPESU26/42_marble-tilt-maze](https://github.com/SETAPESU26/42_marble-tilt-maze)  
**Personal Fork Repository:** [SubramaniBM/42_marble-tilt-maze](https://github.com/SubramaniBM/42_marble-tilt-maze)  
**Master Lab Catalog:** [SubramaniBM/MyProject_MicroserviceCatalog](https://github.com/SubramaniBM/MyProject_MicroserviceCatalog)

---

## 🎯 Project Overview

This project is an interactive physics tilt-maze game built using **Pygame**. Players tilt the board by moving the mouse cursor relative to the screen center, guiding a rolling marble through a winding labyrinth to the goal zone before the countdown timer expires.

This repository contains the complete solutions for **Lab 4: Vibe Coding**, where an LLM pair-programming partner was leveraged iteratively to diagnose bugs, refine collision detection, construct rich graphical UI screens, engineer configurable difficulty levels, and synthesize procedural sound effects.

---

## 🚀 Getting Started

### 1. Requirements & Installation
- Python 3.10+ (tested on Python 3.11.16)
- Dependencies installed via pip:

```bash
pip install -r requirements.txt
```

### 2. Run the Game
```bash
python main.py
```

### 3. Controls
- **Mouse Movement:** Move cursor away from the screen center to physically tilt the board and accelerate the marble.
- **Difficulty Selection:** On the Game Over / Victory screen:
  - Click **[Easy]**, **[Medium]**, or **[Hard]** buttons, OR
  - Press keyboard keys: `1` (Easy), `2` (Medium), `3` (Hard), `R` (Restart Current).
- **Exit:** Press `ESC`, `Q`, or click **[Exit]**.

---

## 🛠️ Tasks Completed

### Task 1: Refine Collision Detection (Circle vs. AABB)
- **Problem / Bug Diagnosed:** In the original starter code, `_resolve_wall_collisions()` utilized `marble_rect.colliderect(wall_rect)`. Because this checks overlap between the marble's square bounding box and the rectangular wall, the corner of the marble's bounding square collided with the wall's corner when the marble circle was still in empty space (Euclidean distance $> 12\text{px}$). This caused a noticeable "phantom bounce" off thin air.
- **Vibe Coding Prompt Used:**
  > *"Analyze `_resolve_wall_collisions` in `game/game_engine.py`. Replace the `colliderect` axis-aligned bounding box collision test with an exact Circle-to-AABB distance check using clamped coordinates. When a collision occurs, separate the marble along the contact normal and reflect the velocity vector with a restitution factor of 0.35 so bounces only occur when the circular marble perimeter visually contacts the wall."*
- **Solution Implemented:**
  1. Clamped the marble center $(x_m, y_m)$ to the wall rectangle bounds:
     $$x_c = \max(\text{left}, \min(x_m, \text{right})), \quad y_c = \max(\text{top}, \min(y_m, \text{bottom}))$$
  2. Evaluated squared Euclidean distance:
     $$d^2 = (x_m - x_c)^2 + (y_m - y_c)^2$$
  3. Collision triggers if and only if $d^2 < r^2$.
  4. Positional correction and impulse reflection:
     $$\mathbf{x}_{\text{new}} = \mathbf{x} + \hat{\mathbf{n}} \cdot (r - d), \quad \mathbf{v}_{\text{reflected}} = \mathbf{v} - (1 + e)(\mathbf{v} \cdot \hat{\mathbf{n}})\hat{\mathbf{n}}$$

### Task 2: Implement Game Over & Victory Condition Screens
- **Problem Diagnosed:** The initial codebase simply printed strings (`"Solved!"` or `"Time's up!"`) to stdout and left the game frozen without visual UI feedback.
- **Vibe Coding Prompt Used:**
  > *"Design and render an end-game overlay modal card for Pygame when the game finishes. If solved, display 'MAZE SOLVED!' in vibrant green with elapsed completion time. If timed out, display 'TIME'S UP!' in crimson red. Pause gameplay inputs while gracefully awaiting replay or exit actions."*
- **Solution Implemented:**
  - Added semi-transparent dark backdrop overlay (`rgba(15, 18, 30, 220)`) and card modal container with rounded corners and high-contrast status borders.
  - Formatted precise completion metrics: `Finished in X.XXs`.

### Task 3: Add Replay Option & Difficulty Selection
- **Problem Diagnosed:** Players had to close and restart the application to play another round.
- **Vibe Coding Prompt Used:**
  > *"Implement a replay system offering three selectable difficulty tiers: Easy (60s timer, high friction, higher tilt grip), Medium (45s timer, balanced physics), and Hard (30s timer, slippery low friction, fast max speed). Support interactive mouse button clicks and keyboard hotkeys (1, 2, 3, R, Q, ESC) to reset the maze state seamlessly."*
- **Solution Implemented:**
  - Configured difficulty presets:
    - **Easy:** `tilt_strength = 0.80`, `friction = 0.035`, `time_limit_ms = 60000`, `max_speed = 8.0`
    - **Medium:** `tilt_strength = 0.60`, `friction = 0.020`, `time_limit_ms = 45000`, `max_speed = 9.0`
    - **Hard:** `tilt_strength = 0.45`, `friction = 0.012`, `time_limit_ms = 30000`, `max_speed = 11.0`
  - Replay method `restart(difficulty)` resets marble coordinates to `(50, 50)`, resets velocity to zero, resets countdown clock, and re-enables physics.

### Task 4: Add Sound Feedback
- **Problem Diagnosed:** The starter game had zero audio feedback.
- **Vibe Coding Prompt Used:**
  > *"Add sound effects for wall bounces, reaching the goal, and timer expiration using Pygame mixer. Synthesize pure procedural 16-bit 44.1kHz PCM WAV audio files so no external asset files are missing, and include debouncing on wall bounce audio to prevent stuttering."*
- **Solution Implemented:**
  - Generated standard WAV audio assets inside `game/sounds/`:
    - `bounce.wav`: Fast acoustic pop frequency sweep with exponential decay.
    - `goal.wav`: 4-note ascending chord fanfare (C5 $\to$ E5 $\to$ G5 $\to$ C6).
    - `timeout.wav`: Descending double-pulse buzzer alert.
  - Safe initialization in `GameEngine._init_sounds()` with headless fallback and 90ms audio debouncing.

---

## 📁 Repository Directory Structure

```text
42_marble-tilt-maze/
├── main.py                     # Application entry point with event handling
├── requirements.txt            # Project dependencies (pygame)
├── README.md                   # Complete documentation and submission checklist
├── game/
│   ├── game_engine.py          # Core physics, collision resolution, UI rendering
│   ├── marble.py               # Marble entity model with radius and velocity
│   ├── wall.py                 # Wall obstacle model with Rect definition
│   └── sounds/                 # Generated 16-bit 44.1kHz WAV sound assets
│       ├── bounce.wav          # Acoustic wall collision sound
│       ├── goal.wav            # Melodic victory fanfare sound
│       └── timeout.wav         # Countdown expiration buzzer
```

---

## ✅ Submission Checklist

- [x] **A 10-second video of gameplay before your changes**, showing the bug/broken behavior (`videos/before_gameplay.mp4`)
- [x] **A 10-second video of gameplay after your changes**, showing the bug fixed and the new features working (`videos/after_gameplay.mp4`)
- [x] **The Chat/LLM used page link & exported document**, with the complete chat history ([Lab_4_VibeCoding_Chat_History_PES1UG24CS473.pdf](https://github.com/SubramaniBM/MyProject_MicroserviceCatalog/blob/main/Lab-4/Lab_4_VibeCoding_Chat_History_PES1UG24CS473.pdf))
