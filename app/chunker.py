import textwrap

# Read .txt file and return as one string
def load_transcript(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as transcriptFile:
        transcriptText = transcriptFile.read()
    return transcriptText
    

# Accept the text and tokenize it
def chunk_text(text: str, max_length: int) -> list[str]:
    chunks = textwrap.wrap(text, max_length)
    return chunks