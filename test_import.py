import traceback

try:
    import backend.ai_engine
    print("SUCCESS")
except Exception:
    traceback.print_exc()