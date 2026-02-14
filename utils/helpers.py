"""Helper utilities for Avengers AI Operating System."""

import os
import json
import yaml
from datetime import datetime
from typing import Any, Dict, List
from pathlib import Path


def load_config(config_path: str = "config/config.yaml") -> Dict[str, Any]:
    """Load system configuration.

    Args:
        config_path: Path to config file

    Returns:
        Configuration dictionary
    """
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def save_json(data: Any, filepath: str) -> None:
    """Save data as JSON.

    Args:
        data: Data to save
        filepath: Path to save to
    """
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, default=str)


def load_json(filepath: str) -> Any:
    """Load JSON data.

    Args:
        filepath: Path to load from

    Returns:
        Loaded data
    """
    with open(filepath, 'r') as f:
        return json.load(f)


def save_markdown(content: str, filepath: str) -> None:
    """Save content as Markdown.

    Args:
        content: Markdown content
        filepath: Path to save to
    """
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)


def get_timestamp() -> str:
    """Get current timestamp string.

    Returns:
        ISO format timestamp
    """
    return datetime.now().isoformat()


def get_date_string() -> str:
    """Get current date string.

    Returns:
        Date in YYYY-MM-DD format
    """
    return datetime.now().strftime("%Y-%m-%d")


def setup_logging(log_dir: str = "logs") -> None:
    """Set up logging directory.

    Args:
        log_dir: Directory for logs
    """
    Path(log_dir).mkdir(parents=True, exist_ok=True)


def log_event(agent: str, event: str, data: Any = None, log_dir: str = "logs") -> None:
    """Log an event.

    Args:
        agent: Agent name
        event: Event description
        data: Optional event data
        log_dir: Log directory
    """
    timestamp = get_timestamp()
    log_entry = {
        "timestamp": timestamp,
        "agent": agent,
        "event": event,
        "data": data
    }

    log_file = Path(log_dir) / f"{agent}_{get_date_string()}.jsonl"
    with open(log_file, 'a') as f:
        f.write(json.dumps(log_entry, default=str) + "\n")


def read_file(filepath: str) -> str:
    """Read file contents.

    Args:
        filepath: Path to file

    Returns:
        File contents
    """
    with open(filepath, 'r') as f:
        return f.read()


def ensure_dir(dirpath: str) -> None:
    """Ensure directory exists.

    Args:
        dirpath: Directory path
    """
    Path(dirpath).mkdir(parents=True, exist_ok=True)


def list_files(directory: str, pattern: str = "*") -> List[str]:
    """List files in directory.

    Args:
        directory: Directory to search
        pattern: File pattern

    Returns:
        List of file paths
    """
    return [str(p) for p in Path(directory).glob(pattern)]
