from pydantic import BaseModel
from typing import Literal, Optional


class Intent(BaseModel):
    action: Literal["create_file", "edit_file", "delete_file", "run_command"]
    target_path: str
    content: Optional[str] = None
    command: Optional[str] = None