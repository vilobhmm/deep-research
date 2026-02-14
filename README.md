# 🛡⚡ Avengers AI Operating System

**A multi-agent AI system that works 24/7 to keep you ahead in AI.**

Six specialized agents collaborate to research trends, build prototypes, create content, and maintain your presence in the AI community.

By the time you wake up, they've already put in a full shift.

---

## 🎯 What This Does

Research what's trending in AI → Build working prototypes → Draft content → Never fall behind.

This is not a content creation tool. **This is a public AI laboratory that compounds learning into artifacts, influence, and authority.**

---

## 🦸 The Team

### 🧠 Iron Man - Chief of Staff
- **Role:** Strategy & Orchestration
- **Principle:** "Execution without direction is noise."
- Sets priorities, delegates tasks, ensures everything compounds toward mastery and visibility

### 🛡 Captain America - Research & Intelligence
- **Role:** Frontier AI Tracking
- **Principle:** "Signal over noise. Facts before hype."
- Monitors: X, Hacker News, GitHub Trending, ArXiv, AI blogs
- Runs 3 research sweeps daily
- Produces structured intelligence reports

### 🔨 Hulk - Prototype Architect
- **Role:** Working Code Demos
- **Principle:** "If you can't run it, you don't understand it."
- Turns complex AI concepts into runnable, playable prototypes
- Every demo must: ✅ Run without errors ✅ Be minimal but complete ✅ Teach interactively
- Outputs to: https://github.com/vilobhmm

### ⚡ Thor - X/Twitter Operator
- **Role:** Attention & Reach
- **Principle:** "If it matters, make it thunder."
- Converts research into high-impact tweets and threads
- Tone: Sharp, authoritative, fast-moving

### 🕷 Black Widow - LinkedIn Authority
- **Role:** Professional Positioning
- **Principle:** "Influence is built, not shouted."
- Creates thought leadership content
- Tone: Composed, high-signal, strategic

### 🎯 Hawkeye - Newsletter Distillation
- **Role:** Weekly Intelligence Digest
- **Principle:** "One shot. No fluff."
- Compiles research + prototypes into clear communication
- Weekly AI digest with genuine insights

---

## 🚀 Quick Start

### 1. Setup

```bash
# Clone the repository
git clone https://github.com/vilobhmm/deep-research.git
cd deep-research

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### 2. Configuration

Edit `config/config.yaml` to customize:
- Agent personalities
- Research sources
- Output preferences
- Scheduling

### 3. Run

**Single daily cycle:**
```bash
python main.py --mode daily
```

**Just research:**
```bash
python main.py --mode research
```

**Build a specific prototype:**
```bash
python main.py --mode prototype --concept "Simple RAG System"
```

**24/7 automated mode:**
```bash
python scheduler.py
```

This runs continuously with:
- Research sweeps: 6am, 12pm, 6pm
- Daily cycle: 4am
- Weekly newsletter: Sunday 8am

---

## 📁 Output Structure

```
intelligence/       # Captain America's research reports
prototypes/        # Hulk's working demos
content/
  ├── twitter/     # Thor's tweets
  ├── linkedin/    # Black Widow's posts
  └── newsletter/  # Hawkeye's digests
logs/             # System logs
```

---

## 🔧 How It Works

### Daily Flow

1. **Captain America** scrapes Hacker News, GitHub Trending, ArXiv
2. **Iron Man** analyzes intelligence and creates strategic plan
3. **Hulk** builds a working prototype based on trending concepts
4. **Thor** crafts tweets from insights
5. **Black Widow** writes LinkedIn thought leadership
6. **Hawkeye** (weekly) compiles everything into newsletter

**Research → Code → Artifact → Attention → Authority → Compounding**

---

## 🛠 Customization

### Adding Research Sources

Edit `config/config.yaml`:
```yaml
captain_america:
  research_sources:
    - "https://your-source.com"
```

### Changing Agent Personalities

Modify agent configurations:
```yaml
thor:
  temperature: 0.8  # More creative
  tone: "your custom tone"
```

### GitHub Integration

Hulk can automatically push prototypes to GitHub (configure in `config/config.yaml`).

---

## 📊 Example Daily Output

**Morning (6am):** Research sweep complete
- 30 HN stories analyzed
- 20 GitHub repos reviewed
- 10 ArXiv papers summarized

**Daily Cycle (4am):**
- ✅ Intelligence report generated
- ✅ Strategic plan created
- ✅ Working prototype: "Tiny RAG System" (runnable demo)
- ✅ 5 tweets drafted
- ✅ 2 LinkedIn posts ready

**Weekly (Sunday):**
- ✅ Newsletter with week's insights

---

## 🎓 Philosophy

### Operating Principles

1. **Learn fast** - Track frontier AI developments
2. **Build immediately** - Turn concepts into working code
3. **Ship publicly** - All prototypes are playable
4. **Document clearly** - Every demo teaches
5. **Repeat relentlessly** - Compound daily

### Quality Standards

**Hulk's Output Must:**
- ✅ Run without errors
- ✅ Be minimal but complete
- ✅ Teach the concept interactively
- ✅ Be modifiable
- ✅ Include clear documentation

**Content Must:**
- ✅ Be high-signal, not noise
- ✅ Demonstrate expertise
- ✅ Provide genuine value
- ✅ Build authority

---

## 🤝 Contributing

This is a personal AI lab system, but feel free to:
- Fork and customize for your needs
- Submit improvements
- Share your agent modifications

---

## 📝 License

MIT License - Use freely, build publicly

---

## 🔗 Links

- **GitHub:** https://github.com/vilobhmm
- **Prototypes:** https://github.com/vilobhmm (Hulk's demos)

---

## ⚠️ Requirements

- Python 3.8+
- Anthropic API key (Claude)
- Internet connection for research scraping

---

## 💡 Tips

1. **Run scheduler in tmux/screen** for 24/7 operation
2. **Review outputs each morning** - agents draft, you approve/edit
3. **Customize agent prompts** in agent files for your voice
4. **Start with daily mode** before going full 24/7
5. **Monitor logs/** for debugging

---

**Six agents. One system. Continuous visible output.**

This is building an AI laboratory in public.

🛡⚡
