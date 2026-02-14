# 🛡⚡ AVENGERS AI OPERATING SYSTEM

**Architecture Documentation**

---

## System Overview

Six agents. Clear ownership. No overlap. Continuous output.

This is a public AI lab that compounds learning into artifacts, influence, and authority.

---

## 🧠 Iron Man — Chief of Staff (Strategy & Orchestration)

### Role
Central command. Primary interface. Sets direction. Prioritizes. Delegates.

### Responsibilities
- Strategic planning
- Task routing
- Sprint definition
- Long-term vision alignment
- Performance tracking
- Quality control

### Core Principle
**"Execution without direction is noise."**

Iron Man ensures everything shipped compounds toward mastery, visibility, and leverage.

### Technical Implementation
- **File:** `agents/iron_man.py`
- **Model:** Claude Sonnet 4.5
- **Temperature:** 0.7
- **Key Functions:**
  - `plan_daily_sprint()` - Create strategic daily plan
  - `review_output()` - Quality control for agent outputs
  - `generate_status_report()` - System status updates

---

## 🛡 Captain America — Research & Intelligence

### Role
Protects signal integrity. Runs structured research sweeps.

### Responsibilities
- Frontier AI tracking
- Model releases monitoring
- Benchmark changes
- Tool ecosystem updates
- Emerging research analysis

### Research Sources
- X (Twitter)
- Hacker News
- GitHub Trending
- ArXiv (cs.AI)
- Google AI Blog
- Official AI lab updates

### Schedule
3x daily sweeps:
- 06:00 - Morning sweep
- 12:00 - Midday sweep
- 18:00 - Evening sweep

### Core Principle
**"Signal over noise. Facts before hype."**

Filters chaos into verified insight.

### Technical Implementation
- **File:** `agents/captain_america.py`
- **Model:** Claude Sonnet 4.5
- **Temperature:** 0.3 (precision for analysis)
- **Key Functions:**
  - `scrape_hackernews()` - HN top stories
  - `scrape_github_trending()` - Trending repos
  - `scrape_arxiv_ai()` - Recent papers
  - `analyze_trends()` - LLM-powered analysis
  - `run_research_sweep()` - Complete sweep cycle

### Output Format
- JSON reports: `intelligence/research_TIMESTAMP.json`
- Markdown analysis: `intelligence/analysis_DATE.md`

---

## ⚡ Thor — X / Twitter Operator

### Role
Converts intelligence into reach. Crafts high-impact content.

### Responsibilities
- Trend positioning
- Insight amplification
- Narrative shaping
- Rapid commentary

### Content Types
- Single tweets
- Threads
- Quote tweets
- Timely reactions

### Tone
Sharp, authoritative, fast-moving.

### Core Principle
**"If it matters, make it thunder."**

Turns insight into attention.

### Technical Implementation
- **File:** `agents/thor.py`
- **Model:** Claude Sonnet 4.5
- **Temperature:** 0.8 (creative for engagement)
- **Key Functions:**
  - `craft_tweets()` - Generate single tweets
  - `craft_thread()` - Create threaded content
  - `generate_content()` - Main content generation

### Output Format
- JSON: `content/twitter/tweets_DATE.json`
- Markdown: `content/twitter/tweets_DATE.md`

### Guidelines
- Max 280 characters per tweet
- Max 10 tweets per day
- Hook in first 5 words
- No hype, pure insight

---

## 🕷 Black Widow — LinkedIn Authority Architect

### Role
Transforms intelligence into professional positioning. Plays the long game.

### Responsibilities
- Thought leadership posts
- Deep analysis breakdowns
- Career positioning
- Founder/researcher credibility building
- Strategic commentary

### Tone
Composed, high-signal, strategic.

### Core Principle
**"Influence is built, not shouted."**

Converts knowledge into reputation capital.

### Technical Implementation
- **File:** `agents/black_widow.py`
- **Model:** Claude Sonnet 4.5
- **Temperature:** 0.6
- **Key Functions:**
  - `craft_post()` - Single LinkedIn posts
  - `craft_deep_analysis()` - Long-form analysis
  - `generate_content()` - Content generation

### Output Format
- JSON: `content/linkedin/posts_DATE.json`
- Markdown: `content/linkedin/posts_DATE.md`

### Guidelines
- 800-1200 characters per post (LinkedIn sweet spot)
- Max 5 posts per week
- First 2 lines critical (feed preview)
- Demonstrate depth without jargon

---

## 🔨 Hulk — Prototype Architect & GitHub Executor

### Role
Turns complex AI concepts into working, playable artifacts.

### Critical Requirements
**NOT half-baked code. NOT theory dumps. If it goes to GitHub — it runs.**

### Responsibilities
- Convert daily AI learning into runnable code
- Build minimal but complete prototypes
- Create demos (CLI, UI, notebooks)
- Write clean, structured code
- Maintain documentation and README
- Create new repositories when needed
- Ship consistently

### Output Standard
Every prototype MUST:
- ✅ Run without errors
- ✅ Be minimal but complete
- ✅ Teach the concept interactively
- ✅ Be modifiable
- ✅ Include clear documentation

### Example Prototypes
- Tiny RAG system
- LoRA fine-tuning demo
- RLHF simulation pipeline
- Evaluation harness
- Agent loop implementation
- Self-reflection / critique system
- World model toy environment

### Core Principle
**"If you can't run it, you don't understand it."**

Builds understanding through execution.

### Technical Implementation
- **File:** `agents/hulk.py`
- **Model:** Claude Sonnet 4.5
- **Temperature:** 0.5
- **Key Functions:**
  - `design_prototype()` - Create design spec
  - `generate_code()` - Generate working code
  - `create_prototype()` - Full prototype creation
  - `test_prototype()` - Validate it works

