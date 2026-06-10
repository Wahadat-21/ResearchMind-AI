from agents.planner import PlannerAgent
from agents.researcher import ResearchAgent
from agents.verifier import VerificationAgent
from agents.writer import WriterAgent

from memory.vector_store import MemoryStore
from tools.pdf_export import PDFExporter

def main():

    topic = input("Research Topic: ")

    planner = PlannerAgent()
    researcher = ResearchAgent()
    verifier = VerificationAgent()
    writer = WriterAgent()

    memory = MemoryStore()
    pdf = PDFExporter()

    print("Creating Plan...")

    plan = planner.create_plan(topic)

    for step in plan:
        print(step)

    print("\nResearching...")

    data = researcher.search(topic)

    print("Verifying...")

    if verifier.verify(data):

        report = writer.generate_report(
            topic,
            data
        )

        memory.save(
            topic,
            report
        )

        pdf.export(
            f"{topic}.pdf",
            report
        )

        print("\nResearch Completed")
        print(report[:1000])

    else:
        print("Verification Failed")

if __name__ == "__main__":
    main()
