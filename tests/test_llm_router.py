import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from app.router.llm_router import choose_source_llm

print(
    choose_source_llm(
        "What are the benefits of RAG?"
    )
)

print(
    choose_source_llm(
        "How does GraphRAG indexing work?"
    )
)

print(
    choose_source_llm(
        "What are language models?"
    )
)