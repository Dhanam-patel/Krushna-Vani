from AI_Pipeline.model import model
from AI_Pipeline.prompt import prompt

def Generate_response(user_input, result):
    final_prompt = prompt(user_input, result)
    response = model.invoke(final_prompt)
    return response