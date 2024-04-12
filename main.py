from fastapi import FastAPI
from app.routes import router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(router,prefix="/user")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, you can specify specific origins here
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Add more HTTP methods if needed
    allow_headers=["*"],  # Allow all headers, you can specify specific headers here
)
