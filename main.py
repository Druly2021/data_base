from models import SessionLocal, Department, Division, Employee    # Импортируем необходимые нам зависимости
from models import create_tables    # Импортируем ранее созданные нами модели данных из файла models.py

create_tables()   # Добавляем вызов функции

session = SessionLocal()    # Создаём локальную сессию

# Создаем функции для добавления департаментов, подразделений, сотрудников и получения всех депортаментов

def add_department(name: str):
    department = Department(name=name)
    session.add(department)
    session.commit()
    
    return department

def add_division(name: str, department_id: int):
    division = Division(name=name, department_id=department_id)
    session.add(division)
    session.commit()
    
    return division

def add_employee(name: str, division_id: int):
    employee = Employee(name=name, division_id=division_id)
    session.add(employee)
    session.commit()
    
    return employee

def get_all_departments():
    return session.query(Department).all()
    
# Добавляем департамент, подразделение, сотрудника и получаем все департаменты

if __name__ == "__main__":

    department = add_department(name="IT Department")  # Добавляем департамент
    print(f"Department added: {department.name}")

    division = add_division(name="Development", department_id=department.id)    # Добавляем подразделение
    print(f"Division added: {division.name}")

    employee = add_employee(name="John Doe", division_id=division.id)   # Добавляем сотрудника
    print(f"Employee added: {employee.name}")

    # Получаем все департаменты и выводим их на экран

    all_departments = get_all_departments()
    for dept in all_departments:
        print(f"Department: {dept.name}")
        for div in dept.divisions:
            print(f"Division: {div.name}")
            for emp in div.employees:
                print(f"Employee: {emp.name}")

    session.close()  # Закрываем локальную сессию



