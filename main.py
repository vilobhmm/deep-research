#!/usr/bin/env python3
"""
Avengers AI Operating System - Main Orchestrator

Six agents working 24/7:
- Iron Man: Strategy & Orchestration
- Captain America: Research & Intelligence
- Hulk: Prototype Architect
- Thor: X/Twitter Content
- Black Widow: LinkedIn Content
- Hawkeye: Newsletter Distillation
"""

import sys
from pathlib import Path
from datetime import datetime
from typing import Optional

from agents.iron_man import IronMan
from agents.captain_america import CaptainAmerica
from agents.hulk import Hulk
from agents.thor import Thor
from agents.black_widow import BlackWidow
from agents.hawkeye import Hawkeye
from utils.helpers import log_event, setup_logging, get_timestamp


class AvengersAI:
    """Main orchestrator for the Avengers AI Operating System."""

    def __init__(self):
        """Initialize the system."""
        setup_logging()
        print("🛡⚡ AVENGERS AI OPERATING SYSTEM")
        print("=" * 50)

        # Initialize all agents
        self.iron_man = IronMan()
        self.captain_america = CaptainAmerica()
        self.hulk = Hulk()
        self.thor = Thor()
        self.black_widow = BlackWidow()
        self.hawkeye = Hawkeye()

        log_event("system", "initialized", {"timestamp": get_timestamp()})

    def run_daily_cycle(self, prototype_concept: Optional[str] = None):
        """Run a complete daily cycle.

        Args:
            prototype_concept: Optional specific concept for Hulk to prototype
        """
        print(f"\n🌅 Starting Daily Cycle - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("=" * 50)

        # STEP 1: Captain America - Research
        print("\n🛡 STEP 1: Research Sweep")
        print("-" * 50)
        intelligence_report = self.captain_america.run_research_sweep()

        # STEP 2: Iron Man - Strategic Planning
        print("\n🧠 STEP 2: Strategic Planning")
        print("-" * 50)
        daily_plan = self.iron_man.plan_daily_sprint(intelligence_report)
        print(f"Priorities set: {daily_plan.get('priorities', [])[:3]}")

        # STEP 3: Hulk - Build Prototype
        print("\n🔨 STEP 3: Building Prototype")
        print("-" * 50)

        # Use specified concept or get from plan
        if not prototype_concept:
            hulk_task = daily_plan.get("tasks", {}).get("hulk", "")
            # Try to extract a concept from the task
            prototype_concept = "Daily AI Concept Demo"

        prototype = self.hulk.create_prototype(
            concept=prototype_concept,
            intelligence_context=intelligence_report.get("analysis", "")[:1000]
        )

        # Optional: Test the prototype
        # test_results = self.hulk.test_prototype(prototype["path"])

        # STEP 4: Thor - Twitter Content
        print("\n⚡ STEP 4: Twitter Content")
        print("-" * 50)
        twitter_content = self.thor.generate_content(intelligence_report, mode="tweets")
        print(f"Generated {len(twitter_content['content'])} tweets")

        # STEP 5: Black Widow - LinkedIn Content
        print("\n🕷 STEP 5: LinkedIn Content")
        print("-" * 50)
        linkedin_content = self.black_widow.generate_content(intelligence_report, count=2)
        print(f"Generated {len(linkedin_content['posts'])} LinkedIn posts")

        # STEP 6: Summary
        print("\n✅ DAILY CYCLE COMPLETE")
        print("=" * 50)
        print(f"📊 Summary:")
        print(f"  ✓ Research: {len(intelligence_report.get('raw_data', {}))} sources")
        print(f"  ✓ Prototype: {prototype['prototype_name']}")
        print(f"  ✓ Twitter: {len(twitter_content['content'])} posts")
        print(f"  ✓ LinkedIn: {len(linkedin_content['posts'])} posts")
        print(f"\n📁 All output saved to respective directories")
        print(f"⏰ Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        log_event("system", "daily_cycle_complete", {
            "intelligence_file": intelligence_report.get("analysis", ""),
            "prototype": prototype["prototype_name"],
            "twitter_posts": len(twitter_content['content']),
            "linkedin_posts": len(linkedin_content['posts'])
        })

        return {
            "intelligence": intelligence_report,
            "plan": daily_plan,
            "prototype": prototype,
            "twitter": twitter_content,
            "linkedin": linkedin_content
        }

    def run_weekly_cycle(self):
        """Run weekly tasks (newsletter)."""
        print("\n📰 Running Weekly Cycle")
        print("=" * 50)

        newsletter = self.hawkeye.generate_newsletter()

        print(f"✅ Newsletter generated: {newsletter.get('stats', {})}")
        return newsletter

    def run_quick_research(self):
        """Run just research sweep."""
        print("🛡 Quick Research Sweep")
        return self.captain_america.run_research_sweep()

    def build_prototype(self, concept: str):
        """Build a specific prototype.

        Args:
            concept: Concept to prototype
        """
        print(f"🔨 Building Prototype: {concept}")
        return self.hulk.create_prototype(concept)


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Avengers AI Operating System - Multi-Agent AI Lab"
    )
    parser.add_argument(
        "--mode",
        choices=["daily", "weekly", "research", "prototype"],
        default="daily",
        help="Operating mode"
    )
    parser.add_argument(
        "--concept",
        type=str,
        help="Specific concept for prototype mode"
    )

    args = parser.parse_args()

    # Initialize system
    avengers = AvengersAI()

    # Run based on mode
    if args.mode == "daily":
        avengers.run_daily_cycle(prototype_concept=args.concept)

    elif args.mode == "weekly":
        avengers.run_weekly_cycle()

    elif args.mode == "research":
        avengers.run_quick_research()

    elif args.mode == "prototype":
        if not args.concept:
            print("Error: --concept required for prototype mode")
            sys.exit(1)
        avengers.build_prototype(args.concept)


if __name__ == "__main__":
    main()
