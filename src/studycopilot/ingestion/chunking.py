from langchain_text_splitters import RecursiveCharacterTextSplitter

from studycopilot.ingestion.schema import DocumentChunk


splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)


def create_chunks(pages, document_id):

    chunks = []

    chunk_id = 0


    for page in pages:

        page_chunks = splitter.split_text(
            page["text"]
        )


        for chunk_index, chunk_text in enumerate(page_chunks):

            chunks.append(

                DocumentChunk(

                    text=chunk_text,

                    source=page["source"],

                    page=page["page"],

                    chunk_id=chunk_id,

                    chunk_index_in_page=chunk_index,

                    document_id=document_id,

                    total_pages=page["total_pages"]
                )
            )


            chunk_id += 1


    return chunks