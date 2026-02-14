#!/usr/bin/env python3
"""
24/7 Scheduler for Avengers AI Operating System

Runs agents on schedule:
- Captain America: 3x daily (6am, 12pm, 6pm)
- Daily cycle: Once per day (4am)
- Weekly newsletter: Once per week (Sunday 8am)
"""

import schedule
import time
from datetime import datetime
from main import AvengersAI
from utils.helpers import log_event


class AvengersScheduler:
    """24/7 scheduler for the Avengers AI system."""

    def __init__(self):
        """Initialize scheduler."""
        self.avengers = AvengersAI()
        print("⏰ Avengers AI Scheduler Initialized")
        print("=" * 50)

    def job_daily_cycle(self):
        """Run daily cycle job."""
        try:
            print(f"\n🌅 [{datetime.now()}] Starting scheduled daily cycle...")
            log_event("scheduler", "daily_cycle_start", {})
            self.avengers.run_daily_cycle()
            log_event("scheduler", "daily_cycle_complete", {})
        except Exception as e:
            print(f"❌ Error in daily cycle: {e}")
            log_event("scheduler", "daily_cycle_error", str(e))

    def job_research_sweep(self):
        """Run research sweep job."""
        try:
            print(f"\n🛡 [{datetime.now()}] Starting scheduled research sweep...")
            log_event("scheduler", "research_sweep_start", {})
            self.avengers.captain_america.run_research_sweep()
            log_event("scheduler", "research_sweep_complete", {})
        except Exception as e:
            print(f"❌ Error in research sweep: {e}")
            log_event("scheduler", "research_sweep_error", str(e))

    def job_weekly_newsletter(self):
        """Run weekly newsletter job."""
        try:
            print(f"\n📰 [{datetime.now()}] Starting weekly newsletter...")
            log_event("scheduler", "newsletter_start", {})
            self.avengers.run_weekly_cycle()
            log_event("scheduler", "newsletter_complete", {})
        except Exception as e:
            print(f"❌ Error in newsletter: {e}")
            log_event("scheduler", "newsletter_error", str(e))

    def start(self):
        """Start the scheduler."""
        print("\n📅 Setting up schedule...")
        print("-" * 50)

        # Daily cycle at 4:00 AM
        schedule.every().day.at("04:00").do(self.job_daily_cycle)
        print("  ✓ Daily cycle: 04:00")

        # Research sweeps 3x daily
        schedule.every().day.at("06:00").do(self.job_research_sweep)
        schedule.every().day.at("12:00").do(self.job_research_sweep)
        schedule.every().day.at("18:00").do(self.job_research_sweep)
        print("  ✓ Research sweeps: 06:00, 12:00, 18:00")

        # Weekly newsletter (Sunday at 8 AM)
        schedule.every().sunday.at("08:00").do(self.job_weekly_newsletter)
        print("  ✓ Weekly newsletter: Sunday 08:00")

        print("\n✅ Scheduler running. Press Ctrl+C to stop.")
        print("=" * 50)

        # Run loop
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("\n\n👋 Scheduler stopped by user")
            log_event("scheduler", "stopped", {})


def main():
    """Main entry point."""
    scheduler = AvengersScheduler()
    scheduler.start()


if __name__ == "__main__":
    main()
