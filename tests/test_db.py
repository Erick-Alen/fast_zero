from sqlalchemy.sql import select

from fast_zero.models import Todo, User


def test_create_user_without_todos(session):
    new_user = User(
        username='alice', password='secret', email='teste@example.com'
    )
    session.add(new_user)
    session.commit()
    user = session.scalar(select(User).where(User.username == 'alice'))

    assert user.username == 'alice'


def test_create_todo(session, user: User):
    todo = Todo(
        title='Test todo',
        description='Test todo description',
        state='draft',
        user_id=user.id,
    )
    session.add(todo)
    session.commit()
    session.refresh(todo)
    user = session.scalar(select(User).where(User.id == user.id))

    assert todo in user.todos
