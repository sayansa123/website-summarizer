from fastapi import FastAPI
from about import router as about
from pass_url import router as url
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()
app.include_router(about)
app.include_router(url)