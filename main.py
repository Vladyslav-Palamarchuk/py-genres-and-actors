import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet[Actor]:
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Drama")

    Actor.objects.create(first_name="George", last_name="Klooni")
    Actor.objects.create(first_name="Keanu", last_name="Reves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    drama_genre = Genre.objects.get(name="Drama")
    drama_genre.name = "Drama"
    drama_genre.save()

    george = Actor.objects.get(first_name="George", last_name="Klooni")
    george.last_name = "Clooney"
    george.save()

    keanu = Actor.objects.get(first_name="Keanu", last_name="Reves")
    keanu.last_name = "Reeves"
    keanu.save()

    Genre.objects.get(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
