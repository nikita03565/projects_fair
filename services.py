from projects.models import Project, Participation


def get_courses_in_which_user_has_been_enrolled_as_student(user):
    return Project.objects.filter(
        participations__user=user,
        participations__role=Participation.ROLE_STUDENT
    )


def get_courses_in_which_user_has_been_enrolled_as_teacher(user):
    return Project.objects.filter(
        participations__user=user,
        participations__role=Participation.ROLE_TEACHER
    )


def get_project_teachers(project):
    return project.participants.filter(
        participations__role=Participation.ROLE_TEACHER
    )


def get_project_students(project):
    return project.participants.filter(
        participations__role=Participation.ROLE_STUDENT
    )
