from fastapi import APIRouter
from summerizer import summerize
from typing import Dict

router = APIRouter()
summery_cache:Dict[str,str]= {}

@router.get('/url')
def url(
    url:str
):
    if url not in summery_cache:
        response = summerize(url)
        summery_cache[url]=response

    return summery_cache.get(url)