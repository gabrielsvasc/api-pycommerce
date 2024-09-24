from pydantic import BaseModel, ConfigDict


class UserTypeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    type_id: int
    type_name: str
