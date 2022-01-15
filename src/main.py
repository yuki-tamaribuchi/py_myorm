from framework.operates.migrations import migrate_all_model
migrate_all_model()

from models.users import Users
from models.entries import Entries


#users = Users().objects.create(username='yuki', handle='ゆうき')

#users = Users().objects.get(username="yuki")
#print(users)

