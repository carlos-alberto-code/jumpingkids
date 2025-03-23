from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Integer, String, ForeignKey, DateTime, Column, Table, CheckConstraint


class Base(DeclarativeBase):
    pass


class CategoryEntity(Base):
    """
    Representa una categoría de rutina. Ejemplos de categorías de rutina incluyen Yoga, Spinning, Crossfit, Fuerza, Resistencia, etc. Cada categoría puede tener múltiples rutinas asociadas.
    """
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    routines: Mapped[list["RoutineEntity"]] = relationship("RoutineEntity", secondary="categories_routines", back_populates="categories")

    def __repr__(self):
        return f"CategoryEntity(id={self.id}, name={self.name})"


class RoutineEntity(Base):
    """
    Representa una rutina de ejercicio. Cada rutina puede tener un nombre, una descripción y una categoría asociada. Las rutinas pueden estar asociadas con múltiples ejercicios.
    """
    __tablename__ = "routines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"), nullable=False)

    categories: Mapped[list["CategoryEntity"]] = relationship("CategoryEntity", secondary="categories_routines", back_populates="routines")
    exercises: Mapped[list["ExerciseEntity"]] = relationship("ExerciseEntity", secondary="routines_exercises", back_populates="routines")

    def __repr__(self):
        return f"RoutineEntity(id={self.id}, name={self.name})"


CategoryRoutineEntity = Table(
    "categories_routines",
    Base.metadata,
    Column("category_id", Integer, ForeignKey("categories.id"), primary_key=True),
    Column("routine_id", Integer, ForeignKey("routines.id"), primary_key=True),
)


class ExerciseEntity(Base):
    """
    Representa un ejercicio individual. Cada ejercicio puede tener un nombre y una descripción. Los ejercicios pueden estar asociados con múltiples rutinas.
    """
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    routines: Mapped[list["RoutineEntity"]] = relationship("RoutineEntity", secondary="routines_exercises", back_populates="exercises")

    def __repr__(self):
        return f"ExerciseEntity(id={self.id}, name={self.name})"


RoutineExerciseEntity = Table(
    "routines_exercises",
    Base.metadata,
    Column("routine_id", Integer, ForeignKey("routines.id"), primary_key=True),
    Column("exercise_id", Integer, ForeignKey("exercises.id"), primary_key=True),
)

class TutorEntity(Base):
    """
    Representa un tutor o cuidador de un niño. Cada tutor puede tener un nombre completo y puede estar asociado con múltiples niños.
    """
    __tablename__ = "tutors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    children: Mapped[list["ChildEntity"]] = relationship("ChildEntity", back_populates="tutor")

    def __repr__(self):
        return f"TutorEntity(id={self.id}, full_name={self.full_name})"


class ChildEntity(Base):
    """
    Representa a un niño que realiza las rutinas. Cada niño puede tener un nombre completo, una edad y un tutor asociado. Los niños pueden estar asociados con múltiples rutinas a través de la tabla de asignación.
    """
    __tablename__ = "children"
    __table_args__ = (
        CheckConstraint("age >= 10", name="check_min_age"),
        CheckConstraint("age <= 15", name="check_max_age"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    tutor_id: Mapped[int] = mapped_column(Integer, ForeignKey("tutors.id"), nullable=False)
    tutor: Mapped["TutorEntity"] = relationship("TutorEntity", back_populates="children")

    def __repr__(self):
        return f"ChildEntity(id={self.id}, full_name={self.full_name}, age={self.age})"
