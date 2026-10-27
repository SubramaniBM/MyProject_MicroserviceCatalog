# 🍽️ Lab 5: Static Code Analysis — Restaurant Order System (#49)

**Course:** Software Engineering Lab — Department of Computer Science & Engineering, PES University  
**Student Name:** Subramani B M  
**SRN:** PES1UG24CS473  
**Section:** H  
**Problem Statement #49:** Restaurant Dining Order Billing and Kitchen Ticket System  
**Assigned Repository:** [https://github.com/SETAPESU26/L5_49_restaurant_order_system](https://github.com/SETAPESU26/L5_49_restaurant_order_system)  
**Personal Solution Repository:** [https://github.com/SubramaniBM/L5_49_restaurant_order_system](https://github.com/SubramaniBM/L5_49_restaurant_order_system)  
**Main Lab Catalog:** [https://github.com/SubramaniBM/MyProject_MicroserviceCatalog](https://github.com/SubramaniBM/MyProject_MicroserviceCatalog)

---

## 📋 Lab 5 Deliverables Directory

In strict adherence to the official [`Lab_5_Static_Code_Analysis_Student_handout.pdf`](Lab_5_Static_Code_Analysis_Student_handout.pdf), all required deliverables are structured below:

| Deliverable Name | Description | Direct File Link |
|:---|:---|:---:|
| **Cleaned Source Code** | Remediated Python code achieving a **10.00/10.00 Pylint score**, **0 Bandit security issues**, and **0 Flake8 style violations**. | [`restaurant_order_system.py`](restaurant_order_system.py) |
| **Documented Issue Table** | Detailed markdown table documenting all 14 identified issues across Pylint, Bandit, and Flake8. | [`issues.md`](issues.md) |
| **Reflection &amp; Analysis** | In-depth answers to all four lab reflection questions regarding code quality, tool synergy, and severity triage. | [`reflection.md`](reflection.md) |
| **Comprehensive PDF Report** | Official 2-page master PDF compiling the issue table, comparative metrics, diffs, and reflections. | [`Lab_5_Static_Code_Analysis_Report_PES1UG24CS473.pdf`](Lab_5_Static_Code_Analysis_Report_PES1UG24CS473.pdf) |
| **Static Analysis Reports** | Raw generated reports from Pylint, Bandit, and Flake8 captured **before** and **after** code remediation. | [`reports/`](reports/) |
| **Official Course Handout** | Reference handout preserved for evaluation. | [`Lab_5_Static_Code_Analysis_Student_handout.pdf`](Lab_5_Static_Code_Analysis_Student_handout.pdf) |

---

## 📊 Quantitative Quality Benchmark

| Static Analysis Tool | Baseline (Before Fixes) | Remediated (After Fixes) | Net Improvement |
|:---|:---:|:---:|:---:|
| **Pylint Code Quality Score** | **4.81 / 10.00** | **10.00 / 10.00** | **+5.19 (+107.9%) — PERFECT** |
| **Bandit Security Scanner** | **5 Issues** (2 High, 1 Medium, 2 Low) | **0 Issues Identified** | **100% Security Remediation** |
| **Flake8 Style Enforcer** | **9 PEP 8 Violations** | **0 Violations** | **100% PEP 8 Compliance** |
| **Total Tracked Defect Count** | **36 Quality / Style / Security Defects** | **0 Remaining** | **Zero Defect State** |

---

## 🛠️ Summary of Git Commits on Personal Solution Fork

In accordance with lab instructions to maintain 3 commits corresponding to the three static analysis tools, the following commit history was pushed to [https://github.com/SubramaniBM/L5_49_restaurant_order_system](https://github.com/SubramaniBM/L5_49_restaurant_order_system):

1. **Commit 1 (`da707ce`):**  
   *`Fix Bandit security issues: eliminate eval, replace os.system shell call, use sha256 and secure random pin`*  
   - Eliminated remote code execution vector `eval(promo_expr)` (`B307`).
   - Removed shell execution `os.system()` to prevent command injection (`B605`).
   - Replaced weak MD5 hash with SHA-256 (`B324`).
   - Replaced pseudo-random PIN generator with `secrets.SystemRandom()` (`B311`).
   - Replaced bare `try/except: pass` with explicit membership check (`B110`).
2. **Commit 2 (`1f5108b`):**  
   *`Fix Flake8 PEP 8 style issues: remove unused imports, wrap long lines, fix None comparison, and add trailing newline`*  
   - Removed unused imports `os` and `math` (`F401`).
   - Removed dead local assignments `service_tax = 3.50` (`F841`).
   - Reformatted lines exceeding 79 characters (`E501`).
   - Fixed singleton equality check to `is None` (`E711`).
   - Added trailing POSIX newline at EOF (`W292`).
3. **Commit 3 (`b4583db`):**  
   *`Fix Pylint code quality issues, achieve 10.00/10 score, add reports, issues table, and reflection document`*  
   - Fixed dangerous mutable default parameter `order_log=[]` $\to$ `order_log=None` (`W0102`).
   - Renamed functions to standard PEP 8 snake_case (`C0103`).
   - Authored comprehensive docstrings for all module functions (`C0116`).
   - Implemented context manager with explicit UTF-8 encoding for file I/O (`R1732`, `W1514`).
   - Resolved variable shadowing of global `orders` dictionary (`W0621`).
   - Modernized `%` formatting to f-strings (`C0209`).
   - Pylint score achieved: **10.00 / 10.00**.

---

## 🧪 Verification & Execution Commands

Run the static analysis suite locally:

```bash
# 1. Pylint Analysis (Target: > 9.5, Achieved: 10.00/10.00)
python3 -m pylint restaurant_order_system.py

# 2. Bandit Security Analysis (Target: 0 Issues)
python3 -m bandit -r restaurant_order_system.py

# 3. Flake8 PEP 8 Style Inspection (Target: 0 Violations)
python3 -m flake8 restaurant_order_system.py

# 4. Program Execution
python3 restaurant_order_system.py
```
