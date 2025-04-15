from .agents_base import AgentBase


class SanitizeDataTool(AgentBase):
    def __init__(self,  max_retries, verbose=True):
        super().__init__(name="SanitizeDataTool",max_retries=max_retries, verbose=verbose)

    def execute(self,medical_data):
        messages=[
            {"role":"system", "content":"You are an AI assistant which sanitizes given medical data by removing Protected Health Information."},
            {
                "role": "user",
                "content": (
                    "Please remove all PHI from the given data:\n\n"
                    f"{medical_data}\n\n:Sanitized Data:"
                )
            }
        ]
        sanitized_data=self.call_openai(messages,max_tokens=300)
        return sanitized_data