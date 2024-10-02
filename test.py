import pytest
from main import get_random_cat_image


def test_get_random_cat_image_success(mocker):
    # Мокируем requests.get
    mock_get = mocker.patch('main.requests.get')

    # Устанавливаем успешный статус код и возвращаемое значение
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {
            'id': 'd08',
            'url': 'https://cdn2.thecatapi.com/images/d08.jpg',
            'width': 468,
            'height': 665
        }
    ]

    # Вызываем функцию
    cat_image_data = get_random_cat_image()

    # Проверяем, что функция возвращает правильный объект
    assert cat_image_data == {
        'id': 'd08',
        'url': 'https://cdn2.thecatapi.com/images/d08.jpg',
        'width': 468,
        'height': 665
    }


def test_get_random_cat_image_failure(mocker):
    # Мокируем requests.get
    mock_get = mocker.patch('main.requests.get')

    # Устанавливаем неуспешный статус код
    mock_get.return_value.status_code = 404

    # Вызываем функцию
    cat_image_data = get_random_cat_image()

    # Проверяем, что функция возвращает None
    assert cat_image_data is None
