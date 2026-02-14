"""Black Widow - LinkedIn Authority Architect.

Black Widow transforms intelligence into professional positioning.
Composed, high-signal, strategic content for the long game.

Core Principle: "Influence is built, not shouted."
"""

import sys
from pathlib import Path
from typing import Dict, Any, List

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.llm import create_agent_llm
from utils.helpers import (
    load_config, save_json, save_markdown, get_timestamp,
    log_event, ensure_dir, get_date_string
)


class BlackWidow:
    """LinkedIn Authority Architect - Converts knowledge into reputation capital."""

    def __init__(self):
        """Initialize Black Widow."""
        self.config = load_config()
        self.agent_config = self.config["agents"]["black_widow"]
        self.llm = create_agent_llm("black_widow", self.agent_config)
        self.output_dir = Path("content/linkedin")
        ensure_dir(str(self.output_dir))

    def craft_post(
        self,
        topic: str,
        intelligence_context: str = "",
        post_type: str = "thought_leadership"
    ) -> Dict[str, str]:
        """Craft a LinkedIn post.

        Args:
            topic: Post topic
            intelligence_context: Research context
            post_type: Type of post (thought_leadership, analysis, insight, etc.)

        Returns:
            Post content
        """
        system_prompt = """You are Black Widow, LinkedIn Authority Architect.

Tone: Composed, high-signal, strategic
Core Principle: "Influence is built, not shouted."

Your posts must:
- Demonstrate deep expertise
- Provide genuine value
- Build professional credibility
- Be strategic and composed
- Show thoughtful analysis

You convert knowledge into reputation capital.
Quality over quantity. Signal over noise.
"""

        prompt = f"""Create a LinkedIn post about: {topic}

Type: {post_type}

Context:
{intelligence_context}

Requirements:
1. Start with a strong hook (first 2 lines critical - they appear in feed)
2. Share genuine insight, not surface-level observations
3. Include specific examples or data points
4. Demonstrate technical depth without jargon overload
5. End with a thought-provoking question or call-to-action
6. Length: 800-1200 characters (LinkedIn sweet spot)

Structure:
- Hook (2 lines)
- Context/Setup
- Key insights (2-3 points)
- Concrete example or data
- Conclusion with CTA

Make it professional yet accessible.
Show expertise through clarity, not complexity.
"""

        post_text = self.llm.generate(
            prompt,
            system_prompt=system_prompt,
            temperature=0.6,
            max_tokens=2000
        )

        post = {
            "text": post_text,
            "topic": topic,
            "type": post_type,
            "created": get_timestamp(),
            "status": "draft",
            "character_count": len(post_text)
        }

        log_event("black_widow", "post_crafted", {
            "topic": topic,
            "type": post_type,
            "length": len(post_text)
        })

        return post

    def craft_deep_analysis(
        self,
        topic: str,
        intelligence_report: Dict[str, Any]
    ) -> Dict[str, str]:
        """Craft a deep analysis post.

        Args:
            topic: Analysis topic
            intelligence_report: Full research report

        Returns:
            Analysis post
        """
        system_prompt = """You are Black Widow crafting deep technical analysis for LinkedIn.

This is strategic content that:
- Positions you as a subject matter expert
- Demonstrates analytical rigor
- Provides frameworks others can use
- Builds long-term credibility

Be thorough but clear.
Insight, not information dump.
"""

        analysis = intelligence_report.get("analysis", "")

        prompt = f"""Create a deep analysis post on: {topic}

Intelligence:
{analysis}

Structure:
1. Hook: Why this matters now
2. The Landscape: Current state
3. Key Insight: Your unique take (the value-add)
4. Implications: What this means
5. Action: What to watch/do next

Make it:
- Comprehensive but readable
- Data-informed where possible
- Forward-looking
- Actionable

Length: 1000-1500 characters
"""

        post_text = self.llm.generate(
            prompt,
            system_prompt=system_prompt,
            temperature=0.5,
            max_tokens=3000
        )

        return {
            "text": post_text,
            "topic": topic,
            "type": "deep_analysis",
            "created": get_timestamp(),
            "status": "draft",
            "character_count": len(post_text)
        }

    def generate_content(
        self,
        intelligence_report: Dict[str, Any],
        count: int = 3
    ) -> Dict[str, Any]:
        """Generate LinkedIn content.

        Args:
            intelligence_report: Research report
            count: Number of posts to generate

        Returns:
            Generated content
        """
        print(f"🕷 Black Widow generating {count} LinkedIn posts...")

        analysis = intelligence_report.get("analysis", "")

        posts = []

        # Generate a mix of post types
        post_types = [
            ("thought_leadership", "AI trends and implications"),
            ("deep_analysis", "Frontier AI developments"),
            ("strategic_insight", "Building AI capabilities")
        ]

        for i in range(min(count, len(post_types))):
            post_type, topic = post_types[i]

            if post_type == "deep_analysis":
                post = self.craft_deep_analysis(topic, intelligence_report)
            else:
                post = self.craft_post(topic, analysis, post_type)

            posts.append(post)

        # Save posts
        date_str = get_date_string()
        output_file = self.output_dir / f"posts_{date_str}.json"
        save_json({
            "posts": posts,
            "generated": get_timestamp()
        }, str(output_file))

        # Also save as markdown
        md_content = "# LinkedIn Content\n\n"
        for i, post in enumerate(posts, 1):
            md_content += f"## Post {i}: {post['topic']}\n"
            md_content += f"**Type:** {post['type']}\n"
            md_content += f"**Length:** {post['character_count']} characters\n\n"
            md_content += post['text']
            md_content += "\n\n---\n\n"

        md_file = self.output_dir / f"posts_{date_str}.md"
        save_markdown(md_content, str(md_file))

        print(f"✅ Generated {len(posts)} LinkedIn posts: {output_file}")

        return {
            "posts": posts,
            "file": str(output_file)
        }


if __name__ == "__main__":
    widow = BlackWidow()

    # Example usage
    mock_report = {
        "analysis": """
        Frontier AI developments:
        - Multi-agent orchestration frameworks emerging
        - RAG systems becoming more sophisticated
        - Evaluation methodologies maturing
        """
    }

    content = widow.generate_content(mock_report, count=2)
    print("\n=== Generated Posts ===")
    for i, post in enumerate(content["posts"], 1):
        print(f"\n{i}. {post['topic']}")
        print(post['text'][:200] + "...")
