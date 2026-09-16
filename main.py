import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet[Actor]:
    # 1. Створення жанрів через список і цикл
    genres_to_create = ["Western", "Action", "Dramma"]
    for genre_name in genres_to_create:
        Genre.objects.create(name=genre_name)

    # 2. Створення акторів через список кортежів та цикл
    actors_to_create = [
        ("George", "Klooni"),
        ("Keanu", "Reves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors_to_create:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # 3. Оновлення
    # Оновлюємо жанр "Dramma" до "Drama"
    drama_genre = Genre.objects.get(name="Dramma")
    drama_genre.name = "Drama"
    drama_genre.save()

    # Оновлюємо прізвище Джорджа Клуні
    george = Actor.objects.get(first_name="George", last_name="Klooni")
    george.last_name = "Clooney"
    george.save()

    # Оновлюємо прізвище Кіану Рівза
    keanu = Actor.objects.get(first_name="Keanu", last_name="Reves")
    keanu.last_name = "Reeves"
    keanu.save()

    # 4. Видалення
    # Видаляємо жанр Action
    Genre.objects.get(name="Action").delete()

    # Видаляємо всіх акторок з ім'ям "Scarlett"
    Actor.objects.filter(first_name="Scarlett").delete()

    # 5. Повернення результату
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
