
from huggingface_hub import HfApi
import os

class TermuxHFOrchestrator:
    def __init__(self, hf_token=None):
        self.hf_token = hf_token if hf_token else os.getenv("HF_TOKEN")
        if not self.hf_token:
            raise ValueError("Hugging Face token not provided and not found in environment variables.")
        self.api = HfApi(token=self.hf_token)

    def create_space(self, repo_id, space_sdk="streamlit", private=False, exist_ok=True):
        """Creates a new Hugging Face Space."""
        try:
            self.api.create_repo(repo_id=repo_id, space_sdk=space_sdk, private=private, exist_ok=exist_ok)
            print(f"Space [1m{repo_id}[0m created successfully.")
        except Exception as e:
            print(f"Error creating space [1m{repo_id}[0m: {e}")

    def upload_file_to_space(self, repo_id, path_or_fileobj, path_in_repo, commit_message="Add file via Termux Orchestrator"):
        """Uploads a file to a Hugging Face Space."""
        try:
            self.api.upload_file(
                path_or_fileobj=path_or_fileobj,
                path_in_repo=path_in_repo,
                repo_id=repo_id,
                repo_type="space",
                commit_message=commit_message
            )
            print(f"File [1m{path_in_repo}[0m uploaded to space [1m{repo_id}[0m successfully.")
        except Exception as e: 
            print(f"Error uploading file to space \033[1m{repo_id}\033[0m: {e}")

    def get_space_status(self, repo_id):
        """Gets the status of a Hugging Face Space."""
        try:
            info = self.api.repo_info(repo_id=repo_id, repo_type="space")
            print(f"Space [1m{repo_id}[0m status: [1m{info.cardData.sdk_status}[0m")
            return info.cardData.sdk_status
        except Exception as e:
            print(f"Error getting space status for [1m{repo_id}[0m: {e}")
            return None

    def delete_space(self, repo_id):
        """Deletes a Hugging Face Space."""
        try:
            self.api.delete_repo(repo_id=repo_id, repo_type="space")
            print(f"Space [1m{repo_id}[0m deleted successfully.")
        except Exception as e:
            print(f"Error deleting space \033[1m{repo_id}\033[0m: {e}")


if __name__ == "__main__":
    # Example Usage (replace with your actual token and repo_id)
    # You would typically set HF_TOKEN as an environment variable in Termux
    # For testing, you can pass it directly:
    # orchestrator = TermuxHFOrchestrator(hf_token="hf_YOUR_TOKEN_HERE")

    orchestrator = TermuxHFOrchestrator()

    # 1. Create a new Space
    # IMPORTANT: Replace 'your-hf-username' with your actual Hugging Face username
    space_name = "elmatador0197/oasis-enterprise-mvp"
#    orchestrator.create_space(space_name, space_sdk="gradio")

    # 2. Upload a simple app.py to the Space
    # Create a dummy app.py file for demonstration
    with open("app.py", "w") as f:
        f.write("""import gradio as gr

def greet(name):
    return "Hello " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
""")
    orchestrator.upload_file_to_space(space_name, "app.py", "app.py")

    # 3. Get Space Status
#    orchestrator.get_space_status(space_name)

#    # 4. (Optional) Delete the Space after testing
#    # orchestrator.delete_space(space_name)

#    # Clean up dummy file
#    os.remove("app.py")