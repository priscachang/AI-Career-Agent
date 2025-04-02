class ResumeUploader:
    name = "ResumeUploader"
    description = "Upload a resume file (PDF) to receive analysis and suggestions."

    def __init__(self):
        from langchain_core.tools import tool

        # 👇 定義成 LangChain Tool 格式，讓 Arklex 可以讀到 .info
        @tool
        def uploader_tool(file_path: str) -> dict:
            """Upload a PDF resume and return the file path."""
            return {"file_path": file_path}

        self.info = uploader_tool
        self.__call__ = uploader_tool

