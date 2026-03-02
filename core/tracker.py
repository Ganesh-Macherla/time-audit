import time
import pygetwindow as gw
from collections import defaultdict
from datetime import datetime
from pynput import keyboard, mouse


class TimeAuditTracker:
    def __init__(self, interval=1, idle_threshold=10):
        self.interval = interval
        self.idle_threshold = idle_threshold
        self.running = False

        self.app_usage = defaultdict(int)
        self.start_time = None
        self.end_time = None

        # Behavior tracking
        self.last_app = None
        self.switch_count = 0
        self.current_streak = 0
        self.longest_streak = 0
        self.longest_streak_app = None

        # Idle tracking
        self.last_activity_time = time.time()
        self.idle_time = 0
        self.active_time = 0
        self.is_idle = False

    # -------- Idle Detection --------

    def on_activity(self, *args):
        self.last_activity_time = time.time()
        self.is_idle = False  # Exit idle state on activity

    def start_activity_listener(self):
        keyboard.Listener(on_press=self.on_activity).start()
        mouse.Listener(
            on_move=self.on_activity,
            on_click=self.on_activity,
            on_scroll=self.on_activity
        ).start()

    # -------- Window Tracking --------

    def get_active_window_title(self):
        try:
            window = gw.getActiveWindow()
            if window:
                return window.title
            return None
        except:
            return None

    def extract_app_name(self, window_title):
        if not window_title:
            return "Unknown"

        if "—" in window_title:
            return window_title.split("—")[-1].strip()

        if "-" in window_title:
            return window_title.split("-")[-1].strip()

        return window_title.strip()

    # -------- Session Control --------

    def start(self):
        print("\nSession started...\n")
        self.running = True
        self.start_time = datetime.now()
        self.start_activity_listener()

        while self.running:
            now = time.time()
            idle_duration = now - self.last_activity_time

            # --- IDLE STATE ---
            if idle_duration > self.idle_threshold:
                self.idle_time += self.interval

                # If entering idle for first time, break streak
                if not self.is_idle:
                    self.is_idle = True

                    if self.current_streak > self.longest_streak:
                        self.longest_streak = self.current_streak
                        self.longest_streak_app = self.last_app

                    self.current_streak = 0

            # --- ACTIVE STATE ---
            else:
                self.active_time += self.interval

                title = self.get_active_window_title()
                app_name = self.extract_app_name(title)

                if app_name:
                    self.app_usage[app_name] += self.interval

                    if app_name != self.last_app:
                        if self.last_app is not None:
                            self.switch_count += 1

                            if self.current_streak > self.longest_streak:
                                self.longest_streak = self.current_streak
                                self.longest_streak_app = self.last_app

                            self.current_streak = 0

                    self.current_streak += self.interval
                    self.last_app = app_name

            time.sleep(self.interval)

    def stop(self):
        self.running = False
        self.end_time = datetime.now()

        # Final streak check
        if self.current_streak > self.longest_streak:
            self.longest_streak = self.current_streak
            self.longest_streak_app = self.last_app

        self.generate_report()

    # -------- Reporting --------

    def format_time(self, seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        remaining_seconds = seconds % 60
        return f"{hours} hr {minutes} min {remaining_seconds} sec"

    def generate_report(self):
        total_seconds = self.active_time + self.idle_time

        print("\n===== TIME AUDIT REPORT =====")
        print(f"Start Time: {self.start_time}")
        print(f"End Time: {self.end_time}")
        print(f"Total Duration: {self.format_time(total_seconds)}")
        print(f"Active Time: {self.format_time(self.active_time)}")
        print(f"Idle Time: {self.format_time(self.idle_time)}\n")

        sorted_usage = sorted(self.app_usage.items(), key=lambda x: x[1], reverse=True)

        for app, seconds in sorted_usage:
            print(f"{app}: {self.format_time(seconds)}")

        active_minutes = self.active_time / 60 if self.active_time > 0 else 1
        switch_rate = self.switch_count / active_minutes

        print("\n----- Behavioral Metrics -----")
        print(f"Total App Switches: {self.switch_count}")
        print(f"Switch Rate: {round(switch_rate, 2)} per active minute")

        if self.longest_streak_app:
            print(
                f"Longest Focus Streak: {self.format_time(self.longest_streak)} "
                f"({self.longest_streak_app})"
            )

        print("=============================\n")


if __name__ == "__main__":
    tracker = TimeAuditTracker(interval=1, idle_threshold=10)

    input("Press ENTER to start tracking...")
    try:
        tracker.start()
    except KeyboardInterrupt:
        tracker.stop()
