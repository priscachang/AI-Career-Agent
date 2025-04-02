# 🧠 AI Career Assistant

An intelligent job application assistant that allows users to upload their resume, receive personalized readability feedback, and get matched with internship opportunities using real-time data from platforms like [Intern-List](https://intern-list.com).

This project is built on the [Arklex Agent First Organization framework](https://arklexai.github.io/Agent-First-Organization/), designed for rapid AI agent prototyping with LangChain and OpenAI APIs.

---

## ✨ Features

- **📄 Resume Uploader Tool**: Upload a `.pdf` resume to receive a preview and suggestions on formatting, readability, and clarity.
- **🧠 LangChain-powered Agent**: Automatically analyzes your background and preferences, and reformulates search queries using LLMs.
- **🔍 Internship Search**: Retrieves job listings from `intern-list.com` based on skills, location, and preferences.
- **🗣️ Multi-turn Conversations**: Supports user clarification and interaction using structured LangChain flows.
- **📚 Knowledge Augmentation**: RAG-enabled assistant leverages curated sources like Jobscan and Indeed to offer resume and interview tips.

---

## 🧩 Architecture Overview

- **Workers**: Modular workers for tasks like search, messaging, and resume analysis.
- **Tools**: Custom LangChain tools like `ResumeUploader`.
- **Prompts**: Stored in reusable YAML templates.
- **Planner**: Chooses appropriate worker per user query.
- **RAG**: Uses predefined `rag_docs` from job-related resources.
- **LLMs**: Compatible with OpenAI, Gemini, Anthropic, HuggingFace.

---

## 🛠️ Tech Stack

- Python 3.10+
- LangChain + LangGraph
- FastAPI (API runtime)
- pdfplumber (resume parsing)
- OpenAI API (chat generation)
- Intern-List (job search)
- ChromeDriver (crawling & RAG)
- Arklex Framework

---

## 🚀 Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

Make sure you set up your `.env` with the required API keys:

```
OPENAI_API_KEY=sk-xxxx
```

---

### 2. Upload and Analyze Resume

Run the test script to upload your resume and get feedback:

```bash
python test/test_resume_upload.py
```

You will see a preview and response from the ResumeWorker.

---

### 3. Launch the agent

```bash
python run.py --input-dir ./examples/ai_job_resume_assistant
```

This will start a chatbot loop. It will first guide you to upload your resume, and then start matching internships.

---

### 4. Run API for evaluation (Optional)

```bash
python model_api.py --input-dir ./examples/ai_job_resume_assistant
```

This starts the FastAPI service on `http://localhost:8000`.

---

## 📂 Project Structure

```
AI_Career_Agent/
├── arklex/                # Core Arklex agent framework
├── examples/              # Task config files
├── logs/                  # Logs from execution
├── model_api.py           # Launch API server for model evaluation
├── create.py              # Task graph creation
├── run.py                 # CLI for agent interaction
├── eval.py                # Evaluation runner
├── test_resume_upload.py  # Resume PDF test script
├── requirements.txt
├── pyproject.toml
```

---

## 🧭 Future Improvements

- **⚡ Solve OpenAI API quota limitations** by migrating to local models or other API providers.
- **📈 Upgrade compute power** to support multi-user access and more complex document analysis.
- **🌐 Web Interface (Frontend)**: Build a user-friendly web UI for users to drag/drop resumes and interact with the chatbot visually.
- **📁 Resume History and Dashboard**: Save past feedback and enable side-by-side comparisons of resume versions.
- **🎯 Recommendation Engine**: Integrate scoring or ranking system for job match precision.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE.md` file for details.

---

## 🙋 Contact

Developed by [ChengHsin Chang](https://www.linkedin.com/in/cheng-hsinchang/)  
For questions or feedback, feel free to open an issue or reach out!
