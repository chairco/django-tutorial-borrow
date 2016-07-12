from django.shortcuts import render
from django.http import HttpResponse


class ActiveDirectoryBackend:

    def authenticate(self, username=None, password=None):
        try:
            if len(password) == 0:
                return None
            s = Server('ldap://ldap.pegatroncorp.com', port=389, get_info=None)  # define an unsecure LDAP server, requesting info on DSE and schema
            c = Connection(s, 
                       auto_bind = True, 
                       client_strategy = STRATEGY_SYNC, 
                       user = username + '@pegatroncorp.com', 
                       password = password, 
                       authentication = AUTH_SIMPLE, 
                       check_names = True)
            c.unbind()
            return self.get_or_create_user(username, password)
        except:
            return None

    def get_or_create_user(self, username, password):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            info=sys.exc_info()  
            print(info[0],":",info[1])
            print(username)
            mail = username + '@pegatroncorp.com'
            user = User(username=username,email=mail)
            user.is_staff = True
            user.is_superuser = False
            user.set_password('ldap a authenticated')
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None #其中域控服务器和用户名，邮箱地址根据实际情况修改。 


def adddri_pega(request):
    from .models import Pegadri
    from .forms import AddpegadriForm
    
    if request.method == 'POST':
        formp = AddpegadriForm(request.POST)
        if formp.is_valid():
            post = formp.save(commit=False)
            post.author = request.user
            post.owner = request.user
            post.save()
            
            select_id = Pegadri.objects.filter(name=post.name) #get the user id from db
            select_id = select_id[len(select_id)-1].id
            return HttpResponse(select_id)
    return HttpResponse("False")


def adddri_coco(request):
    from .models import Cocodri
    from .forms import AddcocodriForm

    if request.method == 'POST':
        formc = AddcocodriForm(request.POST)
        if formc.is_valid():
            post = formc.save(commit=False)
            post.author = request.user
            post.owner = request.user
            post.save()
            
            select_id = Cocodri.objects.filter(name=post.name) # get the user id from db
            select_id = select_id[len(select_id)-1].id
            return HttpResponse(select_id)
    return HttpResponse("False")