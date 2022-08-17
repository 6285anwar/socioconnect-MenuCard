from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'socioconnects' # Must be replaced by your <storage_account_name>
    account_key = '0fw0eut4bsu51s1Nb+LUB9I1KEWuMrmOqqI1IXYv3qyJ4Vg6k7xT0VUXEFyvuUKB6m+zXdg+zWvM+AStpDs2QQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'djangoaccountstorage' # Must be replaced by your storage_account_name
    account_key = 'your_key_here' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None