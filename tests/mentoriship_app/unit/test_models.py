from mentorship_app.domain.models import Mentor


def test_mentor_creation():
    mentor = Mentor(name="Leandro", speciality="Software Engineering")
    assert mentor.name == "Leandro"
    assert mentor.id is None
