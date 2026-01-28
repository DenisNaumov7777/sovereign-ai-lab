# Sovereign AI Lab

A local, privacy-first AI backend running on **Mistral 7B**, **FastAPI**, and **Docker**.
Designed for sovereign data processing within European jurisdiction (GDPR compliant architecture).

**Author:** Denis Naumov
📍 Cologne, Germany 🇩🇪

---

## 🚀 Features

* **Sovereign Inference:** Runs completely offline on local hardware (Apple Silicon M-series optimized).
* **Containerized:** Fully isolated environment using Docker.
* **API-First:** Lightweight REST API built with FastAPI.
* **Privacy:** No data leaves the server. No external API keys required.

## 🛠 Prerequisites

* **Docker** (via OrbStack recommended for macOS)
* **Ollama** running locally with the Mistral model

## 📦 Installation & Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/DenisNaumov7777/sovereign-ai-lab.git](https://github.com/DenisNaumov7777/sovereign-ai-lab.git)
    cd sovereign-ai-lab
    ```

2.  **Ensure Ollama is running:**
    ```bash
    ollama serve
    # Or just open the Ollama app on macOS
    ```

3.  **Build the Docker image:**
    ```bash
    docker build -t sovereign-ai .
    ```

4.  **Run the container:**
    ```bash
    docker run -p 8000:8000 sovereign-ai
    ```

## 🧪 Usage (Test)

You can test the API using `curl` from your terminal.

**Health Check:**
```bash
curl http://localhost:8000/

```

**Chat Request (Example):**

```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Briefly explain: What is GDPR?"}'

```

