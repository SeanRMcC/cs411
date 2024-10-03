from typing import Any, Optional

from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:

    def __init__(self, path_id: int, start_location: Habitat, destination: Habitat, duration: Optional[int]) -> None:
        
        self.path_id = path_id
        self.start_location = start_location
        self.destination = destination
        self.duration = duration or None

    def get_migration_path_details(self, path_id: int) -> dict:
        pass

    def update_migration_path_details(self, path_id: int, **kwargs: Any) -> None:
        pass

        