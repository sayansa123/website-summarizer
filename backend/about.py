from fastapi import APIRouter
router = APIRouter()

@router.get("/about")
def about():
    return {
        "project": "Website Summarizer",
        "description": "A FastAPI-based backend that extracts content from any public URL and generates a concise summary using a Large Language Model.",
        "features": [
            "Summarize blogs and articles",
            "Supports any public website",
            "LLM-powered summarization",
            "Chrome Extension compatible"
        ],
        "endpoints": {
            "/url": "Summarize a given webpage URL",
            "/about": "Project information"
        },
        "tech_stack": [
            "FastAPI",
            "LangChain",
            "HuggingFace (Mistral-7B)",
            "WebBaseLoader"
        ]
    }