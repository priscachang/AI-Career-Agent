import os
from arklex.env.workers.resume_analyzer import ResumeWorker

RESUME_PATH = "test/Fake_Resume_Sample.pdf"

def test_resume_upload():
    if not os.path.exists(RESUME_PATH):
        print(f"❌ Resume file not found: {RESUME_PATH}")
        return

    worker = ResumeWorker()
    result = worker.run({"file_path": RESUME_PATH})
    
    print("📄 AI Feedback：\n")
    print(result["message"])

if __name__ == "__main__":
    test_resume_upload()
