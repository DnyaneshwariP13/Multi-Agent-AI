from .agents_base import AgentBase


class WriteArticleTool(AgentBase):
    def __init__(self,  max_retries, verbose=True):
        super().__init__(name="WriteArticleTool",max_retries=max_retries, verbose=verbose)

    def execute(self,topic,outline=None):
        system_message="You are an expert academic writer."
        user_content=f"Write research article on the following topic:\n Topic:{topic}\n\n"
       
        if outline:
            user_content += f"Outline:\n{outline}\n\n"
        user_content += f"Article:\n"

        messages=[
            {"role":"system","content":system_message },
            {"role":"user","content":user_content}
        ]
        article=self.call_openai(messages,max_tokens=300)
        return article