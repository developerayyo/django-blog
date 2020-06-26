from storages.backends.azure_storage import AzureStorage
import os
import dotenv
from mysite.settings import BASE_DIR

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)


class AzureMediaStorage(AzureStorage):
    account_name = 'mydjangoaccountstorage' # Must be replaced by your <storage_account_name>
    account_key = os.getenv("account_key") # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

# class AzureStaticStorage(AzureStorage):
#     account_name = 'djangoaccountstorage' # Must be replaced by your storage_account_name
#     account_key = 'your_key_here' # Must be replaced by your <storage_account_key>
#     azure_container = 'static'
#     expiration_secs = None