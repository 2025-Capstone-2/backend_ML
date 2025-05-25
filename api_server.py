from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import feature_router

app = FastAPI(
    title="WiFi Streaming Video Test API",
    description="PCAP 파일을 분석하여 표적 스트림 반환",
    version="1.0.0",
)

app.include_router(feature_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "WiFi Streaming Video Test API is running."}
