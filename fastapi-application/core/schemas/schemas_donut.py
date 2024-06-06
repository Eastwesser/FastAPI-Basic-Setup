from pydantic import BaseModel, ConfigDict


class DonutBase(BaseModel):
    donut: str
    description: str


class DonutCreate(DonutBase):
    pass


class DonutRead(DonutBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
