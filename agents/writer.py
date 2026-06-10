from openai import OpenAI

client = OpenAI()

class WriterAgent:

    def generate_report(self, topic, content):

        prompt = f"""
        Create a professional research report.

        Topic:
        {topic}

        Content:
        {content}
        """

        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role":"user","content":prompt}
            ]
        )

        return response.choices[0].message.content
