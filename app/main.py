from fastapi import FastAPI, Query

app = FastAPI(
    title="Tiny FastAPI Hello Service",
    description="A minimal FastAPI app that returns a greeting and health check.",
    version="0.1.0",
)

DEFAULT_GREETING = "Hello, World!"


@app.get("/", response_model=dict, summary="Root greeting")
def read_root(msg: str = Query(None, description="Custom greeting message")):
    """
    Return a greeting. If the `msg` query parameter is provided, it is used as the greeting;
    otherwise the default greeting is returned.
    """
    greeting = msg if msg is not None else DEFAULT_GREETING
    return {"greeting": greeting}


@app.get("/health", response_model=dict, summary="Health check")
def health_check():
    """
    Simple health‑check endpoint used for liveness probes.
    """
    return {"status": "ok"}