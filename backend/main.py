from deep_translator import GoogleTranslator
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TextRequest(BaseModel):
    text: str


@app.post("/translate")
async def translate_text(request: TextRequest):
    text = request.text

    return {
        "english": GoogleTranslator(source="auto", target="en").translate(text),
        "tamil": GoogleTranslator(source="auto", target="ta").translate(text),
        "bengali": GoogleTranslator(source="auto", target="bn").translate(text),
    }
