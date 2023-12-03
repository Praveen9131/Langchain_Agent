from langchain.agents import AgentType, Tool, initialize_agent
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.utilities import SerpAPIWrapper
import gradio as gr
# Replace 'your_actual_api_key' with your SerpAPI API key
search = SerpAPIWrapper(serpapi_api_key='')

tools = [
    Tool(
        name="Current Search",
        func=search.run,
        description="useful for when you need to answer questions about current events or the current state of the world",
    ),
]
# Replace 'your_actual_api_key' with your OpenAI API key
def search_job_openings(query):
    # Perform the search
    search_result = search.run(query=query)
    
    # Return the search result
    return search_result

# Create a Gradio interface
iface = gr.Interface(
    fn=search_job_openings,
    inputs=gr.Textbox(type="text", label="Enter your query"),
    outputs=gr.Textbox(type="text", label="Search Result"),
    live=True,
    title="agent",
    description="Enter a query to search for current job openings.",
)

# Launch the Gradio interface
iface.launch(share=True)