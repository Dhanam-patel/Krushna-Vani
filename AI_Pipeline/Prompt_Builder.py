from langchain_core.prompts import PromptTemplate

Template = PromptTemplate(
    template="""

Context (excerpts from Bhagavad Gita and commentary):
{retrieved_context}

User Question:
{user_input}

Instructions for response:
- Provide a very simplified and clear explanation suitable for youth, based only on the provided context.
- Do NOT add any external information or hallucinate.
- Then, provide the actual verse exactly as in the context, with appropriate formatting.
- Afterwards, list meta-data including:
  * Shlok (verse) number(s)
  * Adhyay (chapter) number or name
  * Any other relevant citations or metadata
- Maintain respect for the original text's meaning and spiritual tone.
- Help the user engage with the teachings meaningfully.

Response format:
1. Simple Explanation:
   [Your simplified understandable answer]

2. Actual Verse from the Context:
   [The exact verse, properly quoted and tagged]

3. Meta Data:
   - Shlok (Verse) number: [Verse number]
   - Adhyay (Chapter) number: [Chapter number or name]
   - Other citation: [Translator, publisher, or relevant info]

Response:

""",
input_variables=["retrieved_context", "user_input"],
validate_template=True
)


Template.save("AI_Pipeline/Prompt_Template.json")