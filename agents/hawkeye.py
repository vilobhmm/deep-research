"""Hawkeye - Newsletter & Intelligence Distillation.

Hawkeye filters everything into clarity.
Research + prototypes → structured communication.

Core Principle: "One shot. No fluff."
"""

import sys
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime, timedelta

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.llm import create_agent_llm
from utils.helpers import (
    load_config, save_json, save_markdown, get_timestamp,
    log_event, ensure_dir, get_date_string, list_files
)


class Hawkeye:
    """Newsletter & Intelligence Distillation Agent."""

    def __init__(self):
        """Initialize Hawkeye."""
        self.config = load_config()
        self.agent_config = self.config["agents"]["hawkeye"]
        self.llm = create_agent_llm("hawkeye", self.agent_config)
        self.output_dir = Path("content/newsletter")
        ensure_dir(str(self.output_dir))

    def gather_weekly_intelligence(self) -> Dict[str, Any]:
        """Gather all intelligence from the past week.

        Returns:
            Compiled weekly data
        """
        print("📊 Gathering weekly intelligence...")

        # Collect intelligence reports
        intelligence_files = list_files("intelligence", "*.json")
        research_data = []

        for file in intelligence_files[-7:]:  # Last 7 files
            try:
                with open(file, 'r') as f:
                    import json
                    data = json.load(f)
                    research_data.append(data)
            except:
                pass

        # Collect prototypes
        prototype_dirs = [d for d in Path("prototypes").iterdir() if d.is_dir()]
        prototypes = []

        for proto_dir in prototype_dirs[-5:]:  # Last 5 prototypes
            metadata_file = proto_dir / "prototype_metadata.json"
            if metadata_file.exists():
                try:
                    with open(metadata_file, 'r') as f:
                        import json
                        prototypes.append(json.load(f))
                except:
                    pass

        # Collect social content
        twitter_files = list_files("content/twitter", "*.json")
        linkedin_files = list_files("content/linkedin", "*.json")

        return {
            "research_reports": research_data,
            "prototypes": prototypes,
            "twitter_count": len(twitter_files),
            "linkedin_count": len(linkedin_files),
            "period": f"Week of {get_date_string()}"
        }

    def create_newsletter(self, weekly_data: Dict[str, Any]) -> str:
        """Create newsletter content.

        Args:
            weekly_data: Compiled weekly intelligence

        Returns:
            Newsletter markdown content
        """
        system_prompt = """You are Hawkeye, Newsletter & Intelligence Distillation specialist.

Core Principle: "One shot. No fluff."

Your newsletter must:
- Convert complexity into clarity
- Highlight signal, eliminate noise
- Be structured and scannable
- Provide genuine value
- Tell a coherent story

You turn the week's work into digestible insights.
Every word must earn its place.
"""

        research_summary = "\n".join([
            r.get("analysis", "")[:500] for r in weekly_data.get("research_reports", [])
        ])

        prototypes_summary = "\n".join([
            f"- {p.get('concept', 'Prototype')}: {p.get('path', '')}"
            for p in weekly_data.get("prototypes", [])
        ])

        prompt = f"""Create this week's AI digest newsletter.

Period: {weekly_data.get('period')}

Data:
- Research Reports: {len(weekly_data.get('research_reports', []))}
- Prototypes Built: {len(weekly_data.get('prototypes', []))}
- Twitter Posts: {weekly_data.get('twitter_count', 0)}
- LinkedIn Posts: {weekly_data.get('linkedin_count', 0)}

Research Highlights:
{research_summary}

Prototypes:
{prototypes_summary}

Create a newsletter with these sections:

# 🎯 AI Digest - [Week of DATE]

## 📈 Week's Top AI Developments
Top 3-5 most significant developments
Each with:
- What happened
- Why it matters
- Key takeaway

## 🔬 Research Highlights
Notable papers, releases, or breakthroughs
Signal-only summary

## 🔨 Prototypes Built This Week
Showcase working demos created
Each with:
- Concept implemented
- What you can learn from it
- Link to play with it

## 💡 Signal vs Noise
What to pay attention to vs what to ignore
Honest assessment of hype vs substance

## 👀 What to Watch
Emerging trends and areas to monitor
Forward-looking insights

## 🎓 Learning of the Week
One deep insight or lesson learned
Practical and applicable

---

Keep it:
- Scannable (use bullets, bold, emojis strategically)
- Honest (no hype)
- Actionable (readers should know what to do)
- Concise (value per word)

Length: 1000-1500 words
"""

        newsletter = self.llm.generate(
            prompt,
            system_prompt=system_prompt,
            temperature=0.5,
            max_tokens=8000
        )

        return newsletter

    def generate_newsletter(self) -> Dict[str, Any]:
        """Generate weekly newsletter.

        Returns:
            Newsletter data
        """
        print("🎯 Hawkeye creating newsletter...")

        # Gather weekly data
        weekly_data = self.gather_weekly_intelligence()

        # Create newsletter
        newsletter_content = self.create_newsletter(weekly_data)

        # Save newsletter
        date_str = get_date_string()
        week_str = datetime.now().strftime("week_%Y_W%W")

        # Markdown version
        md_file = self.output_dir / f"newsletter_{week_str}.md"
        save_markdown(newsletter_content, str(md_file))

        # JSON metadata
        metadata = {
            "content": newsletter_content,
            "generated": get_timestamp(),
            "period": weekly_data.get("period"),
            "stats": {
                "research_reports": len(weekly_data.get("research_reports", [])),
                "prototypes": len(weekly_data.get("prototypes", [])),
                "twitter_posts": weekly_data.get("twitter_count", 0),
                "linkedin_posts": weekly_data.get("linkedin_count", 0)
            }
        }

        json_file = self.output_dir / f"newsletter_{week_str}.json"
        save_json(metadata, str(json_file))

        log_event("hawkeye", "newsletter_created", {
            "file": str(md_file),
            "period": weekly_data.get("period")
        })

        print(f"✅ Newsletter complete: {md_file}")

        return metadata


if __name__ == "__main__":
    hawkeye = Hawkeye()

    # Generate newsletter
    newsletter = hawkeye.generate_newsletter()

    print("\n=== Newsletter Preview ===")
    print(newsletter["content"][:500] + "...")
