# MCP Server for Research Assistant
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from llm.phi_model import generate_answer
from mcp.server import MCPServer
from retrieval.retriever import retrieve
from retrieval.github_retriever import retrieve_github
from router.source_router import choose_source
from llm.phi_model import compare_documents
from retrieval.pdf_retriever import retrieve_pdf
from router.llm_router import choose_source_llm
from retrieval.repo_retriever import retrieve_repo

mcp = MCPServer("Research Assistant")

@mcp.tool()
def get_project_info() -> str:
    """
    Returns basic project information.
    """
    return "MCP-Powered Research Assistant Version 1"

@mcp.tool()
def summarize_text(text: str) -> str:
    """
    Returns a short summary of the provided text.
    """
    return text[:1000]

@mcp.tool()
def compare_texts(text1: str, text2: str) -> str:
    """
    Compares two texts.
    """
    if text1 == text2:
        return "Both texts are identical."

    return f"Text 1 Length: {len(text1)}, Text 2 Length: {len(text2)}"

import os

@mcp.tool()
def list_papers() -> list[str]:
    """
    Returns all available PDF files.
    """
    return [
        file for file in os.listdir("data/papers")

        if file.endswith(".pdf")

    ]

@mcp.tool()
def read_paper(pdf_name: str) -> str:
    """
    Reads the selected PDF and returns its content.
    """
    from pypdf import PdfReader

    reader = PdfReader(f"data/papers/{pdf_name}")

    text = ""

    for page in reader.pages:
        extracted_text = page.extract_text()

        if extracted_text:
            text += extracted_text + "\n"

    return text[:10000]

@mcp.resource("research://note")
def research_note() -> str:
    with open(
        "data/notes/research_note.txt",
        "r",
        encoding="utf-8"
    ) as file:
        return file.read()

from pypdf import PdfReader


@mcp.resource("research://paper1")
def paper1_resource() -> str:
    reader = PdfReader("data/papers/paper1.pdf")

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text[:10000]

@mcp.tool()
def summarize_paper(pdf_name: str) -> str:
    """
    Returns a summary of the selected paper.
    """

    from pypdf import PdfReader

    reader = PdfReader(f"data/papers/{pdf_name}")

    text = ""

    for page in reader.pages:
        extracted_text = page.extract_text()

        if extracted_text:
            text += extracted_text + "\n"

    return text[:1000]

@mcp.tool()
def compare_papers(
    pdf1: str,
    pdf2: str
) -> str:
    """
    Compares two papers using Phi-4-mini.
    """

    from pypdf import PdfReader

    text1 = ""
    text2 = ""

    reader1 = PdfReader(f"data/papers/{pdf1}")

    for page in reader1.pages:

        page_text = page.extract_text()

        if page_text:
            text1 += page_text

    reader2 = PdfReader(f"data/papers/{pdf2}")

    for page in reader2.pages:

        page_text = page.extract_text()

        if page_text:
            text2 += page_text

    return compare_documents(
        text1[:5000],
        text2[:5000]
    )

@mcp.tool()
def search_paper(pdf_name: str, query: str) -> str:
    """
    Searches for a keyword inside the selected PDF.
    """

    from pypdf import PdfReader

    reader = PdfReader(f"data/papers/{pdf_name}")

    matches = []

    for page_num, page in enumerate(reader.pages, start=1):

        page_text = page.extract_text()

        if page_text and query.lower() in page_text.lower():

            start_index = page_text.lower().find(query.lower())

            snippet_start = max(0, start_index - 100)
            snippet_end = min(len(page_text), start_index + 300)

            snippet = page_text[snippet_start:snippet_end]

            matches.append(
                    f"\nPage {page_num}:\n{snippet}\n"
            )

    if not matches:
        return f"No matches found for '{query}' in {pdf_name}"

    return "\n\n".join(matches[:5])

@mcp.tool()
def ask_paper(pdf_name: str, question: str) -> str:
    """
    Answers a question using ChromaDB retrieval and Phi-4-mini.
    """

    try:

        retrieved_chunks = retrieve_pdf(
            query=question,
            pdf_name=pdf_name
        )
        context = "\n\n".join(retrieved_chunks)

        answer = generate_answer(
            context=context,
            question=question
        )

        return answer

    except Exception as e:

        return f"Ask Paper Error: {str(e)}"

@mcp.tool()
def ask_github(question: str) -> str:
    """
    Answers a question using GitHub notes.
    """

    try:

        retrieved_chunks = retrieve_github(question)

        context = "\n\n".join(retrieved_chunks)

        answer = generate_answer(
            context=context,
            question=question
        )

        return answer

    except Exception as e:

        return f"Ask GitHub Error: {str(e)}"

@mcp.tool()
def ask_anything(question: str) -> str:
    """
    Automatically selects the best source and answers the question.
    """

    try:

        source = choose_source_llm(question)

        if source == "github":

            retrieved_chunks = retrieve_github(
                question
            )

        elif source == "github_repo":

            retrieved_chunks = retrieve_repo(
                question
            )

        else:

            retrieved_chunks = retrieve(
                question
            )

        context = "\n\n".join(
            retrieved_chunks
        )

        answer = generate_answer(
            context=context,
            question=question
        )

        return f"""
Source Selected: {source}

Answer:
{answer}
"""

    except Exception as e:

        return f"Ask Anything Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()