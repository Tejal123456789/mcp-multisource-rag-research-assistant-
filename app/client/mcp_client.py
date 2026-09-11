# MCP Client for Research Assistant

import asyncio

from mcp.client import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client


async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["app/server/mcp_server.py"]
    )

    async with stdio_client(server_params) as (read_stream, write_stream):
        print("Connected to MCP Server")

        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            print("Session Initialized")
            tools = await session.list_tools()

            print("\nAvailable Tools:")
            print(tools)
            resources = await session.list_resources()

            print("\nAvailable Resources:")
            print(resources)
            resource_content = await session.read_resource(
                "research://note"
            )
            paper_content = await session.read_resource(
                "research://paper1"
            )

            print("\nPaper Content:")
            print(paper_content)

            print("\nResource Content:")
            print(resource_content)

            result = await session.call_tool("get_project_info")
            print("\nTool Result:")
            print(result)
            summary_result = await session.call_tool(
                "summarize_text",
                {"text": "GraphRAG combines knowledge graphs with retrieval augmented generation to improve multi-hop reasoning."}
            )

            print("\nSummary Result:")
            print(summary_result)
            compare_result = await session.call_tool(
                "compare_texts",
                {
                    "text1": "GraphRAG is useful.",
                    "text2": "MCP is useful."
                }
            )
            print("\nCompare Result:")
            print(compare_result)
            print(session)

            papers_result = await session.call_tool(
                "list_papers"
            )

            print("\nAvailable Papers:")
            print(papers_result)

            selected_paper = await session.call_tool(
                "read_paper",
            {
                "pdf_name": "paper7.pdf"
            }
            )

            print("\nSelected Paper Content:")
            print(selected_paper)

            summary = await session.call_tool(
                "summarize_paper",
            {
                "pdf_name": "paper7.pdf"
            }
            )

            print("\nPaper Summary:")
            print(summary)
            print("Calling compare_papers...")
            comparison_result = await session.call_tool(
                "compare_papers",
            {
                "pdf1": "paper1.pdf",
                "pdf2": "paper7.pdf"
            }
            )
            print("compare_papers finished")
            print("\nPaper Comparison:")
            print(comparison_result)

            search_result = await session.call_tool(
                "search_paper",
            {
                "pdf_name": "paper7.pdf",
                "query": "language"
            }
            )

            print("\nSearch Result:")
            print(search_result)

            answer_result = await session.call_tool(
                "ask_paper",
            {
                "pdf_name": "paper7.pdf",
                "question": "What is Retrieval Augmented Generation?"
            }
            )

            print("\nQuestion Answer Result:")
            print(answer_result)

            github_answer = await session.call_tool(
                "ask_github",
                {
                    "question": "How can we improve a RAG pipeline?"
                }
            )

            print("\nGitHub Answer Result:")
            print(github_answer)

            anything_result = await session.call_tool(
                "ask_anything",
                {
                    "question": "What are the benefits of RAG?"
                }
            )

            print("\nAsk Anything Result:")
            print(anything_result)

if __name__ == "__main__":
    asyncio.run(main())