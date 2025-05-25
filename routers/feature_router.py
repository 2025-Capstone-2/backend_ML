from fastapi import APIRouter, UploadFile, File, HTTPException
from services.feature_extractor import analyze_pcap

router = APIRouter(prefix="/pcap")

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        result = await analyze_pcap(file)
        return result
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except FileNotFoundError as fnf:
        raise HTTPException(status_code=500, detail=str(fnf))
    except RuntimeError as re:
        raise HTTPException(status_code=500, detail=str(re))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
