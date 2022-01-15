from framework.operates.migrations import migrate_all_model
#migrate_all_model()

from models.users import Users


#users = Users().objects.create(username='yuki', handle='ゆうき')

users = Users().objects.get(username="yuki")
print(users)