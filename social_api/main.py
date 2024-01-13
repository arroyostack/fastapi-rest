# uvicorn social_api.main:app --reload

from fastapi import FastAPI
from social_api.routers.post import router as post_router

# Init App
app = FastAPI()

# Hook router
app.include_router(post_router)


