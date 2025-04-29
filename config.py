# config.py
from typing import Optional

class Config:
    """Class to store configuration settings for the AI Assistant."""
    def __init__(self):
        self.deepinfra_api_key = "RGcJ063FZOSHIRLKq822sdFSDCxBvXvi"  # DeepInfra API key
        self.api_url = "https://api.deepinfra.com/v1/openai/chat/completions"  # OpenAI-compatible endpoint
        self.serpapi_key = "7a51f9ef1b1bd7a8c8d4a854ef8f0256ff5153221fd8a78b1c13e86182441f93"  # Replace with your SerpAPI key
        self.serpapi_url = "https://serpapi.com/search"
        self.default_model = "mistralai/Mixtral-8x7B-Instruct-v0.1"  # Default model
        self.fallback_model = "meta-llama/Llama-2-7b-chat-hf"  # Fallback model

    def validate(self) -> bool:
        """Validate that API keys are set."""
        return (self.deepinfra_api_key and "RGcJ063FZOSHIRLKq822sdFSDCxBvXvi" not in self.deepinfra_api_key and
                self.serpapi_key and "7a51f9ef1b1bd7a8c8d4a854ef8f0256ff5153221fd8a78b1c13e86182441f93" not in self.serpapi_key)
