from .models import Department
def department_links(request):
    departments = Department.objects.all()
    department_links = [(department.name, department.wikipedia_link) for department in departments]

    return {'department_links': department_links}
