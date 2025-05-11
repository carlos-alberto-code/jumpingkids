from sqlalchemy import Integer, String, ForeignKey, Column, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class SubscriptionTypeEntity(Base):
    __tablename__ = "subscription_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)

    def __init__(self, name: str):
        self.name = name
    
    def __repr__(self):
        return f"SubscriptionTypeEntity(name={self.name})"


class CategoryEntity(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    routines: Mapped[list["RoutineEntity"]] = relationship("RoutineEntity", secondary="categories_routines", back_populates="categories", lazy="selectin")
    exercises: Mapped[list["ExerciseEntity"]] = relationship("ExerciseEntity", back_populates="category", lazy="selectin")

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"CategoryEntity(id={self.id}, name={self.name})"


class RoutineEntity(Base):
    __tablename__ = "routines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(255), nullable=False)

    categories: Mapped[list["CategoryEntity"]] = relationship("CategoryEntity", secondary="categories_routines", back_populates="routines", lazy="selectin")
    exercises: Mapped[list["ExerciseEntity"]] = relationship("ExerciseEntity", secondary="routines_exercises", lazy="selectin")
    subscription_types: Mapped[list["SubscriptionTypeEntity"]] = relationship(
        "SubscriptionTypeEntity",
        secondary="routines_subscription_types",
        lazy="selectin"
    )

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"RoutineEntity(id={self.id}, name={self.name})"


CategoryRoutineEntity = Table(
    "categories_routines",
    Base.metadata,
    Column("category_id", Integer, ForeignKey("categories.id"), primary_key=True),
    Column("routine_id", Integer, ForeignKey("routines.id"), primary_key=True),
)


class ExerciseEntity(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"), nullable=False)
    level_id: Mapped[int] = mapped_column(Integer, ForeignKey("levels.id"), nullable=False)
    duration: Mapped[int] = mapped_column(Integer, nullable=False, default=15)

    category: Mapped["CategoryEntity"] = relationship("CategoryEntity", back_populates="exercises", lazy="selectin")
    level: Mapped["LevelEntity"] = relationship("LevelEntity", back_populates="exercises", lazy="selectin")

    subscription_types: Mapped[list["SubscriptionTypeEntity"]] = relationship(
        "SubscriptionTypeEntity",
        secondary="exercises_subscription_types",
        lazy="selectin"
    )

    def __init__(self, name: str, description: str, category_id: int, level_id: int):
        self.name = name
        self.description = description
        self.category_id = category_id
        self.level_id = level_id

    def __repr__(self):
        return f"ExerciseEntity(id={self.id}, name={self.name})"


RoutineExerciseEntity = Table(
    "routines_exercises",
    Base.metadata,
    Column("routine_id", Integer, ForeignKey("routines.id"), primary_key=True),
    Column("exercise_id", Integer, ForeignKey("exercises.id"), primary_key=True),
)

RoutineSubscriptionTypeEntity = Table(
    "routines_subscription_types",
    Base.metadata,
    Column("routine_id", Integer, ForeignKey("routines.id"), primary_key=True),
    Column("subscription_type_id", Integer, ForeignKey("subscription_types.id"), primary_key=True),
)

ExerciseSubscriptionTypeEntity = Table(
    "exercises_subscription_types",
    Base.metadata,
    Column("exercise_id", Integer, ForeignKey("exercises.id"), primary_key=True),
    Column("subscription_type_id", Integer, ForeignKey("subscription_types.id"), primary_key=True),
)

class TutorEntity(Base):
    __tablename__ = "tutors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    subscription_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("subscription_types.id"), nullable=False)

    children: Mapped[list["ChildEntity"]] = relationship("ChildEntity", back_populates="tutor", lazy="selectin")
    subscription_type: Mapped[SubscriptionTypeEntity] = relationship("SubscriptionTypeEntity", lazy="selectin")

    def __init__(self, full_name: str, username: str, password: str, subscription_type_id: int):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.subscription_type_id = subscription_type_id

    def __repr__(self):
        return f"TutorEntity(id={self.id}, full_name={self.full_name})"


class ChildEntity(Base):
    __tablename__ = "children"
    

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    tutor_id: Mapped[int] = mapped_column(Integer, ForeignKey("tutors.id"), nullable=False)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    tutor: Mapped["TutorEntity"] = relationship("TutorEntity", back_populates="children", lazy="selectin")
    favorite_routines: Mapped[list["RoutineEntity"]] = relationship("RoutineEntity", secondary="favorite_routines",lazy="selectin")

    def __init__(self, full_name: str, tutor_id: int, username: str, password: str):
        self.full_name = full_name
        self.tutor_id = tutor_id
        self.username = username
        self.password = password

    def __repr__(self):
        return f"ChildEntity(id={self.id}, full_name={self.full_name})"


FavoriteRoutinesEntity = Table(
    "favorite_routines",
    Base.metadata,
    Column("child_id", Integer, ForeignKey("children.id"), primary_key=True, nullable=False),
    Column("routine_id", Integer, ForeignKey("routines.id"), primary_key=True, nullable=False),
)

class LevelEntity(Base):
    __tablename__ = "levels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    routines: Mapped[list["RoutineEntity"]] = relationship("RoutineEntity", secondary="levels_routines", lazy="selectin")
    exercises: Mapped[list["ExerciseEntity"]] = relationship("ExerciseEntity", back_populates="level", lazy="selectin")

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"LevelEntity(id={self.id}, name={self.name})"

# Tabla de asociación opcional para rutinas por nivel
LevelsRoutinesEntity = Table(
    "levels_routines",
    Base.metadata,
    Column("level_id", Integer, ForeignKey("levels.id"), primary_key=True),
    Column("routine_id", Integer, ForeignKey("routines.id"), primary_key=True),
)
