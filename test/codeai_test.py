from src.codeai import CodeAI


codeai = CodeAI(".")

question = "Where is cosine similarity calculated?"

answer = codeai.ask(
    question,
    top_k=5
)

print("\nCodeAI:\n")
print(answer)