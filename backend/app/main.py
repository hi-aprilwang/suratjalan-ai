import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.config import settings
from app.api.audit import router as audit_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="SuratJalan.AI - AI-Powered Proof-of-Delivery Audit & Invoice Reconciliation Engine for Indonesian Logistics"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router under /api
app.include_router(audit_router, prefix="/api")

# Mount static files for sample presets if directory exists
samples_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../datasets/samples"))
if not os.path.exists(samples_dir):
    samples_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../datasets/samples"))

if os.path.exists(samples_dir):
    app.mount("/samples", StaticFiles(directory=samples_dir), name="samples")
    print(f"Mounted sample files from {samples_dir}")

@app.get("/")
async def root():
    return {
        "app": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "docs": "/docs",
        "health": "/api/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
