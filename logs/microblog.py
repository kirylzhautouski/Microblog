2020-02-17 12:59:59,326 ERROR: Exception on /reset_password_request [GET] [in /home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py:1891]
Traceback (most recent call last):
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/app/routes.py", line 167, in reset_password_request
    title='Reset Password', form=form)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/templating.py", line 138, in render_template
    ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/jinja2/environment.py", line 930, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/jinja2/environment.py", line 883, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/jinja2/environment.py", line 857, in _load_template
    template = self.loader.load(self, name, globals)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/jinja2/loaders.py", line 117, in load
    source, filename, uptodate = self.get_source(environment, name)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/templating.py", line 60, in get_source
    return self._get_source_fast(environment, template)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/templating.py", line 89, in _get_source_fast
    raise TemplateNotFound(template)
jinja2.exceptions.TemplateNotFound: reset_password_request.html
2020-02-17 13:01:47,904 INFO: Microblog startup [in /home/kiryl/dev/edupurposes/flask-tutorial/app/__init__.py:51]
2020-02-17 13:01:55,474 ERROR: Exception on /reset_password_request [POST] [in /home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py:1891]
Traceback (most recent call last):
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/app/routes.py", line 163, in reset_password_request
    send_password_reset_email(user)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/app/email.py", line 20, in send_password_reset_email
    token = user.get_reset_password_token()
  File "/home/kiryl/dev/edupurposes/flask-tutorial/app/models.py", line 61, in get_reset_password_token
    app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')
NameError: name 'app' is not defined
2020-02-17 13:02:15,157 INFO: Microblog startup [in /home/kiryl/dev/edupurposes/flask-tutorial/app/__init__.py:51]
2020-02-17 13:02:21,642 ERROR: Exception on /reset_password_request [POST] [in /home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py:1891]
Traceback (most recent call last):
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/app/routes.py", line 163, in reset_password_request
    send_password_reset_email(user)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/app/email.py", line 22, in send_password_reset_email
    sender=app.config['ADMINS'][0],
NameError: name 'app' is not defined
2020-02-17 13:02:30,655 INFO: Microblog startup [in /home/kiryl/dev/edupurposes/flask-tutorial/app/__init__.py:51]
2020-02-17 13:02:36,125 ERROR: Exception on /reset_password_request [POST] [in /home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py:1891]
Traceback (most recent call last):
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/app/routes.py", line 163, in reset_password_request
    send_password_reset_email(user)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/app/email.py", line 24, in send_password_reset_email
    text_body=render_template('email/reset_password.txt',
NameError: name 'render_template' is not defined
2020-02-17 13:02:49,806 INFO: Microblog startup [in /home/kiryl/dev/edupurposes/flask-tutorial/app/__init__.py:51]
