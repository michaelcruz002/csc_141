
# 9-12 Multiple Modules: Import Admin from another module.
from admin import Admin

admin = Admin("Alex", "Smith")

admin.greet_user()
admin.privileges.show_privileges()
