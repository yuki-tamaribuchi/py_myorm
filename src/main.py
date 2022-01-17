#テーブル作成サンプル
#from framework.operates.migrations import migrate_all_model
#migrate_all_model()

from models.users import Users
from models.entries import Entries

#インサートサンプル
Users().objects.create(username='yuki', handle='ゆうき').run()

#WHERE条件(1つ)指定セレクトサンプル
#users = Users().objects.get(username="yuki").run()
#print(users)

#WHERE条件(2つ)指定セレクトサンプル
#users = Users().objects.get(username="yuki", handle="ゆうき").run()
#print(users)

#WHERE条件3(つ)指定セレクトサンプル
#users = Users().objects.get(username="sampleuser", handle="sample user", id=1).run()
#print(users)

#全セレクトサンプル
#users = Users().objects.all().run()
#print(users)