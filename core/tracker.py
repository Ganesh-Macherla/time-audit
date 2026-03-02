import time
import pygetwindow as gw
from collections import defaultdict
from datetime import datetime


class TimeAuditTracker:
    def __init__(self, interval=1):
        self.interval = interval
        self.running = False
        self.app_usage = defaultdict(int)
        self.start_time = None
        self.end_time = None

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

        # Handle em dash (—)
        if "—" in window_title:
            return window_title.split("—")[-1].strip()

        # Handle normal dash (-)
        if "-" in window_title:
            return window_title.split("-")[-1].strip()

        return window_title.strip()

    def start(self):
        print("\nSession started...\n")
        self.running = True
        self.start_time = datetime.now()

        while self.running:
            title = self.get_active_window_title()
            app_name = self.extract_app_name(title)

            if app_name:
                self.app_usage[app_name] += self.interval

            time.sleep(self.interval)

    def stop(self):
        self.running = False
        self.end_time = datetime.now()
        self.generate_report()

    def generate_report(self):
        total_seconds = sum(self.app_usage.values())

        print("\n===== TIME AUDIT REPORT =====")
        print(f"Start Time: {self.start_time}")
        print(f"End Time: {self.end_time}")

        total_hours = total_seconds // 3600
        total_minutes = (total_seconds % 3600) // 60
        total_remaining_seconds = total_seconds % 60

        print(f"Total Duration: {total_hours} hr {total_minutes} min {total_remaining_seconds} sec\n")

        sorted_usage = sorted(self.app_usage.items(), key=lambda x: x[1], reverse=True)

        for app, seconds in sorted_usage:
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            remaining_seconds = seconds % 60

            print(f"{app}: {hours} hr {minutes} min {remaining_seconds} sec")

        print("=============================\n")


if __name__ == "__main__":
    tracker = TimeAuditTracker(interval=1)

    input("Press ENTER to start tracking...")
    try:
        tracker.start()
    except KeyboardInterrupt:
        tracker.stop()