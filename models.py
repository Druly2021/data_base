from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()  # Создаем базовый класс


class Department(
    Base
):  # Создаём модель данных департамента, наследуясь от базового класса
    __tablename__ = "departments"  # Определяем имя таблицы
    id = Column(Integer, primary_key=True, index=True)  # Колонка с типом данных Integer
    name = Column(String, nullable=False)  # Колонка с типом данных String

    divisions = relationship(
        "Division", back_populates="department"
    )  # Связь с таблицей подразделений


class Division(
    Base
):  # Создаём модель данных подразделения, наследуясь от базового класса
    __tablename__ = "divisions"  # Определяем имя таблицы
    id = Column(Integer, primary_key=True, index=True)  # Колонка с типом данных Integer
    name = Column(String, nullable=False)  # Колонка с типом данных String
    department_id = Column(
        Integer, ForeignKey("departments_id")
    )  # Колонка в таблице с типом данных Integer и внешним ключом

    department = relationship(
        "Department", back_populates="divisions"
    )  # Cвязь с таблицей департаментов

    employees = relationship(
        "Employee", back_populates="division"
    )  # Cвязь с таблицей сотрудников


class Employee(Base):  # Создаём модель данных сотрудника, наследуясь от базового класса
    __tablename__ = "employees"  # Определяем имя таблицы
    id = Column(Integer, primary_key=True, index=True)  # Колонка с типом данных Integer
    name = Column(String, nullable=False)  # Колонка с типом данных String
    division_id = Column(Integer, ForeignKey("divisions_id"))  # Добавляем подразделение

    division = relationship(
        "Division", back_populates="employees"
    )  # Взаимосвязь между подразделениями и работником


DATABASE_URL = "sqlite:///./company.db"  # Ссылка к базе данных

engine = create_engine(DATABASE_URL)  # Создание движка для БД

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)  # Локальная сессия для работы с БД


def create_tables():  # Функция для создания таблиц
    Base.metadata.create_all(bind=engine)
