"""Thor - X/Twitter Operator.

Thor converts intelligence into reach.
Sharp, authoritative, fast-moving content that makes insights thunder.

Core Principle: "If it matters, make it thunder."
"""

import sys
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.llm import create_agent_llm
from utils.helpers import (
    load_config, save_json, save_markdown, get_timestamp,
    log_event, ensure_dir, get_date_string
)


class Thor:
    """X/Twitter Operator - Converts insights into attention."""

    def __init__(self):
        """Initialize Thor."""
        self.config = load_config()
        self.agent_config = self.config["agents"]["thor"]
        self.llm = create_agent_llm("thor", self.agent_config)
        self.output_dir = Path("content/twitter")
        ensure_dir(str(self.output_dir))

    def craft_tweets(
        self,
        intelligence_report: Dict[str, Any],
        count: int = 5
    ) -> List[Dict[str, str]]:
        """Craft tweets from intelligence report.

        Args:
            intelligence_report: Captain America's research
            count: Number of tweets to generate

        Returns:
            List of tweet dictionaries
        """
        system_prompt = """You are Thor, X/Twitter Operator.

Tone: Sharp, authoritative, fast-moving
Core Principle: "If it matters, make it thunder."

Your tweets must:
- Cut through noise
- Be immediately valuable
- Show technical depth
- Build authority
- Drive engagement

You turn insight into attention.
No fluff. Pure signal.
"""

        analysis = intelligence_report.get("analysis", "")

        prompt = f"""Based on today's AI intelligence, craft {count} high-impact tweets.

Intelligence Report:
{analysis}

Create tweets that:

1. INSIGHT TWEETS (2-3)
   - Share non-obvious insights from the research
   - Technical but accessible
   - Make people think

2. TREND COMMENTARY (1-2)
   - React to what's happening
   - Sharp takes on developments
   - Show you're paying attention

3. EDUCATIONAL (1)
   - Teach something valuable
   - Break down a concept
   - Share a learning

Requirements:
- Max 280 characters each
- Include relevant technical terms
- No hype, just facts and insight
- Each should stand alone
- Hook in first 5 words

Format each as:
---
[tweet text]
---

Generate exactly {count} tweets.
"""

        response = self.llm.generate(
            prompt,
            system_prompt=system_prompt,
            temperature=0.8,
            max_tokens=4000
        )

        # Parse tweets
        tweets = []
        for section in response.split('---'):
            tweet_text = section.strip()
            if tweet_text and len(tweet_text) > 10:
                tweets.append({
                    "text": tweet_text,
                    "created": get_timestamp(),
                    "status": "draft",
                    "length": len(tweet_text)
                })

        # Limit to requested count
        tweets = tweets[:count]

        log_event("thor", "tweets_crafted", {"count": len(tweets)})
        return tweets

    def craft_thread(
        self,
        topic: str,
        intelligence_context: str = ""
    ) -> List[str]:
        """Craft a Twitter thread on a topic.

        Args:
            topic: Thread topic
            intelligence_context: Research context

        Returns:
            List of thread tweets
        """
        system_prompt = """You are Thor crafting a Twitter thread.

Make it:
- Sharp and authoritative
- Technically deep but readable
- Build momentum tweet by tweet
- End with impact

Each tweet must:
- Be self-contained but flow
- Max 280 characters
- Hook the reader
"""

        prompt = f"""Create a Twitter thread about: {topic}

Context:
{intelligence_context}

Structure:
1. Hook tweet - grab attention
2. 3-5 insight tweets - build the argument
3. Conclusion tweet - land the point

Make each tweet punchy and valuable.
No filler. Pure signal.

Format:
1/X: [tweet]
2/X: [tweet]
...
"""

        response = self.llm.generate(
            prompt,
            system_prompt=system_prompt,
            temperature=0.8,
            max_tokens=3000
        )

        # Parse thread
        thread = []
        for line in response.split('\n'):
            if line.strip() and ('/' in line[:5] or line.startswith(tuple('0123456789'))):
                # Extract tweet text after number
                if ':' in line:
                    tweet = line.split(':', 1)[1].strip()
                    thread.append(tweet)

        log_event("thor", "thread_crafted", {"length": len(thread), "topic": topic})
        return thread

    def generate_content(
        self,
        intelligence_report: Dict[str, Any],
        mode: str = "tweets"
    ) -> Dict[str, Any]:
        """Generate Twitter content.

        Args:
            intelligence_report: Research report
            mode: "tweets" or "thread"

        Returns:
            Generated content
        """
        print(f"⚡ Thor generating {mode}...")

        if mode == "tweets":
            tweets = self.craft_tweets(intelligence_report)

            # Save tweets
            date_str = get_date_string()
            output_file = self.output_dir / f"tweets_{date_str}.json"
            save_json({"tweets": tweets, "generated": get_timestamp()}, str(output_file))

            # Also save as markdown for easy review
            md_content = "# Twitter Content\n\n"
            for i, tweet in enumerate(tweets, 1):
                md_content += f"## Tweet {i}\n{tweet['text']}\n\n---\n\n"

            md_file = self.output_dir / f"tweets_{date_str}.md"
            save_markdown(md_content, str(md_file))

            print(f"✅ Generated {len(tweets)} tweets: {output_file}")

            return {
                "type": "tweets",
                "content": tweets,
                "file": str(output_file)
            }

        else:  # thread
            analysis = intelligence_report.get("analysis", "")
            # Extract a topic from analysis
            topic = "AI developments today"

            thread = self.craft_thread(topic, analysis)

            # Save thread
            date_str = get_date_string()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = self.output_dir / f"thread_{timestamp}.json"
            save_json({
                "thread": thread,
                "topic": topic,
                "generated": get_timestamp()
            }, str(output_file))

            print(f"✅ Generated thread ({len(thread)} tweets): {output_file}")

            return {
                "type": "thread",
                "content": thread,
                "file": str(output_file)
            }


if __name__ == "__main__":
    thor = Thor()

    # Example usage
    mock_report = {
        "analysis": """
        TRENDING TOPICS:
        1. AI Agents - Multi-agent systems gaining traction
        2. RAG improvements - Better retrieval methods
        3. LLM evaluation - New benchmarks released
        """
    }

    content = thor.generate_content(mock_report, mode="tweets")
    print("\n=== Generated Content ===")
    for i, tweet in enumerate(content["content"], 1):
        print(f"{i}. {tweet['text'][:100]}...")
