# from django.db.models.signals import pre_save,post_save,pre_delete,post_delete,pre_init,post_init,pre_migrate,post_migrate
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
# , user_logged_in, user_logged_out, user_login_failed,  user_password_changed, user_set_password, user_email_confirmed

@receiver(user_signed_up)
def handle_user_signed_up(request,sociallogin,user,**kwargs):
    new_user=sociallogin.account.extra_data
   