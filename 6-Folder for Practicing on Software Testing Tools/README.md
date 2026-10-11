# 6-Folder for Practicing on Software Testing Tools

## Lab 4: Vibe Coding & Software Testing — Marble Tilt Maze (Game #42)

**Student Name:** Subramani B M &nbsp;|&nbsp; **SRN:** PES1UG24CS473 &nbsp;|&nbsp; **Section:** H  
**Course:** Software Engineering Lab — Department of CSE, PES University  
**Assigned Original Repository:** [https://github.com/SETAPESU26/42_marble-tilt-maze](https://github.com/SETAPESU26/42_marble-tilt-maze)  
**Personal Fork & Solution Repository:** [https://github.com/SubramaniBM/42_marble-tilt-maze](https://github.com/SubramaniBM/42_marble-tilt-maze)  
**Dedicated Lab-4 Directory:** [`../Lab-4/`](../Lab-4/)

---

### Overview & Lab Guidelines
In accordance with official PES University Lab guidelines for *Folder 6 (Practicing on Software Testing Tools)* and *Lab 4 (VibeCoding)*:
- Leveraged modern AI-assisted engineering ("vibe coding") to diagnose broken collision logic, implement surgical code patches, and add full game features in under four prompt iterations.
- Executed rigorous unit testing across 6 test conditions.
- Recorded 10-second gameplay verification videos before and after fixes.
- Pushed updated, fully passing game codebase to personal GitHub repository.

---

### Software Testing Methodology & 4 Tasks

#### Task 1: Refined Collision Detection (Circle vs. AABB)
- **Defect Located:** `colliderect` bounding-box collision caused phantom bounces off empty space near wall corners ($d > 12\text{px}$).
- **Vibe Coding Patch:** Clamped coordinates projection onto rectangle edges + Euclidean distance check ($d^2 < r^2$) + contact normal separation and velocity reflection with restitution coefficient $0.35$.

#### Task 2: Game Over Condition & UI Screens
- **Defect Located:** Game over originally only printed to terminal console and froze.
- **Vibe Coding Patch:** Semi-transparent Pygame modal overlay displaying victory banner with elapsed completion time (`Finished in X.XXs`) or timeout alert.

#### Task 3: Interactive Replay Option & Difficulty Selection
- **Feature Added:** Difficulty presets selectable via UI buttons or keyboard hotkeys (`1`: Easy 60s, `2`: Medium 45s, `3`: Hard 30s, `R`: Replay, `ESC`/`Q`: Exit).

#### Task 4: Sound Feedback System
- **Feature Added:** Pure procedural 16-bit 44.1kHz PCM WAV audio generation and Pygame mixer integration (`bounce.wav`, `goal.wav`, `timeout.wav`) with 90ms audio debouncing.

---

### 🧪 Test Execution Matrix (100% Pass Rate)

| Test Case ID | Test Objective | Inputs / Condition | Expected Result | Status |
|:---:|:---|:---|:---|:---:|
| **TC-VIBE-01** | Corner Collision Accuracy | Marble at $(469, 131)$, corner at $(460, 140)$ | $d=12.72\text{px} > 12\text{px}$: Zero false bounce. | **PASSED ✓** |
| **TC-VIBE-02** | True Boundary Reflection | Marble at $(467, 133)$, direct corner contact | $d=9.89\text{px} < 12\text{px}$: Rebound along contact normal. | **PASSED ✓** |
| **TC-VIBE-03** | Goal Reached Game Over | Marble center inside goal circle | `game_over=True`, `result="solved"`, victory modal shown. | **PASSED ✓** |
| **TC-VIBE-04** | Countdown Expiration | Elapsed time $\ge \text{time\_limit\_ms}$ | `game_over=True`, `result="timeout"`, timeout modal shown. | **PASSED ✓** |
| **TC-VIBE-05** | Replay Difficulty Reset | `restart("Hard")` invoked | Timer resets to 30s, friction=0.012, position resets to $(50, 50)$. | **PASSED ✓** |
| **TC-VIBE-06** | Audio Debouncing | Rapid consecutive wall contact ($<90\text{ms}$) | Played once without audio buffer stuttering. | **PASSED ✓** |

---

### 📦 Deliverables & Quick Links

1. **Personal GitHub Repository:** [https://github.com/SubramaniBM/42_marble-tilt-maze](https://github.com/SubramaniBM/42_marble-tilt-maze)
2. **Gameplay Before Video (10s):** [`../Lab-4/videos/before_gameplay.mp4`](../Lab-4/videos/before_gameplay.mp4)
3. **Gameplay After Video (10s):** [`../Lab-4/videos/after_gameplay.mp4`](../Lab-4/videos/after_gameplay.mp4)
4. **Complete Vibe Coding Chat History PDF:** [`../Lab-4/Lab_4_VibeCoding_Chat_History_PES1UG24CS473.pdf`](../Lab-4/Lab_4_VibeCoding_Chat_History_PES1UG24CS473.pdf)
5. **Full Source Code:** [`../Lab-4/code/`](../Lab-4/code/)
