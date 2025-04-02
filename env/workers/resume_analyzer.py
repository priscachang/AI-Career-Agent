from arklex.env.workers.base_worker import BaseWorker
import pdfplumber

class ResumeWorker(BaseWorker):
    name = "ResumeWorker"
    description = "Analyzes uploaded resumes and provides readability suggestions."
    def run(self, task_input):
        # task_input file path
        file_path = task_input.get("file_path", "")
        if not file_path.endswith(".pdf"):
            return {"message": "❌ Only PDF resumes are supported at the moment."}

        try:
            with pdfplumber.open(file_path) as pdf:
                text = "\n".join([page.extract_text() or "" for page in pdf.pages])
            
            # return 500 words
            preview = text[:500]
            return {
                "message": f"📄 Your resume has been received. Here's a quick preview:\n\n{preview}\n\nWould you like feedback or role suggestions based on this?"
            }

        except Exception as e:
            return {"message": f"⚠️ Failed to read the file: {str(e)}"}
