import asyncio
import sys
# Configure UTF-8 encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    # Alternatively, use this if above doesn't work
    # import codecs
    # sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

from gpt_researcher import GPTResearcher

async def main():
    query = "why is Nvidia stock going up?"
    researcher = GPTResearcher(query=query, report_type="research_report")
    # Conduct research on the given query
    research_result = await researcher.conduct_research()
    # Write the report
    report = await researcher.write_report()
    return report

if __name__ == "__main__":
    try:
        report = asyncio.run(main())
        # Print the report, ensuring proper encoding
        print(report)
    except UnicodeEncodeError as e:
        print("Encoding error occurred. Trying to encode as ASCII:", str(e))
        print(report.encode('ascii', 'ignore').decode('ascii'))