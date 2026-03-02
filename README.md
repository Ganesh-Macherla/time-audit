# TIME AUDIT

A behavioral time intelligence system that examines how you actually spend your time...and tells you the brutal truth, Because I'm just an idiot who can't manage my time and has attachment issues with the internet.

---

## 🧠 ORIGIN

This project started with a simple realization of losing more time than I had imagined. I ran a self assessment test of timing myself to figure out how much time I was actually wasting. And It's no shocker that 65.8% of the total screen time I invest is short form media content.

The human brain does not have a built-in clock.  
It estimates time based on attention and memory formation.

Deep focus forms strong memory anchors.  
Shallow stimulation on the other hand, like endless doom-scrolling...does not.

When memory density is low, time compresses in hindsight.

Three hours of deep work feels full.  
Three hours of scrolling feels like it vanished.

Time Audit exists to measure that difference.

---

## 🎯 CORE IDEA

Time Audit is not just a timer.

It is a behavioral analysis system that:

- Tracks what applications are opened
- Monitors active windows
- Identifies websites visited
- Analyzes switching frequency
- Detects shallow engagement vs deep focus
- Generates a session report

At the end of a session, it provides:

- Total time spent
- Productivity breakdown
- Distraction percentage
- Focus stability metrics
- Behavioral pattern insights
- A brutally honest roast to hit me back to reality

---

## 🏗 SYSTEM ARCHITCTURE (Planned, but can be altered based on necessity)

Time Audit will operate in layered analysis:

1. **Application Layer**
   - Detect active apps and duration

2. **Domain Layer**
   - Identify website domains (e.g., YouTube, GitHub, Instagram)

3. **Content Classification**
   - Distinguish study content vs entertainment

4. **Behavioral Pattern Analysis**
   - Tab switching frequency
   - Rapid context switching detection
   - Focus streak tracking

5. **Time Context Layer**
   - Time-of-day weighting
   - Productivity probability scoring

---

## 🚀 DEVELOPMENT ROADMAP

# 🔵 PHASE 1 — Core Tracking Engine (Foundation)

## 🎯 Goal

Press **Start** → Track active app → Press **Stop** → Show time per app.


### Step 1 — Setup Project Structure

```
time-audit/
│
├── core/
│   └── tracker.py
│
├── data/
│   └── sessions.db
│
├── analyzer/
│   └── scorer.py
│
├── ui/
│
└── main.py
```


## Step 2 — Install Dependencies

```bash
pip install psutil pygetwindow pynput
```



## Step 3 — Build `tracker.py`

**Features to implement:**

- Detect active window
- Extract app name
- Track duration
- Store usage in dictionary
- Print formatted report

Test this until stable.

Do not move forward until:

- It tracks correctly  
- No crashes  
- Durations are accurate  

---

# 🟢 PHASE 2 — Persistent Storage Layer

Right now it only prints session data.

Now we:

- Create SQLite database
- Store:
  - session_id
  - app_name
  - duration
  - timestamp

**Why?**

Because later phases require historical trend analysis.

---

# 🟡 PHASE 3 — Domain Detection (Browser Layer)

Now add contextual intelligence.

## Step 1 — Build Chrome Extension

Extension responsibilities:

- Detect active tab
- Capture URL + page title
- Send data to localhost server

## Step 2 — Create Local Python Server

Install:

```bash
pip install flask
```

Python server listens for browser data.

Now tracker receives:

- App name
- URL
- Page title

This enables domain-level tracking.

---

# 🟣 PHASE 4 — Classification Layer

Create `analyzer/scorer.py`.

Add:

- Productive apps list
- Distracting apps list
- Mixed apps list

Example:

```python
PRODUCTIVE = ["Code", "VS Code", "LeetCode", "GitHub"]
DISTRACT = ["Instagram", "Netflix", "YouTube Shorts"]
```

Scoring logic:

```python
score = productive_time / total_time
```

Add behavior penalty:

- If tab switches > threshold → reduce score

Output: **Productivity %**

---

# 🔴 PHASE 5 — Behavior Intelligence Engine

Track:

- Tab switch count
- App switch frequency
- Longest uninterrupted streak

Example logic:

If switch rate > threshold → mark session as unstable (turbulence).

This is where behavioral awareness becomes meaningful.

---

# ⚫ PHASE 6 — Roast / Praise Engine

Create `roast.py`.

Rules:

- ≥ 85% → Praise
- 50–84% → Neutral
- < 50% → Roast
- < 30% → Brutal Roast

Initial version:
Template-based responses.

Future version:
LLM-based dynamic generation.

---

# 🟤 PHASE 7 — UI Layer (Only After Core Works)

Build PyQt interface:

- Start button
- Stop button
- Live focus indicator
- Animated report screen

Important:

UI wraps around the engine —  
it does not control the core logic.

---

# 🧠 DEVELOPMENT ORDER SUMMARY

1️⃣ Build tracker  
2️⃣ Store session data  
3️⃣ Add browser intelligence  
4️⃣ Add classification  
5️⃣ Add behavior detection  
6️⃣ Add scoring  
7️⃣ Add roast logic  
8️⃣ Build UI  

---

TimeAudit evolves from signal collection → contextual awareness → behavioral intelligence → feedback system.

---

## 🔒 PRIVACY 

- Runs locally
- No screen recording
- No keystroke logging
- No cloud storage (initially)
- Full user control

---

## 🔥 VISION

The goal is not productivity obsession.

The goal is awareness.

If the brain cannot reliably distinguish between deep immersion and shallow stimulation in real time, this Time Audit will.

---

## 📌 STATUS

✅ Current Progress – Phase 1 Complete (Behavioral Core)

The foundational tracking engine has been implemented.

What’s done:

App-level time tracking

Active vs idle detection (keyboard/mouse-based)

App switch counter

Switch rate (per active minute)

Longest focus streak + associated app

Clean session lifecycle management

This phase focuses purely on behavioral signal collection, not interpretation.

Phase 1.7 Output:-
```bash
===== TIME AUDIT REPORT =====
Start Time: 2026-03-02 23:13:51.680456
End Time: 2026-03-02 23:17:39.280713
Total Duration: 0 hr 3 min 48 sec
Active Time: 0 hr 3 min 40 sec
Idle Time: 0 hr 0 min 8 sec

Mozilla Firefox: 0 hr 3 min 25 sec
WhatsApp: 0 hr 0 min 8 sec
Task Switching: 0 hr 0 min 4 sec
Windows PowerShell: 0 hr 0 min 2 sec
Visual Studio Code: 0 hr 0 min 1 sec

----- Behavioral Metrics -----
Total App Switches: 9
Switch Rate: 2.45 per active minute
Longest Focus Streak: 0 hr 1 min 48 sec (Mozilla Firefox)
=============================
```


