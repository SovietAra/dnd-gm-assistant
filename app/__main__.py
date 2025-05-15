from app.chunker import load_transcript, chunk_text

if __name__ == "__main__":
    text = load_transcript("data/example_transcript.txt")
    chunks = chunk_text(text, max_length = 500)
    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i+1} ---\n{chunk}")