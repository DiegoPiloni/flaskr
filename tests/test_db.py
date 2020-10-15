import sqlite3

import pytest

from flaskr.db import get_db


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)


def test_init_db_command(runner, mocker):
    mock_init_db = mocker.patch('flaskr.db.init_db')
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert mock_init_db.called
