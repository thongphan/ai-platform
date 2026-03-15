class PromptBuilder:

    def build(self, request):

        return f"""
                You are a helpful AI assistant.
                
                User: {request.name}
                
                Question:
                {request.query}
                """