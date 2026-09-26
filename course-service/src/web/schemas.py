"""Pydantic schemas for the web API."""

from pydantic import BaseModel, ConfigDict


class BaseSchemaModel(BaseModel):
    """Base model for API schemas."""

    model_config = ConfigDict(
        from_attributes=True, validate_assignment=True, populate_by_name=True
    )


class ServiceInfo(BaseSchemaModel):
    """Service health information."""

    healthy: bool = True
