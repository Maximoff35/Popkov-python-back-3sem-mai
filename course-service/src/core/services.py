"""Course service business logic."""

from src.web.schemas import ServiceInfo


def get_service_info() -> ServiceInfo:
    """Return service health information."""
    return ServiceInfo()
