"""Captain America - Research & Intelligence.

Captain America protects signal integrity through structured
research sweeps across AI frontiers.
"""

import sys
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import feedparser

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.llm import create_agent_llm
from utils.helpers import (
    load_config, save_json, save_markdown, get_timestamp,
    log_event, ensure_dir, get_date_string
)


class CaptainAmerica:
    """Research & Intelligence Agent."""

    def __init__(self):
        """Initialize Captain America."""
        self.config = load_config()
        self.agent_config = self.config["agents"]["captain_america"]
        self.llm = create_agent_llm("captain_america", self.agent_config)
        self.sources = self.agent_config.get("research_sources", [])
        ensure_dir("intelligence")

    def scrape_hackernews(self) -> List[Dict[str, str]]:
        """Scrape Hacker News front page.

        Returns:
            List of top stories
        """
        try:
            url = "https://news.ycombinator.com/"
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            stories = []
            story_links = soup.find_all('span', class_='titleline')[:10]

            for story in story_links:
                link = story.find('a')
                if link:
                    stories.append({
                        "title": link.text,
                        "url": link.get('href', '')
                    })

            log_event("captain_america", "hn_scraped", {"count": len(stories)})
            return stories
        except Exception as e:
            log_event("captain_america", "hn_error", str(e))
            return []

    def scrape_github_trending(self) -> List[Dict[str, str]]:
        """Scrape GitHub trending repos.

        Returns:
            List of trending repositories
        """
        try:
            url = "https://github.com/trending"
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            repos = []
            articles = soup.find_all('article', class_='Box-row')[:10]

            for article in articles:
                h2 = article.find('h2')
                if h2:
                    link = h2.find('a')
                    if link:
                        repo_name = link.get('href', '').strip('/')
                        description_elem = article.find('p', class_='col-9')
                        description = description_elem.text.strip() if description_elem else ""

                        repos.append({
                            "name": repo_name,
                            "url": f"https://github.com/{repo_name}",
                            "description": description
                        })

            log_event("captain_america", "github_scraped", {"count": len(repos)})
            return repos
        except Exception as e:
            log_event("captain_america", "github_error", str(e))
            return []

    def scrape_arxiv_ai(self) -> List[Dict[str, str]]:
        """Scrape recent ArXiv AI papers.

        Returns:
            List of recent papers
        """
        try:
            url = "http://export.arxiv.org/rss/cs.AI"
            feed = feedparser.parse(url)

            papers = []
            for entry in feed.entries[:10]:
                papers.append({
                    "title": entry.title,
                    "url": entry.link,
                    "summary": entry.summary[:200] + "..."
                })

            log_event("captain_america", "arxiv_scraped", {"count": len(papers)})
            return papers
        except Exception as e:
            log_event("captain_america", "arxiv_error", str(e))
            return []

    def analyze_trends(self, raw_data: Dict[str, List]) -> Dict[str, Any]:
        """Analyze collected data to identify trends.

        Args:
            raw_data: Raw scraped data from all sources

        Returns:
            Analyzed intelligence report
        """
        system_prompt = """You are Captain America, protecting signal integrity.

Core Principle: "Signal over noise. Facts before hype."

Your mission:
- Identify genuine AI trends vs hype
- Extract actionable insights
- Spot emerging patterns
- Flag important developments
- Maintain factual accuracy
"""

        prompt = f"""Analyze today's AI intelligence data and create a structured report.

Data collected:
Hacker News: {len(raw_data.get('hackernews', []))} stories
GitHub Trending: {len(raw_data.get('github', []))} repositories
ArXiv Papers: {len(raw_data.get('arxiv', []))} papers

Raw Data:
{raw_data}

Create an intelligence report with:

1. TRENDING TOPICS (top 5 themes across all sources)
   - What's genuinely trending
   - Why it matters
   - Signal vs noise assessment

2. KEY DEVELOPMENTS
   - Important new releases/papers
   - Breakthrough research
   - Tool/framework updates

3. EMERGING PATTERNS
   - What's gaining momentum
   - Shifting focus areas
   - New capabilities

4. PROTOTYPE OPPORTUNITIES
   - Concrete AI concepts that would make great demos
   - Must be implementable, interesting, and educational
   - Rank by learning value + current relevance

5. CONTENT ANGLES
   - Insights worth sharing on X/Twitter
   - Deeper analysis topics for LinkedIn
   - Newsletter-worthy developments

Format as clear, structured markdown.
"""

        analysis = self.llm.generate(prompt, system_prompt=system_prompt, max_tokens=6000)

        return {
            "timestamp": get_timestamp(),
            "date": get_date_string(),
            "raw_data": raw_data,
            "analysis": analysis,
            "sources_checked": list(raw_data.keys())
        }

    def run_research_sweep(self) -> Dict[str, Any]:
        """Run a complete research sweep.

        Returns:
            Intelligence report
        """
        print("🛡 Captain America starting research sweep...")

        # Collect data from all sources
        raw_data = {
            "hackernews": self.scrape_hackernews(),
            "github": self.scrape_github_trending(),
            "arxiv": self.scrape_arxiv_ai()
        }

        # Analyze and create report
        report = self.analyze_trends(raw_data)

        # Save report
        date_str = get_date_string()
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Save full report as JSON
        json_file = f"intelligence/research_{timestamp_str}.json"
        save_json(report, json_file)

        # Save analysis as markdown
        md_file = f"intelligence/analysis_{date_str}.md"
        save_markdown(report["analysis"], md_file)

        log_event("captain_america", "research_sweep_complete", {
            "json_file": json_file,
            "md_file": md_file,
            "sources": len(raw_data)
        })

        print(f"✅ Research complete: {json_file}")
        return report


if __name__ == "__main__":
    captain = CaptainAmerica()
    report = captain.run_research_sweep()

    print("\n=== Intelligence Report ===")
    print(report["analysis"][:500] + "...")
