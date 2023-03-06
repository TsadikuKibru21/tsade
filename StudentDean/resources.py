from import_export import resources
from account.models import User

class UserResource(resources.ModelResource):
    class Meta:
        model=User