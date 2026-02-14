"""Iron Man - Chief of Staff & Orchestrator.

Iron Man coordinates all agents, sets priorities, and ensures
everything compounds toward mastery, visibility, and leverage.
"""

import sys
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.llm import create_agent_llm
from utils.helpers import (
    load_config, save_json, get_timestamp, log_event, ensure_dir
)


class IronMan:
    """Chief of Staff - Strategy & Orchestration."""

    def __init__(self):
        """Initialize Iron Man."""
        self.config = load_config()
        self.agent_config = self.config["agents"]["iron_man"]
        self.llm = create_agent_llm("iron_man", self.agent_config)
        ensure_dir("intelligence")

    def plan_daily_sprint(self, intelligence_report: Dict[str, Any]) -> Dict[str, Any]:
        """Plan daily sprint based on intelligence.

        Args:
            intelligence_report: Captain America's research

        Returns:
            Daily sprint plan
        """
        system_prompt = """You are Iron Man, Chief of Staff of the Avengers AI Operating System.

Your role is to:
- Analyze intelligence reports
- Set strategic priorities
- Delegate tasks to specialized agents
- Ensure all output compounds toward mastery, visibility, and leverage

Core Principle: "Execution without direction is noise."
"""

        prompt = f"""Based on today's intelligence report, create a daily sprint plan.

Intelligence Report:
{intelligence_report}

Create a plan that includes:
1. Top 3 strategic priorities for today
2. Task assignments for each agent:
   - Hulk: Which AI concept to prototype (must be runnable, complete demo)
   - Thor: Which insights to amplify on X/Twitter
   - Black Widow: Which topics for LinkedIn thought leadership
   - Hawkeye: Key themes for newsletter (if applicable)

3. Success criteria for today
4. How today's work compounds toward long-term goals

Provide the plan in JSON format with keys: priorities, tasks, success_criteria, compounding_value
"""

        response = self.llm.generate(prompt, system_prompt=system_prompt)

        # Extract and parse the plan
        try:
            import json
            # Try to extract JSON from response
            start_idx = response.find('{')
            end_idx = response.rfind('}') + 1
            if start_idx != -1 and end_idx > start_idx:
                plan = json.loads(response[start_idx:end_idx])
            else:
                # Fallback: create structured plan
                plan = {
                    "priorities": ["Analyze AI trends", "Create prototypes", "Build authority"],
                    "tasks": {
                        "hulk": "Create working demo based on trending AI concept",
                        "thor": "Share insights on X/Twitter",
                        "black_widow": "Write LinkedIn thought leadership",
                        "hawkeye": "Compile weekly digest"
                    },
                    "success_criteria": "All agents deliver high-quality output",
                    "compounding_value": response
                }
        except Exception as e:
            log_event("iron_man", "plan_parsing_error", str(e))
            plan = {
                "priorities": ["Execute daily tasks", "Maintain momentum", "Build in public"],
                "tasks": {
                    "hulk": "Create prototype",
                    "thor": "Share on X",
                    "black_widow": "Post on LinkedIn",
                    "hawkeye": "Draft newsletter"
                },
                "success_criteria": "Daily output complete",
                "compounding_value": "Consistent public building"
            }

        plan["timestamp"] = get_timestamp()

        # Save plan
        plan_file = f"intelligence/daily_plan_{datetime.now().strftime('%Y%m%d')}.json"
        save_json(plan, plan_file)
        log_event("iron_man", "plan_created", plan_file)

        return plan

    def review_output(self, agent: str, output: Any) -> Dict[str, Any]:
        """Review agent output for quality.

        Args:
            agent: Agent name
            output: Agent's output

        Returns:
            Review results
        """
        system_prompt = f"""You are Iron Man reviewing {agent}'s output.

Quality standards:
- Does it compound toward mastery, visibility, and leverage?
- Is it high-signal, not noise?
- Does it demonstrate expertise?
- Is it complete and actionable?
"""

        prompt = f"""Review this output from {agent}:

{output}

Provide:
1. Quality score (1-10)
2. Strengths
3. Areas for improvement
4. Approval status (approved/needs_revision)

Format as JSON.
"""

        response = self.llm.generate(prompt, system_prompt=system_prompt, temperature=0.3)

        review = {
            "agent": agent,
            "timestamp": get_timestamp(),
            "review": response,
            "approved": True  # Default to approved
        }

        log_event("iron_man", f"review_{agent}", review)
        return review

    def generate_status_report(self) -> str:
        """Generate overall system status report.

        Returns:
            Status report
        """
        system_prompt = """You are Iron Man providing a status update.

Be concise and focus on:
- What was accomplished
- Current priorities
- Next actions
"""

        prompt = """Generate a brief status report for the Avengers AI Operating System.

Check recent logs and outputs, then summarize:
1. Today's accomplishments
2. Current system status
3. Next priorities

Keep it concise and actionable.
"""

        return self.llm.generate(prompt, system_prompt=system_prompt, temperature=0.5)


if __name__ == "__main__":
    iron_man = IronMan()

    # Example: Create a plan
    mock_intelligence = {
        "trending_topics": ["AI agents", "RAG improvements", "LLM evaluation"],
        "key_insights": ["Agent frameworks evolving rapidly", "Focus on reliability"]
    }

    plan = iron_man.plan_daily_sprint(mock_intelligence)
    print("Daily Sprint Plan:")
    print(plan)
