import os
import asyncio
import streamlit as st
from src.web_extractor import WebExtractor

class StreamlitWebScraperChat:
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        specific_model_name = os.getenv("MODEL_NAME")
        model_name = specific_model_name if specific_model_name else model_name
        self.web_extractor = WebExtractor(model_name=model_name)

    def process_message(self, message: str) -> str:
        return asyncio.run(self.web_extractor.process_query(message))