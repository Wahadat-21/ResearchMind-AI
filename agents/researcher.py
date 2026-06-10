import requests

class ResearchAgent:

    def search(self, topic):

        url = f"https://en.wikipedia.org/wiki/{topic.replace(' ','_')}"

        try:
            data = requests.get(url).text
            return data[:5000]
        except:
            return "No data found"
