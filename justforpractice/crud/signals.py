# from django.contrib.auth.models import User
# from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
# from django.dispatch import receiver
# from django.db.models.signals  import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate 
# from django.core.signals import request_started, request_finished, got_request_exception
# from django.db.backends.signals import connection_created

# # No need to memorize, just check this file and point it out to your receiver function.
# # Real world Examples : login user IP Address, 
# # login Count, Session store or cache store at time of user login succesfully, 
# # intro code while login by user, tracking of login failed by user, 
# # no of times login failed permission then user id get blocked

# @receiver(user_logged_in,sender = User)
# def login_success(sender,request,user,**kwargs): # Receiver Function
#     print('----------------------------')
#     print(f'------{user} Login Succesfully---')
#     print('Sender:',sender)
#     print('Request:',request)
#     print('User:',user)
#     print('kwargs:',f'{kwargs}')
# # user_logged_in.connect(login_success,sender = User)  

# @receiver(user_logged_out,sender = User)
# def logout_success(sender,user,request,**kwargs):
#     print('----------------------------')
#     print(f'------{user} Logout Succesfully---')
#     print('Sender:',sender)
#     print('Request:',request)
#     print('User:',user)
#     print('kwargs:',f'{kwargs}')  
# # user_logged_out.connect(logout_success, sender=User)


# @receiver(user_login_failed)
# def login_failed(sender,request,credentials,**kwargs):
#     print('----------------------------')
#     print(f'----- Login Failed---')
#     print('Sender:',sender)
#     print('Request:',request)
#     print('Credentials:', credentials)
#     print('kwargs:',f'{kwargs}')
# # user_login_failed.connect(login_failed)

# @receiver(pre_save, sender = User) # User or 'Post' Model class -> Doing Crud Operations
# def at_beginning_save(sender, instance, **kwargs):
#     print('----------------------------')
#     print(f'----- pre Save Signal---')
#     print('Sender:',sender)
#     print('kwargs:',f'{kwargs}')
#     print('Instance:', instance)
# # pre_save.connect(at_beginning_save,sender=User)

# @receiver(post_save,sender=User) # POST_SAVE --> When You Store new Data, so update in new Cache
# def at_ending_save(sender, instance, created, **kwargs):
#     if created:
#         print('----------------------------')
#         print(f'----- New Post Save Signal---')
#         print('Sender:',sender)
#         print('kwargs:',f'{kwargs}')
#         print('Instance:', instance)
#         print('Created:',created)
#     else: 
#         print('----------------------------')
#         print(f'----- Post Save Signal---')
#         print('Sender:',sender)
#         print('kwargs:',f'{kwargs}')
#         print('Instance:', instance)
# # post_save.connect(at_ending_save,sender=User)


# #----------pre-migrate & post_migrate at every app migrate this receiver function runs.

# @receiver(pre_migrate)
# def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
#     print('----------------------------')
#     print(f'---before install app---')
#     print('Sender:',sender)
#     print('App_config:',app_config)
#     print('Verbosity:',verbosity)
#     print('Interactive:',interactive)
#     print('Using:', using)
#     print('Plan:',plan)
#     print('Apps:',apps)
#     print('kwargs:',f'{kwargs}')
# #pre_migrate.connect(before_install_app)

# @receiver(post_migrate)
# def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
#     print('----------------------------')
#     print(f'---at_end_migrate_flush---')
#     print('Sender:',sender)
#     print('App_config:',app_config)
#     print('Verbosity:',verbosity)
#     print('Interactive:',interactive)
#     print('Using:', using)
#     print('Plan:',plan)
#     print('Apps:',apps)
#     print('kwargs:',f'{kwargs}')
# #post_migrate.connect(at_end_migrate_flush)

# #----------------pre_delete & post_delete when you delete any object from the POST request.

# @receiver(pre_delete, sender = User)
# def at_beginning_delete(sender, instance, **kwargs):
#     print('----------------------------')
#     print(f'--- pre Delete Signal---')
#     print('Sender:',sender)
#     print('kwargs:',f'{kwargs}')
#     print('Instance:', instance)
# # pre_delete.connect(at_beginning_delete,sender=User)

# @receiver(post_delete, sender = User)
# def at_ending_delete(sender, instance, **kwargs):
#     print('----------------------------')
#     print(f'--- post Delete Signal---')
#     print('Sender:',sender)
#     print('kwargs:',f'{kwargs}')
#     print('Instance:', instance)
# # post_delete.connect(at_ending_delete,sender=User)

# #------------- when you save automatically {pre_init & post_init } will run

# @receiver(pre_init, sender = User)
# def at_beginning_init(sender, *args, **kwargs):
#     print('----------------------------')
#     print(f'--- pre init Signal---')
#     print('Sender:',sender)
#     print('kwargs:',f'{kwargs}')
#     print('args:', f'{args}')
# # pre_init.connect(at_beginning_init,sender=User)

# @receiver(post_init, sender = User)
# def at_ending_init(sender, *args, **kwargs):
#     print('----------------------------')
#     print(f'--- post init Signal---')
#     print('Sender:',sender)
#     print('kwargs:',f'{kwargs}')
#     print('args:', f'{args}')
# # post_init.connect(at_ending_init,sender=User)

# #------------- when you want to show on request a data.

# @receiver(request_started)
# def at_beginning_request(sender, environ, **kwargs):
#     print('----------------------------')
#     print(f'--- request starts Signal---')
#     print('Sender:',sender)
#     print('kwargs:',f'{kwargs}')
#     print('environ:',environ )
# # request_started.connect(at_beginning_request)

# @receiver(request_finished)
# def at_ending_request(sender, **kwargs):
#     print('----------------------------')
#     print(f'--- request ending Signal---')
#     print('Sender:',sender)
#     print('kwargs:',f'{kwargs}')
# # request_finished.connect(at_ending_request)

# @receiver(got_request_exception) # this will run when exception occur like 10/0 in view.home view function.
# def at_exception_request(sender, request, **kwargs):
#     print('----------------------------')
#     print(f'--- request exception Signal---')
#     print('Sender:',sender)
#     print('request',request)
#     print('kwargs:',f'{kwargs}')
# # got_request_exception.connect(at_exception_request)

# #----------connection_created at every time database initiate this receiver function runs.

# @receiver(connection_created)
# def connect_db(sender, connection, **kwargs):
#     print('----------------------------')
#     print(f'--- Initial connection to the Database Signal---')
#     print('Sender:',sender)
#     print('Connection:',connection)
#     print('kwargs:',f'{kwargs}')
# # connection_created.connect(connect_db)