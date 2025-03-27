from datetime import date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Column, Table, CheckConstraint, DATE, text
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


class CategoryEntity(Base):
    """
    Representa una categoría de rutina. Ejemplos de categorías de rutina incluyen Yoga, Spinning, Crossfit, Fuerza, Resistencia, etc. Cada categoría puede tener múltiples rutinas asociadas.
    """
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    routines: Mapped[list["RoutineEntity"]] = relationship("RoutineEntity", secondary="categories_routines", back_populates="categories", lazy="selectin")

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

    categories: Mapped[list["CategoryEntity"]] = relationship("CategoryEntity", secondary="categories_routines", back_populates="routines", lazy="selectin")
    exercises: Mapped[list["ExerciseEntity"]] = relationship("ExerciseEntity", secondary="routines_exercises", lazy="selectin")

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
    birth_date: Mapped[date] = mapped_column(DATE, nullable=False)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    children: Mapped[list["ChildEntity"]] = relationship("ChildEntity", back_populates="tutor", lazy="selectin")

    @hybrid_property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    
    @age.expression
    def age_expression(cls):
        today = func.current_date()
        today_month = func.extract('month', today)
        today_day = func.extract('day', today)
        birth_month = func.extract('month', cls.birth_date)
        birth_day = func.extract('day', cls.birth_date)
        
        # Check if today's date is before the birth date in the current year
        is_before_birthday = (today_month < birth_month) | ((today_month == birth_month) & (today_day < birth_day))
        
        return func.extract('year', today) - func.extract('year', cls.birth_date) - func.cast(is_before_birthday, Integer)

    def __repr__(self):
        return f"TutorEntity(id={self.id}, full_name={self.full_name})"


class ChildEntity(Base):
    """
    Representa a un niño que realiza las rutinas. Cada niño puede tener un nombre completo, una edad y un tutor asociado. Los niños pueden estar asociados con múltiples rutinas a través de la tabla de asignación.
    """
    __tablename__ = "children"
    

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    birth_date: Mapped[date] = mapped_column(DATE, nullable=False)
    tutor_id: Mapped[int] = mapped_column(Integer, ForeignKey("tutors.id"), nullable=False)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    # Adding constraints on birth_date instead of age
    __table_args__ = (
        # Example constraint: children must be born after a certain date (for max age)
        CheckConstraint(text("birth_date > DATE '2008-01-01'"), name="child_min_birth_date"),
        # Example constraint: children must be born before a certain date (for min age)
        CheckConstraint(text("birth_date < CURRENT_DATE - INTERVAL '5 years'"), name="child_max_birth_date"),
    )

    tutor: Mapped["TutorEntity"] = relationship("TutorEntity", back_populates="children")
    favorite_routines: Mapped[list["RoutineEntity"]] = relationship("RoutineEntity", secondary="favorite_routines",lazy="selectin")

    @hybrid_property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    
    @age.expression
    def age_expression(cls):  # Renamed to avoid redeclaration warning
        today = func.current_date()
        today_month = func.extract('month', today)
        today_day = func.extract('day', today)
        birth_month = func.extract('month', cls.birth_date)
        birth_day = func.extract('day', cls.birth_date)
        
        # Check if today's date is before the birth date in the current year
        is_before_birthday = (today_month < birth_month) | ((today_month == birth_month) & (today_day < birth_day))
        
        return func.extract('year', today) - func.extract('year', cls.birth_date) - func.cast(is_before_birthday, Integer)

    def __repr__(self):
        return f"ChildEntity(id={self.id}, full_name={self.full_name})"


FavoriteRoutinesEntity = Table(
    "favorite_routines",
    Base.metadata,
    Column("child_id", Integer, ForeignKey("children.id"), primary_key=True, nullable=False),
    Column("routine_id", Integer, ForeignKey("routines.id"), primary_key=True, nullable=False),
)