"""LLM interface using Anthropic's Claude API."""

import os
from typing import Optional, Dict, Any
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()


class ClaudeInterface:
    """Interface for interacting with Claude API."""

    def __init__(self, model: str = "claude-sonnet-4-5-20250929", temperature: float = 0.7):
        """Initialize Claude interface.

        Args:
            model: Claude model to use
            temperature: Sampling temperature (0.0-1.0)
        """
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")

        self.client = Anthropic(api_key=self.api_key)
        self.model = model
        self.temperature = temperature

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: int = 4096
    ) -> str:
        """Generate text using Claude.

        Args:
            prompt: User prompt
            system_prompt: Optional system prompt
            temperature: Override default temperature
            max_tokens: Maximum tokens to generate

        Returns:
            Generated text
        """
        messages = [{"role": "user", "content": prompt}]

        kwargs: Dict[str, Any] = {
            "model": self.model,
            "max_tokens": max_tokens,
            "temperature": temperature if temperature is not None else self.temperature,
            "messages": messages
        }

        if system_prompt:
            kwargs["system"] = system_prompt

        response = self.client.messages.create(**kwargs)
        return response.content[0].text

    def generate_structured(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        output_format: str = "json",
        temperature: Optional[float] = None,
        max_tokens: int = 4096
    ) -> str:
        """Generate structured output.

        Args:
            prompt: User prompt
            system_prompt: Optional system prompt
            output_format: Desired output format (json, yaml, markdown, etc.)
            temperature: Override default temperature
            max_tokens: Maximum tokens to generate

        Returns:
            Generated structured text
        """
        structured_prompt = f"{prompt}\n\nProvide your response in {output_format} format."
        return self.generate(structured_prompt, system_prompt, temperature, max_tokens)


def create_agent_llm(agent_name: str, config: Dict[str, Any]) -> ClaudeInterface:
    """Create LLM interface for a specific agent.

    Args:
        agent_name: Name of the agent
        config: Agent configuration

    Returns:
        Configured ClaudeInterface
    """
    return ClaudeInterface(
        model=config.get("model", "claude-sonnet-4-5-20250929"),
        temperature=config.get("temperature", 0.7)
    )