### Output Structure
```
prototypes/
  └── concept_name_DATE/
      ├── main.py
      ├── README.md
      ├── requirements.txt
      ├── example_usage.py
      └── prototype_metadata.json
```

### GitHub Integration
All prototypes pushed to: https://github.com/vilobhmm

---

## 🎯 Hawkeye — Newsletter & Intelligence Distillation

### Role
Filters everything into clarity. Converts complexity into communication.

### Responsibilities
- Weekly AI digest
- Research summaries
- Prototype highlights
- Signal-only breakdowns
- Clean narrative flow

### Core Principle
**"One shot. No fluff."**

Turns complexity into clarity.

### Technical Implementation
- **File:** `agents/hawkeye.py`
- **Model:** Claude Sonnet 4.5
- **Temperature:** 0.5
- **Key Functions:**
  - `gather_weekly_intelligence()` - Collect week's data
  - `create_newsletter()` - Generate newsletter
  - `generate_newsletter()` - Full workflow

### Output Format
- Markdown: `content/newsletter/newsletter_WEEK.md`
- JSON: `content/newsletter/newsletter_WEEK.json`

### Newsletter Sections
1. Week's Top AI Developments
2. Research Highlights
3. Prototypes Built This Week
4. Signal vs Noise
5. What to Watch
6. Learning of the Week

### Schedule
Weekly - Sunday 8:00 AM

---

## ⚙ System Flow

```
1. Captain America gathers frontier intelligence
   ↓
2. Iron Man prioritizes and assigns
   ↓
3. Hulk builds working prototypes
   ↓
4. Thor amplifies on X
   ↓
5. Black Widow builds authority on LinkedIn
   ↓
6. Hawkeye distills into newsletter
```

**Research → Code → Artifact → Attention → Authority → Compounding**

---

## 📈 Operating Philosophy

### Core Principles
1. **Learn fast** - Track AI frontier daily
2. **Build immediately** - Concepts to code
3. **Ship publicly** - Everything visible
4. **Document clearly** - Teach while building
5. **Repeat relentlessly** - Compound effect

### Quality Bar

**For Code (Hulk):**
- Must run without errors
- Minimal but complete
- Educational value
- Interactive/playable
- Well documented

**For Content (Thor, Black Widow, Hawkeye):**
- High signal-to-noise ratio
- Demonstrates expertise
- Genuine value
- Authority building
- No hype

### Workflow Automation

**Daily (4:00 AM):**
```python
research() → plan() → prototype() → content() → save()
```

**3x Daily (6am, 12pm, 6pm):**
```python
research_sweep() → update_intelligence()
```

**Weekly (Sunday 8am):**
```python
gather_weekly() → newsletter() → publish()
```

---

## 🔧 Technical Architecture

### Directory Structure
```
deep-research/
├── agents/              # Agent implementations
│   ├── iron_man.py
│   ├── captain_america.py
│   ├── hulk.py
│   ├── thor.py
│   ├── black_widow.py
│   └── hawkeye.py
├── utils/              # Shared utilities
│   ├── llm.py         # Claude API interface
│   └── helpers.py     # Common functions
├── config/            # Configuration
│   └── config.yaml
├── intelligence/      # Research outputs
├── prototypes/        # Working demos
├── content/          # Generated content
│   ├── twitter/
│   ├── linkedin/
│   └── newsletter/
├── logs/             # System logs
├── main.py           # Main orchestrator
├── scheduler.py      # 24/7 automation
└── requirements.txt
```

### Dependencies
- **anthropic** - Claude API
- **requests** - HTTP requests
- **beautifulsoup4** - Web scraping
- **feedparser** - RSS/Atom feeds
- **pyyaml** - Config management
- **schedule** - Task scheduling

### API Usage
- **Primary:** Anthropic Claude API
- **Models:** Claude Sonnet 4.5
- **Temperature:** Varies by agent (0.3-0.8)

---

## 🚀 Deployment

### Development
```bash
python main.py --mode daily
```

### Production (24/7)
```bash
# In tmux/screen session
python scheduler.py
```

### Docker (Optional)
```bash
docker build -t avengers-ai .
docker run -d --env-file .env avengers-ai
```

---

## 📊 Monitoring

### Logs
All events logged to: `logs/AGENT_DATE.jsonl`

### Metrics Tracked
- Research sources checked
- Prototypes created
- Content pieces generated
- Execution times
- Errors/failures

### Review Points
- Morning: Check overnight outputs
- Weekly: Review all content before publishing
- Monthly: System performance analysis

---

## 🔐 Security & Privacy

### API Keys
- Store in `.env` file (never commit)
- Use environment variables

### Data
- All outputs local first
- Manual review before publishing
- No automatic posting (draft only)

### Web Scraping
- Respect robots.txt
- Rate limiting implemented
- User-agent headers set

---

## 🎯 Success Metrics

### Daily
- [ ] Intelligence report generated
- [ ] Working prototype created
- [ ] Content drafted (Twitter + LinkedIn)
- [ ] All outputs saved

### Weekly
- [ ] Newsletter compiled
- [ ] 3-5 working prototypes
- [ ] 20-30 content pieces drafted

### Monthly
- [ ] System uptime > 95%
- [ ] All prototypes runnable
- [ ] Consistent public output

---

## 🔄 Iteration & Improvement

### Agent Tuning
- Adjust temperatures for output quality
- Refine system prompts
- Add new research sources

### Feature Additions
- GitHub auto-commit
- Social media auto-posting
- Telegram notifications
- Performance analytics dashboard

### Quality Improvements
- Better error handling
- Prototype testing automation
- Content quality scoring

---

**Six agents. One system. Continuous visible output.**

This is not content creation. **This is building an AI laboratory in public.**

🛡⚡
