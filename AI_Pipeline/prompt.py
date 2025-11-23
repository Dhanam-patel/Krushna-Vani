from langchain_core.prompts import load_prompt

def prompt(user_input, result):
    final = ""
    for data in result.matches:
        final = f"{final} + {data["metadata"]["content"]}"
    template = load_prompt("AI_Pipeline/Prompt_Template.json")
    Prompt = template.invoke({
        "retrieved_context": final,
        "user_input": user_input
    })
    return Prompt