2020-02-18 09:30:13,798 ERROR: Exception on /index [GET] [in /home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/app.py:1891]
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
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask_login/utils.py", line 272, in decorated_view
    return func(*args, **kwargs)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/app/routes.py", line 43, in index
    next_url=next_url, prev_url=prev_url)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/templating.py", line 140, in render_template
    ctx.app,
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask/templating.py", line 120, in _render
    rv = template.render(context)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/jinja2/environment.py", line 1090, in render
    self.environment.handle_exception()
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/jinja2/environment.py", line 832, in handle_exception
    reraise(*rewrite_traceback_stack(source=source))
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/jinja2/_compat.py", line 28, in reraise
    raise value.with_traceback(tb)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/app/templates/index.html", line 2, in top-level template code
    {% import 'bootstrap/wtf.html' as wtf %}
  File "/home/kiryl/dev/edupurposes/flask-tutorial/app/templates/base.html", line 1, in top-level template code
    {% extends 'bootstrap/base.html' %}
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask_bootstrap/templates/bootstrap/base.html", line 1, in top-level template code
    {% block doc -%}
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask_bootstrap/templates/bootstrap/base.html", line 3, in block "doc"
    <html{% block html_attribs %}{% endblock html_attribs %}>
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask_bootstrap/templates/bootstrap/base.html", line 11, in block "html"
    {%- endblock metas %}
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/flask_bootstrap/templates/bootstrap/base.html", line 13, in block "body"
    {%- block styles %}
  File "/home/kiryl/dev/edupurposes/flask-tutorial/app/templates/base.html", line 48, in block "content"
    {% block app_content %}{% endblock %}
  File "/home/kiryl/dev/edupurposes/flask-tutorial/app/templates/index.html", line 11, in block "app_content"
    {% include '_post.html' %}
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/jinja2/environment.py", line 832, in handle_exception
    reraise(*rewrite_traceback_stack(source=source))
  File "/home/kiryl/dev/edupurposes/flask-tutorial/env/lib/python3.6/site-packages/jinja2/_compat.py", line 28, in reraise
    raise value.with_traceback(tb)
  File "/home/kiryl/dev/edupurposes/flask-tutorial/app/templates/_post.html", line 15, in template
    {% comment %} {% if post.language and post.language != g.locale %} {% endcomment %}
jinja2.exceptions.TemplateSyntaxError: Encountered unknown tag 'comment'.
2020-02-18 09:31:08,115 INFO: Microblog startup [in /home/kiryl/dev/edupurposes/flask-tutorial/app/__init__.py:60]
