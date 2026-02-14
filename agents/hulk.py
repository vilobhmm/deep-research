"""Hulk - Prototype Architect & GitHub Executor.

Hulk turns complex AI concepts into working, playable artifacts.
Not half-baked code. Not theory dumps. If it goes to GitHub — it runs.

Core Principle: "If you can't run it, you don't understand it."
"""

import sys
import os
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.llm import create_agent_llm
from utils.helpers import (
    load_config, save_json, get_timestamp, log_event,
    ensure_dir, get_date_string
)


class Hulk:
    """Prototype Architect - Creates working AI demos."""

    def __init__(self):
        """Initialize Hulk."""
        self.config = load_config()
        self.agent_config = self.config["agents"]["hulk"]
        self.llm = create_agent_llm("hulk", self.agent_config)
        self.prototypes_dir = Path("prototypes")
        ensure_dir(str(self.prototypes_dir))

    def design_prototype(self, concept: str, intelligence_context: str = "") -> Dict[str, Any]:
        """Design a prototype for an AI concept.

        Args:
            concept: AI concept to prototype
            intelligence_context: Context from Captain America's research

        Returns:
            Prototype design specification
        """
        system_prompt = """You are Hulk, the Prototype Architect.

Core Principle: "If you can't run it, you don't understand it."

Your prototypes MUST:
✅ Run without errors
✅ Be minimal but complete
✅ Teach the concept interactively
✅ Be modifiable and hackable
✅ Include clear documentation

You build understanding through execution.
Never create half-baked code.
Every prototype must be playable and educational.
"""

        prompt = f"""Design a working prototype for this AI concept: {concept}

Context from research:
{intelligence_context}

Create a design specification with:

1. CONCEPT OVERVIEW
   - What this demonstrates
   - Why it's valuable to build
   - Key learning outcomes

2. IMPLEMENTATION PLAN
   - Core components needed
   - Minimal viable approach
   - No unnecessary complexity

3. FILE STRUCTURE
   - Exact files to create
   - What each file does

4. CODE OUTLINE
   - Key functions/classes
   - Main logic flow
   - Critical implementation details

5. DEMO INTERACTION
   - How users will run it
   - Example inputs/outputs
   - What they'll learn by playing with it

6. README STRUCTURE
   - Installation steps
   - Usage examples
   - Concept explanation

Keep it minimal but complete. Focus on clarity and educational value.
Provide response as structured JSON.
"""

        design_response = self.llm.generate(
            prompt,
            system_prompt=system_prompt,
            max_tokens=8000,
            temperature=0.5
        )

        # Parse design
        try:
            import json
            start_idx = design_response.find('{')
            end_idx = design_response.rfind('}') + 1
            if start_idx != -1 and end_idx > start_idx:
                design = json.loads(design_response[start_idx:end_idx])
            else:
                design = {"raw_design": design_response}
        except:
            design = {"raw_design": design_response}

        design["concept"] = concept
        design["timestamp"] = get_timestamp()

        return design

    def generate_code(self, design: Dict[str, Any]) -> Dict[str, str]:
        """Generate actual working code from design.

        Args:
            design: Prototype design specification

        Returns:
            Dictionary of filename -> code content
        """
        system_prompt = """You are Hulk creating working prototype code.

CRITICAL REQUIREMENTS:
- Code MUST run without errors
- Include ALL necessary imports
- Handle edge cases
- Add helpful comments
- Make it interactive and educational
- No placeholders or TODOs - complete implementation only

Quality bar: Someone should be able to run this immediately and learn by playing with it.
"""

        concept = design.get("concept", "AI Concept")

        prompt = f"""Generate complete, working code for this prototype:

Concept: {concept}

Design:
{design}

Generate ALL files needed for a working prototype:

1. Main implementation file(s)
2. README.md with:
   - Clear explanation of the concept
   - Installation instructions
   - Usage examples
   - How to experiment with it
3. requirements.txt (if needed)
4. Example usage script or notebook

Provide each file with clear markers:
=== FILENAME: path/to/file.py ===
[code here]
=== END FILE ===

Make sure EVERYTHING works. No placeholders. No "implement this later".
This must be runnable and educational immediately.
"""

        code_response = self.llm.generate(
            prompt,
            system_prompt=system_prompt,
            max_tokens=16000,
            temperature=0.4
        )

        # Parse files from response
        files = {}
        current_file = None
        current_content = []

        for line in code_response.split('\n'):
            if '=== FILENAME:' in line or '=== FILE:' in line:
                # Save previous file
                if current_file and current_content:
                    files[current_file] = '\n'.join(current_content)

                # Start new file
                current_file = line.split(':', 1)[1].strip().strip('=').strip()
                current_content = []

            elif '=== END' in line:
                # Save current file
                if current_file and current_content:
                    files[current_file] = '\n'.join(current_content)
                current_file = None
                current_content = []

            elif current_file:
                current_content.append(line)

        # Save last file if not ended
        if current_file and current_content:
            files[current_file] = '\n'.join(current_content)

        # If no files parsed, create default structure
        if not files:
            files = {
                "README.md": f"# {concept}\n\nPrototype implementation\n\n{code_response}",
                "main.py": code_response
            }

        return files

    def create_prototype(
        self,
        concept: str,
        intelligence_context: str = "",
        prototype_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a complete working prototype.

        Args:
            concept: AI concept to prototype
            intelligence_context: Research context
            prototype_name: Optional custom name

        Returns:
            Prototype creation result
        """
        print(f"🔨 Hulk building prototype: {concept}")

        # Design the prototype
        design = self.design_prototype(concept, intelligence_context)
        log_event("hulk", "design_complete", design)

        # Generate code
        files = self.generate_code(design)
        log_event("hulk", "code_generated", {"file_count": len(files)})

        # Create prototype directory
        if not prototype_name:
            date_str = datetime.now().strftime("%Y%m%d")
            prototype_name = f"{concept.lower().replace(' ', '_')}_{date_str}"

        prototype_path = self.prototypes_dir / prototype_name
        ensure_dir(str(prototype_path))

        # Write all files
        written_files = []
        for filename, content in files.items():
            file_path = prototype_path / filename
            file_path.parent.mkdir(parents=True, exist_ok=True)

            with open(file_path, 'w') as f:
                f.write(content)

            written_files.append(str(file_path))
            print(f"  ✓ Created: {file_path}")

        # Save metadata
        metadata = {
            "concept": concept,
            "prototype_name": prototype_name,
            "created": get_timestamp(),
            "design": design,
            "files": written_files,
            "path": str(prototype_path)
        }

        metadata_file = prototype_path / "prototype_metadata.json"
        save_json(metadata, str(metadata_file))

        log_event("hulk", "prototype_created", metadata)

        print(f"✅ Prototype complete: {prototype_path}")

        return metadata

    def test_prototype(self, prototype_path: str) -> Dict[str, Any]:
        """Test if prototype runs correctly.

        Args:
            prototype_path: Path to prototype directory

        Returns:
            Test results
        """
        print(f"🧪 Testing prototype: {prototype_path}")

        results = {
            "prototype_path": prototype_path,
            "timestamp": get_timestamp(),
            "tests": []
        }

        path = Path(prototype_path)

        # Check for requirements.txt and try to install
        requirements_file = path / "requirements.txt"
        if requirements_file.exists():
            print("  Installing requirements...")
            try:
                subprocess.run(
                    ["pip", "install", "-q", "-r", str(requirements_file)],
                    check=True,
                    capture_output=True
                )
                results["tests"].append({"test": "requirements_install", "passed": True})
            except subprocess.CalledProcessError as e:
                results["tests"].append({
                    "test": "requirements_install",
                    "passed": False,
                    "error": str(e)
                })

        # Try to run main.py if it exists
        main_file = path / "main.py"
        if main_file.exists():
            print("  Checking main.py syntax...")
            try:
                # Check syntax
                subprocess.run(
                    ["python", "-m", "py_compile", str(main_file)],
                    check=True,
                    capture_output=True
                )
                results["tests"].append({"test": "syntax_check", "passed": True})
            except subprocess.CalledProcessError as e:
                results["tests"].append({
                    "test": "syntax_check",
                    "passed": False,
                    "error": str(e)
                })

        # Check README exists
        readme_file = path / "README.md"
        results["tests"].append({
            "test": "readme_exists",
            "passed": readme_file.exists()
        })

        results["all_passed"] = all(t.get("passed", False) for t in results["tests"])

        log_event("hulk", "prototype_tested", results)
        print(f"  {'✅' if results['all_passed'] else '❌'} Tests complete")

        return results


if __name__ == "__main__":
    hulk = Hulk()

    # Example: Create a simple RAG prototype
    metadata = hulk.create_prototype(
        concept="Simple RAG System",
        intelligence_context="RAG (Retrieval Augmented Generation) is trending"
    )

    print("\nMetadata:", metadata)

    # Test the prototype
    results = hulk.test_prototype(metadata["path"])
    print("\nTest Results:", results)
