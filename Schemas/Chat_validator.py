from pydantic import BaseModel, Field
from typing import Annotated

class Chat_Validator(BaseModel):
    Input : Annotated[str, Field(..., title="Input",description="User input for chat with Bhagavad Gita")]  