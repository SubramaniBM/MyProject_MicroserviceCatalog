# 6-Folder for Practicing on Software Testing Tools

**Course:** Software Engineering Lab — Department of CSE, PES University  
**Student Name:** Subramani B M &nbsp;|&nbsp; **SRN:** PES1UG24CS473 &nbsp;|&nbsp; **Section:** H  

---

## 🧭 Overview & Lab Modules

This folder serves as the central hub for **Software Testing Tools, Defect Remediation, and Automated Static Code Analysis** across the Software Engineering Laboratory curriculum:

1. **Lab 4: Vibe Coding & Dynamic Test Case Verification** (Marble Tilt Maze — Problem Statement #42)
2. **Lab 5: Static Code Analysis & Security Hardening** (Restaurant Dining Billing System — Problem Statement #49)

---

## 🍽️ Lab 5: Static Code Analysis (Pylint, Bandit, Flake8)

- **Problem Statement #49:** Restaurant Dining Order Billing and Kitchen Ticket System
- **Assigned Repository:** [https://github.com/SETAPESU26/L5_49_restaurant_order_system](https://github.com/SETAPESU26/L5_49_restaurant_order_system)
- **Personal Fork & Solution Repository:** [https://github.com/SubramaniBM/L5_49_restaurant_order_system](https://github.com/SubramaniBM/L5_49_restaurant_order_system)
- **Dedicated Lab-5 Directory:** [`../Lab-5/`](../Lab-5/)

### Static Analysis Toolchain & Results
- **Pylint Score:** Elevated from **4.81/10.00** to a perfect **10.00/10.00** (+107.9% improvement).
- **Bandit Security:** Remediated all 5 vulnerabilities (2 High severity shell/hash risks, 1 Medium eval execution risk, 2 Low risks) to **0 issues**.
- **Flake8 Compliance:** Resolved all 9 PEP 8 formatting, unused import, and style violations to **0 violations**.

### 3 Disciplined Git Commits (Handout Requirement)
1. `da707ce`: *Fix Bandit security issues: eliminate eval, replace os.system shell call, use sha256 and secure random pin*
2. `1f5108b`: *Fix Flake8 PEP 8 style issues: remove unused imports, wrap long lines, fix None comparison, and add trailing newline*
3. `b4583db`: *Fix Pylint code quality issues, achieve 10.00/10 score, add reports, issues table, and reflection document*

---

## 🕹️ Lab 4: Vibe Coding & Software Testing (Game #42)

- **Problem Statement #42:** Marble Tilt Maze Game
- **Assigned Repository:** [https://github.com/SETAPESU26/42_marble-tilt-maze](https://github.com/SETAPESU26/42_marble-tilt-maze)
- **Personal Fork & Solution Repository:** [https://github.com/SubramaniBM/42_marble-tilt-maze](https://github.com/SubramaniBM/42_marble-tilt-maze)
- **Dedicated Lab-4 Directory:** [`../Lab-4/`](../Lab-4/)

### Testing Methodology & 4 Tasks
1. **Task 1: Circle-vs-AABB Collision Refinement:** Eliminated phantom corner bounces via clamped Euclidean distance.
2. **Task 2: Game Over Condition & Modal UI:** Added victory/timeout overlay cards with finish time tracking.
3. **Task 3: Replay Option & Difficulty Selection:** Configured Easy (60s), Medium (45s), and Hard (30s) presets.
4. **Task 4: Sound Feedback System:** Pure procedural 16-bit 44.1kHz PCM WAV audio generation (`bounce.wav`, `goal.wav`, `timeout.wav`).

---

## 📦 Master Deliverables Quick Links

1. **Lab 5 Solution Repository:** [https://github.com/SubramaniBM/L5_49_restaurant_order_system](https://github.com/SubramaniBM/L5_49_restaurant_order_system)
2. **Lab 5 Static Analysis PDF Report:** [`../Lab-5/Lab_5_Static_Code_Analysis_Report_PES1UG24CS473.pdf`](../Lab-5/Lab_5_Static_Code_Analysis_Report_PES1UG24CS473.pdf)
3. **Lab 5 Issues Table & Reflection:** [`../Lab-5/issues.md`](../Lab-5/issues.md) & [`../Lab-5/reflection.md`](../Lab-5/reflection.md)
4. **Lab 4 Solution Repository:** [https://github.com/SubramaniBM/42_marble-tilt-maze](https://github.com/SubramaniBM/42_marble-tilt-maze)
5. **Lab 4 Videos (Before & After):** [`../Lab-4/videos/before_gameplay.mp4`](../Lab-4/videos/before_gameplay.mp4) & [`../Lab-4/videos/after_gameplay.mp4`](../Lab-4/videos/after_gameplay.mp4)
6. **Lab 4 Chat History PDF:** [`../Lab-4/Lab_4_VibeCoding_Chat_History_PES1UG24CS473.pdf`](../Lab-4/Lab_4_VibeCoding_Chat_History_PES1UG24CS473.pdf)
