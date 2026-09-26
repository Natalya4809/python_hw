import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

db_connection_string = os.getenv("DATABASE_URL")
if not db_connection_string:
    raise RuntimeError("Не найдена переменная DATABASE_URL в .env")

db = create_engine(db_connection_string)


def test_update_teacher():
    email = "vika1234@gmail.ru"
    teacher_id_val = 34993

    # добавляю учителя
    with db.connect() as conn:
        conn.execute(
            text(
                "INSERT INTO teacher (teacher_id, email) VALUES (:teacher_id, :email)"
            ),
            {"teacher_id": teacher_id_val, "email": email},
        )

        # ищу по email

        row = conn.execute(
            text("SELECT teacher_id, email FROM teacher WHERE email = :email"),
            {"email": email},
        ).fetchone()

        assert row is not None, "Учитель не добавился — строка не найдена"

        assert row[1] == email

        # Вносим изменения
        conn.execute(
            text(
                "UPDATE teacher SET email = :new_email WHERE teacher_id = :teacher_id"
            ),
            {"new_email": "vikanew@example.com", "teacher_id": teacher_id_val},
        )

        # удаляем учителя

        conn.execute(
            text("DELETE FROM teacher WHERE teacher_id = :teacher_id"),
            {"teacher_id": teacher_id_val},
        )
