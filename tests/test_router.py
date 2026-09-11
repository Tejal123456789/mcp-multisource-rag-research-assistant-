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

from app.router.source_router import choose_source

print(
    choose_source(
        "What are the benefits of RAG?"
    )
)

print(
    choose_source(
        "What is Retrieval Augmented Generation?"
    )
)