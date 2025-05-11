from domain.model.dto import CategoryDTO, ExerciseDTO, LevelDTO
from infrastructure.database.model import CategoryEntity, ExerciseEntity, LevelEntity


class EXERCISE_MAPPER:
    @staticmethod
    def TO_DTO(exercise: ExerciseEntity) -> ExerciseDTO:
        return ExerciseDTO(
            id=exercise.id,
            name=exercise.name,
            description=exercise.description,
            category=exercise.category.name,
            level=exercise.level.name,
            duration=exercise.duration
        )


class CATEGORY_MAPPER:
    @staticmethod
    def TO_DTO(category: CategoryEntity) -> CategoryDTO:
        return CategoryDTO(
            id=category.id,
            name=category.name
        )

class LEVEL_MAPPER:
    @staticmethod
    def TO_DTO(level: LevelEntity) -> LevelDTO:
        return LevelDTO(
            id=level.id,
            name=level.name
        )
    