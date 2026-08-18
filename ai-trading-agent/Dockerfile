FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -e ".[api,alpaca,telegram]"
EXPOSE 8000
CMD ["uvicorn", "ai_trading_agent.api.routes:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]

