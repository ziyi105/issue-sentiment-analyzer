# services/cluster_summarizer.py

from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from typing import List

class Summarizer:
    def __init__(self, model_name: str = "gemma:2b"):
        self.llm = Ollama(model=model_name)
        self.prompt_template = PromptTemplate.from_template(
            "Summarize the main opinion expressed in the following comments:\n\n{comments}\n\nSummary:"
        )

    def summarize_cluster(self, comments: List[str]) -> str:
        """Generates a summary of a list of comments (a cluster)."""
        joined = "\n".join(comments)
        prompt = self.prompt_template.format(comments=joined)
        return self.llm.invoke(prompt)
