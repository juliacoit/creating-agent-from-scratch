from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

pdf_tool = PDFKnowledgeSource(
    file_paths=["bpf.pdf", "rdc301_2019.pdf", "rdc658_2022.pdf"]
)