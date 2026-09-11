import os

from pypdf import PdfReader

from app.retrieval.chunking import chunk_text
from app.retrieval.embeddings import get_embedding
from app.retrieval.vector_store import collection


def ingest_pdfs():

    pdf_folder = "data/papers"

    pdf_files = [
        file
        for file in os.listdir(pdf_folder)
        if file.endswith(".pdf")
    ]

    chunk_id = 0

    for pdf_file in pdf_files:

        pdf_path = os.path.join(pdf_folder, pdf_file)

        print(f"Processing: {pdf_file}")

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        chunks = chunk_text(text)

        for chunk in chunks:

            try:

                embedding = get_embedding(str(chunk))

                collection.add(
                    ids=[f"chunk_{chunk_id}"],
                    documents=[str(chunk)],
                    embeddings=[embedding],
                    metadatas=[
                    {
                        "source": pdf_file
                    }
                ]
            )

                chunk_id += 1

            except Exception as e:

                print(f"ERROR in {pdf_file}")
                print(type(chunk))
                print(repr(chunk[:200] if isinstance(chunk, str) else chunk))
                print(e)

                continue

    print("All PDFs ingested successfully.")


if __name__ == "__main__":
    ingest_pdfs()