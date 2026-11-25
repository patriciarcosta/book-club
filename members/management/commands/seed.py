from datetime import date

from django.core.management.base import BaseCommand
from django.db import transaction

from members.models import Book, Member, ReadingLog

BOOKS = [
    ("Os Maias", "Eça de Queirós", 720, 1888),
    ("Ensaio sobre a Cegueira", "José Saramago", 336, 1995),
    ("O Livro do Desassossego", "Fernando Pessoa", 544, 1982),
    ("Cem Anos de Solidão", "Gabriel García Márquez", 448, 1967),
    ("1984", "George Orwell", 328, 1949),
    ("Orgulho e Preconceito", "Jane Austen", 432, 1813),
    ("O Principezinho", "Antoine de Saint-Exupéry", 96, 1943),
    ("Dom Casmurro", "Machado de Assis", 256, 1899),
]

MEMBERS = [
    # firstname, lastname, email, phone, joined_date, favorite_book
    ("Ana", "Silva", "ana.silva@example.com", 912345678, date(2025, 1, 15), "Os Maias"),
    ("João", "Ferreira", "joao.ferreira@example.com", 913456789, date(2025, 3, 2), "1984"),
    ("Marta", "Costa", "marta.costa@example.com", 914567890, date(2025, 6, 20), "Cem Anos de Solidão"),
    ("Rui", "Pereira", "rui.pereira@example.com", 915678901, date(2025, 9, 8), "Ensaio sobre a Cegueira"),
    ("Inês", "Santos", "ines.santos@example.com", 916789012, date(2026, 2, 11), "O Principezinho"),
]

READINGS = [
    # (member firstname, book title, date finished)
    ("Ana", "Os Maias", date(2025, 4, 10)),
    ("Ana", "O Principezinho", date(2025, 5, 2)),
    ("Ana", "Dom Casmurro", date(2026, 1, 18)),
    ("João", "1984", date(2025, 4, 25)),
    ("João", "Ensaio sobre a Cegueira", date(2025, 11, 3)),
    ("Marta", "Cem Anos de Solidão", date(2025, 8, 14)),
    ("Marta", "Orgulho e Preconceito", date(2026, 3, 9)),
    ("Rui", "Ensaio sobre a Cegueira", date(2025, 12, 1)),
    ("Inês", "O Principezinho", date(2026, 4, 22)),
]


class Command(BaseCommand):
    help = "Popula a base de dados com membros, livros e leituras de exemplo."

    @transaction.atomic
    def handle(self, *args, **options):
        books = {}
        for title, author, pages, year in BOOKS:
            book, _ = Book.objects.get_or_create(
                title=title,
                author=author,
                defaults={"pages": pages, "published_year": year},
            )
            books[title] = book

        members = {}
        for first, last, email, phone, joined, fav in MEMBERS:
            member, _ = Member.objects.get_or_create(
                firstname=first,
                lastname=last,
                defaults={
                    "email": email,
                    "phone": phone,
                    "joined_date": joined,
                    "favorite_book": fav,
                },
            )
            members[first] = member

        for first, title, finished in READINGS:
            ReadingLog.objects.get_or_create(
                member=members[first],
                book=books[title],
                defaults={"date_finished": finished},
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Pronto: {Member.objects.count()} membros, "
                f"{Book.objects.count()} livros, "
                f"{ReadingLog.objects.count()} leituras."
            )
        )
