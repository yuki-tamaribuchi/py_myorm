from framework.operates.migrations import migrate_all_model
#migrate_all_model()

from models.users import Users

users = Users()
#users.objects.create(
#	username='sampleuser',
#	handle='sample user'
#)

users = users.objects.get(username="sampleuser")
print(users)