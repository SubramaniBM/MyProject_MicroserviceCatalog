# 🕹️ Lab 4: Vibe Coding — Interactive Physics Tilt Maze

**Course:** Software Engineering Lab — Department of Computer Science & Engineering, PES University  
**Student Name:** Subramani B M  
**SRN:** PES1UG24CS473  
**Section:** H  
**Problem Statement #42:** Marble Tilt Maze Game  
**Assigned Repository:** [https://github.com/SETAPESU26/42_marble-tilt-maze](https://github.com/SETAPESU26/42_marble-tilt-maze)  
**Personal Fork Repository:** [https://github.com/SubramaniBM/42_marble-tilt-maze](https://github.com/SubramaniBM/42_marble-tilt-maze)  
**Main Lab Catalog:** [https://github.com/SubramaniBM/MyProject_MicroserviceCatalog](https://github.com/SubramaniBM/MyProject_MicroserviceCatalog)

---

## 📋 Lab 4 Deliverables Summary

In strict accordance with the official [`Lab_4_VibeCoding_Student_handout.pdf`](Lab_4_VibeCoding_Student_handout.pdf), all required deliverables are structured below:

| Deliverable Code | Deliverable Name | Description | File / Direct Link |
|:---:|:---|:---|:---:|
| **a** | **Gameplay Videos (Before & After)** | 10-second gameplay video showing the bug before fixes, and 10-second gameplay video showing the bug fixed with all new features. | [`videos/before_gameplay.mp4`](videos/before_gameplay.mp4)<br/>[`videos/after_gameplay.mp4`](videos/after_gameplay.mp4) |
| **b** | **Updated Code** | Full Python source code implementing all 4 tasks with procedural sound assets. | [`code/`](code/) & [GitHub Fork](https://github.com/SubramaniBM/42_marble-tilt-maze) |
| **c** | **Exported Chat History** | 2-Page comprehensive PDF documenting the exact prompt-engineering dialogue, math models, unit tests, and screenshots. | [`Lab_4_VibeCoding_Chat_History_PES1UG24CS473.pdf`](Lab_4_VibeCoding_Chat_History_PES1UG24CS473.pdf) |
| **d** | **Official Handout** | Reference handout from course faculty. | [`Lab_4_VibeCoding_Student_handout.pdf`](Lab_4_VibeCoding_Student_handout.pdf) |

---

## 🎯 Task Breakdown & Vibe Coding Prompts

### Task 1: Refine Collision Detection (Circle vs. AABB)
- **Bug Diagnosed:** The starter code evaluated `colliderect` between the marble's square bounding box and rectangular walls. Near wall corners (e.g. `(460, 140)`), the corners of the bounding box collided while the circle's Euclidean distance from the corner was $> 12\text{px}$, causing the marble to bounce off thin air.
- **Vibe Coding Prompt:**
  > *"Analyze `_resolve_wall_collisions` in `game/game_engine.py`. Replace the `colliderect` axis-aligned bounding box collision test with an exact Circle-to-AABB distance check using clamped coordinates. When a collision occurs, separate the marble along the contact normal and reflect the velocity vector with a restitution factor of 0.35 so bounces only occur when the circular marble perimeter visually contacts the wall."*
- **Mathematical Solution:**
  1. Clamped coordinate projection:
     $$x_c = \max(\text{left}, \min(x_m, \text{right})), \quad y_c = \max(\text{top}, \min(y_m, \text{bottom}))$$
  2. Distance check: Collision triggers if and only if:
     $$d^2 = (x_m - x_c)^2 + (y_m - y_c)^2 < r^2$$
  3. Impulse resolution:
     $$\mathbf{x}_{\text{corrected}} = \mathbf{x} + \hat{\mathbf{n}} \cdot (r - d), \quad \mathbf{v}' = \mathbf{v} - (1 + e)(\mathbf{v} \cdot \hat{\mathbf{n}})\hat{\mathbf{n}} \quad (e=0.35)$$

---

### Task 2: Implement Game Over & Victory Condition Screens
- **Bug Diagnosed:** Game over merely printed strings to the console without an in-game UI screen.
- **Vibe Coding Prompt:**
  > *"Design and render an end-game overlay modal card for Pygame when the game finishes. If solved, display 'MAZE SOLVED!' in vibrant green with elapsed completion time. If timed out, display 'TIME'S UP!' in crimson red. Pause gameplay inputs while gracefully awaiting replay or exit actions."*
- **Features Implemented:**
  - Alpha-blended dark backdrop overlay (`rgba(15, 18, 30, 220)`).
  - Rounded modal card with color-coded status border (Emerald Green `#3cd070` on win, Coral Red `#eb4b4b` on timeout).
  - High-precision timer readout: `Finished in X.XXs`.

---

### Task 3: Add Replay Option & Multi-Tier Difficulty Selection
- **Feature Implemented:** Replay modal with 3 configurable difficulty tiers without requiring application restart.
- **Vibe Coding Prompt:**
  > *"Implement a replay system offering three selectable difficulty tiers: Easy (60s timer, high friction, higher tilt grip), Medium (45s timer, balanced physics), and Hard (30s timer, slippery low friction, fast max speed). Support interactive mouse button clicks and keyboard hotkeys (1, 2, 3, R, Q, ESC) to reset the maze state seamlessly."*
- **Difficulty Configurations:**
  - **Easy:** Tilt strength: 0.80, Friction: 0.035, Time Limit: 60s, Max Speed: 8.0 px/frame
  - **Medium (Default):** Tilt strength: 0.60, Friction: 0.020, Time Limit: 45s, Max Speed: 9.0 px/frame
  - **Hard:** Tilt strength: 0.45, Friction: 0.012, Time Limit: 30s, Max Speed: 11.0 px/frame (High-speed, low-friction challenge)

---

### Task 4: Add Sound Feedback
- **Feature Implemented:** Pure procedural 16-bit 44.1kHz PCM WAV audio generation and Pygame mixer integration.
- **Vibe Coding Prompt:**
  > *"Add sound effects for wall bounces, reaching the goal, and timer expiration using Pygame mixer. Synthesize pure procedural 16-bit 44.1kHz PCM WAV audio files so no external asset files are missing, and include debouncing on wall bounce audio to prevent stuttering."*
- **Sound Assets in `game/sounds/`:**
  - `bounce.wav`: Rapid acoustic frequency sweep ($320\text{Hz} \to 120\text{Hz}$) with exponential decay envelope (120ms).
  - `goal.wav`: 4-tone ascending arpeggio fanfare (C5 $\to$ E5 $\to$ G5 $\to$ C6) (800ms).
  - `timeout.wav`: Descending 2-pulse alert buzzer ($220\text{Hz}$) (500ms).
  - 90ms audio debouncer prevents audio stuttering when marble rolls against walls.

---

## 🧪 Verification & Test Suite

| Test Case ID | Test Objective | Inputs / Condition | Expected Result | Status |
|:---:|:---|:---|:---|:---:|
| **TC-VIBE-01** | Corner Collision Accuracy | Marble at $(469, 131)$, corner at $(460, 140)$ | $d=12.72\text{px} > 12\text{px}$: Zero false bounce. | **PASSED ✓** |
| **TC-VIBE-02** | True Boundary Reflection | Marble at $(467, 133)$, direct corner contact | $d=9.89\text{px} < 12\text{px}$: Rebound along contact normal. | **PASSED ✓** |
| **TC-VIBE-03** | Goal Reached Game Over | Marble center inside goal circle | `game_over=True`, `result="solved"`, victory modal shown. | **PASSED ✓** |
| **TC-VIBE-04** | Countdown Expiration | Elapsed time $\ge \text{time\_limit\_ms}$ | `game_over=True`, `result="timeout"`, timeout modal shown. | **PASSED ✓** |
| **TC-VIBE-05** | Replay Difficulty Reset | `restart("Hard")` invoked | Timer resets to 30s, friction=0.012, position resets to $(50, 50)$. | **PASSED ✓** |
| **TC-VIBE-06** | Audio Debouncing | Rapid consecutive wall contact ($<90\text{ms}$) | Played once without audio buffer stuttering. | **PASSED ✓** |

---

## 🚀 How to Run the Game Locally

1. Navigate to the code directory:
   ```bash
   cd Lab-4/code
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run:
   ```bash
   python main.py
   ```
