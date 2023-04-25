Feature 1:
# Fork and clone project alpha
# Create and activate virtual environment
# upgrade pip,
# install django, black, flake8, djhtml
# deactivate virtual env and reactivate
# pip freeze to generate requirments.txt file

Feature 2:
# django-admin startproject tracker
# python manage.py apps (accounts projects tasks)
# register in project settings under installed apps
# run migrations
# create superuser

Feature 3:
# Create Project model in Projects app
# name, description, members
# make migrations and migrate

Feature 4:
# Register Project model in Django admin site
# import Project from models
# create class for admin
# admin.site.register

Feature 5:
# Create ListView for project model
# register the view in app URLS with path "" and name="list_projects"
# register url in project urls that include urls
# create base.html and list.html to extend to it

Feature 6:
# redirect localhost to project lists page
# use redirect view in tracker urls and register name as home

Feature 7:
# create loginview and register in accounts urls
# include urls in tracker project with prefix accounts
# create template in accounts templates
# register login_redirect_url to home in tracker project settings

Feature 8:
# import loginrequiredmixin in projects views
# add to listview
# change queryset to filer where members = logged in user

Feature 9:
# create logoutview and register in accounts urls
# register logout_redirect_url to login in tracker project settings

Feature 10:
# import usercreationform, user, and login
# create function for signup
# create signup template in registration

Feature 11:
# create task model in tasks app
# with attributes: name, startedate, due date, iscompleted, project, assignee
# str method to set value of name property

Feature 12:
# import and register Task model in admin

Feature 13:
# create detailview for projects
# must be logged in so have loginrequiredmixin
# path <int:pk> and name show_project
# create template to show details and table of tasks
# update list template to show #of tasks for project
# add link to list template that takes you to detail view for a project

Feature 14:
# create a createview for project model
# fields: name description members
# must have loginrequiredmixin
# redirect to detail page after creation
# register in projects urls with name create_project
# create template and add link to list template that navigates to it

Feature 15:
# create a createview for task model
# fields: all but is_completed
# must have loginrequiredmixin
# redirect to detail page after creation
# register in tasks urls with name create_task
# create template and add link to detail template

Feature 16:
# create listview for task model
# filter by assignee = currently logged in user
# loginrequiredmixin required
# register view in tasks urls with name show_my_tasks
# create html template for list

Feature 17:
# create updateview for task model
# only for is_completed field
# redirect to listview for task
# register view in tasks urls <int:pk>/complete/ with name complete_task
# no template needed
# modify task listview template

Feature 18:
# pip install django-markdownify
# follow instructions from articles
# disable sanitation
# load markdownify
# replace p tag

Feature 19:
# Add header tag to base.html
# include nav tag with list of links
# if user is authenticated: show my tasks, my projects, and logout
# else: show login, signup
