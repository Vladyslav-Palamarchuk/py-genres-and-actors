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
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors_to_create:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # 3. Оновлення жанру "Dramma" до "Drama"
    drama_genre = Genre.objects.get(name="Dramma")
    drama_genre.name = "Drama"
    drama_genre.save()

    # 4. Оновлення прізвища Джорджа Клуні ("Klooney" -> "Clooney")
    george = Actor.objects.get(first_name="George", last_name="Klooney")
    george.last_name = "Clooney"
    george.save()

    # 5. Оновлення Кіану Рівза ("Kianu Reaves" -> "Keanu Reeves")
    keanu = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    keanu.first_name = "Keanu"
    keanu.last_name = "Reeves"
    keanu.save()

    # 6. Видалення жанру "Action" та акторок "Scarlett"
    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # 7. Повернення відфільтрованого та відсортованого набору запитів
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
