
# 9-11 Imported Admin: Import Admin and show its privileges.
from users import Admin

admin = Admin("Alex", "Smith")

admin.greet_user()
admin.privileges.show_privileges()
