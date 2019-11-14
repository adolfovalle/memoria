import sys
import facebook_business
sys.path.append() # Replace this with the place you installed facebookads using pip
sys.path.append() # same as above

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business import adobjects

my_app_id = 
my_app_secret = 
my_access_token = 
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount()

campaigns = my_account.get_campaigns()
print(campaigns)
print(dir(facebook_business.adobjects.campaign.Campaign))

# fields = []
# params = {
#   adobjects.campaign.Campaign.Field.name : 'Conversions Campaign',
#   adobjects.campaign.Campaign.Field.configured_status: adobjects.campaign.Campaign.Status.paused,
#   adobjects.campaign.Campaign.Field.objective : 'LINK_CLICKS',
# }
# campaign = my_account.create_campaign(fields, params)

# campaigns = my_account.get_campaigns()
# print(campaigns)
account_data = my_account.api_get(fields=[adobjects.adaccount.AdAccount.Field.amount_spent])
print(account_data)