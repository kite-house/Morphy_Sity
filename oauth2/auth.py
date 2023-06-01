from django.contrib.auth.backends import BaseBackend
from .models import Users

class AuthorizationUserDiscord(BaseBackend):
    def authenticate(self, request ,user) -> Users:
        find_user = Users.objects.filter(discord_id=user['id'])
        if len(find_user) == 0:
            return None
        
        else:
            self.get_access(find_user,user)
            return find_user

    def get_user(self, user_id):
        try:
            return Users.objects.get(pk = user_id)
        except Users.DoesNotExist:
            return None

    def get_access(self, find_user, user) -> Users:
        if user['id'] == '343339732975091714':
            find_user.update(access = 'developer')
            return
            
        roles = Users.objects.values_list('roles', flat=True).filter(discord_id=user['id'])                                             
        for roles in roles:
            roles = roles.replace('[', '').replace(']', '').split(',')
            for role in roles:
                if role == '<@&879382113491779604>' or role == "<@&930434804170760192>":
                    find_user.update(access = 'moderator')
                    return
                
                if role == '<@&879394956802940958>':
                    find_user.update(access = 'member')
                    return
            
            find_user.update(access = 'guest')
            return 
