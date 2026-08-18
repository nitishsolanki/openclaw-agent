from pathlib import Path
import uvicorn
from ai_trading_agent.api.routes import create_app

uvicorn.run(create_app(Path(__file__).parents[1]), host="127.0.0.1", port=8000)

