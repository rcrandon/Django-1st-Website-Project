# Django-1st-Website-Project

## Table of Contents:
#### Criteria List 
Running Tests

Useful Commands

## Criteria List

1. This is a Django application. You need to create a new virtual environment and install the dependencies for Django and software development.

    Fork and clone the starter project from Project Alpha
    Create a new virtual environment in the repository directory for the project
    Activate the virtual environment
    Upgrade pip
    Install django
    Install black
    Install flake8
    Install djlint
    Deactivate your virtual environment
    Activate your virtual environment
    Use pip freeze to generate a requirements.txt file

2. This Django application needs to have a Django project named tracker and three Django apps named accounts, projects, and tasks. Those three Django apps need to be properly installed in the Django project so it can find them.

In the repository directory:

    Create a Django project named tracker so that the manage.py file is in the top directory
    Create a Django app named accounts and install it in the tracker Django project in the INSTALLED_APPS list
    Create a Django app named projects and install it in the tracker Django project in the INSTALLED_APPS list
    Create a Django app named tasks and install it in the tracker Django project in the INSTALLED_APPS list
    Run the migrations
    Create a super user

3. This feature is for you to create a Project model in the projects Django app.

The Project model should have the following attributes:
(Name| Type| Constraints)

description |	string | no maximum length

owner | foreign key to User | Refers to the auth.User model, related name "projects", on delete cascade, null is True


Once you have the Project model defined with its attributes, write a def __str__(self) method that returns the name of the project.

4. Register the Project model with the admin so you can see it in the Django admin site.

5.This feature is about creating a list view for the Project model, registering the view for a path, registering the projects paths with the tracker project, and creating a template for the view.

    Create a view that will get all of the instances of the Project model and put them in the context for the template.
    Register that view in the projects app for the path "" and the name "list_projects" in a new file named projects/urls.py.
    Include the url patterns from the projects app in the tracker project with the prefix "projects/".
    Create a template for the list view that complies with the following specifications.

Template specifications

The resulting HTML from a request to the path http://localhost:8000/projects/ should result in HTML that has:

    the fundamental five in it
    a main tag that contains:
        a div tag that contains:
            an h1 tag with the content "My Projects"
            if there are no projects created, then:
                a p tag with the content "You are not assigned to any projects"
            otherwise:
                a table that has two columns:
                    the first with the header "Name" and the rows with the names of the projects
                    the second with the header "Number of tasks" and nothing in those rows because we don't yet have tasks
                    
6. This feature is about redirecting http://localhost:8000/ to the project list page created in Feature 5.

In the tracker urls.py, write a function to redirect from "" to the name of path for the list view that you created in the previous feature. Register that path a name of "home".

7. This feature is about setting up a login page so the person using the application can be identified.

Make sure you have a super user created so you can log in to test the feature.

All of this code should happen in the accounts Django app!

    Create a Django form that has username and password attributes, both of type CharField with max lengths of 150. Make sure the password attribute uses the PasswordInput widget.
    Create a view function that will show the login form for an HTTP GET, and try to log the person in for an HTTP POST.
    If the person is successfully logged in, you should redirect them to the list of projects.
    Register the view in the with the path "login/" and the name "login".
    Include the url patterns from the accounts app in the tracker project with the prefix "accounts/".
    Create a templates directory under accounts.
    Create an accounts directory under templates.
    Create an HTML template named login.html in the accounts directory.
    Render the form in the login.html. Make sure to put the required HTML, security tags, or template inheritance stuff that you need to make it a valid Web page with the fundamental five (see specifications below).

Template specifications

The resulting HTML from a request to the path http://localhost:8000/accounts/login/ should result in HTML that has:

    the fundamental five in it:
    a main tag that contains:
        a div tag that contains:
            an h1 tag with the content "Login"
            a form tag with method "post" that contains any kind of HTML structures but must include:
                your rendered form
                a button with the content "Login"
                
8. This feature requires someone to log in before accessing the list view for the projects. It also constrains the result set of projects to those that the person is a member of.

    Protect the list view for the Project model so that only a person who has logged in can access it.
    Change the queryset of the view to filter the Project objects where members equals the logged in user. That means instead of .all(), we want to use .filter(owner=request.user).

9. In the accounts Django app:

    Create a function view that logs out a user and redirects them to the login page
    In the accounts/urls.py file:
        Import the that view you just created
        Register that view in your urlpatterns list with the path "logout/" and the name "logout"

10. This feature allows people to sign up for the project tracker.

You need to create a function view to handle showing the signup form and handle its submission. This is a view, so you should create it in the file in the accounts directory that should hold the views.

    Create a sign-up form with the following fields:
        username that has a max length of 150 characters
        password that has a max length of 150 characters and uses a PasswordInput
        password_confirmation that has a max length of 150 characters and uses a PasswordInput
    Create a view function that will show the login form for an HTTP GET, and try to create a new user for an HTTP POST.
    If the password and password_confirmation do not match, then the User should not be created and there should be an error that reads "the passwords do not match"
    If the account is created, you should redirect them to the list of projects.
    You'll need to use the special create_user method to create a new user account from their username and password.
    You'll need to use the login function that logs an account in.
    Create an HTML template named signup.html in the registration directory.
    Render the form in the signup.html. Make sure to put the required HTML, security tags, or template inheritance stuff that you need to make it a valid Web page with the fundamental five (see specifications below).

Template specifications

The resulting HTML from a request to the path http://localhost:8000/accounts/signup/ should result in HTML that has:

    the fundamental five in it
    a main tag that contains:
        a div tag that contains:
            an h1 tag with the content "Signup"
            a form tag with method "post" that contains any kind of HTML structures but must include:
                your rendered form
                a button with the content "Signup"

11. This feature is for you to create a Task model in the tasks Django app.

The Task model should have the following attributes(Name | Type | Constraints):

name 	| string 	| maximum length of 200 characters

start_date |	date-time 	

due_date | 	date-time

is_completed |	Boolean |	default value should be False

project |	foreign key |	Refers to the projects.Project model, related name "tasks", on delete cascade

assignee |	foreign key |	Refers to the auth.User model, null is True, related name "tasks", on delete cascade

12. Register the Task model with the admin so you can see it in the Django admin site. You want to do this in the tasks Django app's admin.py.

13. This feature allows people to see the details about a project.

    Create a view that shows the details of a particular project.
    A user must be logged in to see the view.
    In the projects urls.py file, register the view with the path "<int:id>/" and the name "show_project".
    Create a template to show the details of the project and a table of its tasks.
    Update the list template to show the number of tasks for a project using the |length filter like project.tasks.all|length
    Update the list template to have a link from the project name to the detail view for that project.

Template specifications

There is one template to create and one to modify.
Project detail view

The project detail view should render to HTML that has the following structure:

    the fundamental five in it
    a main tag that contains:
        a div tag that contains:
            an h1 tag with the project's name as its content
            a p tag with the project's description in it
            an h2 tag that has the content "Tasks"
            if the project has tasks, then:
                a table that contains five columns with the headers "Name", "Assignee", "Start date", "Due date", and "Is completed" with rows for each task in the project. For each row, show the details of a task:
                    The "Name" column has the task's name
                    The "Assignee" column has the assignee's username
                    The "Start date" column has the task's start date
                    The "Due date" column has the task's due date
                    Use the |yesno filter without any arguments to output "yes" or "no" if the task is completed or not
            otherwise:
                a p tag with the content "This project has no tasks"

Note: The "Is completed" column shows "yes" and "no" for the task is_completed status.

14. This feature allows a person to go from the project list page to a page that allows them to create a new project.

    Create a create view for the Project model that will show the name, description, and owner properties in the form and handle the form submission to create a new Project. (You may want to use a ModelForm.)
    A person must be logged in to see the view.
    If the project is successfully created, it should redirect to the list of projects.
    Register that view for the path "create/" in the projects urls.py and the name "create_project".
    Create an HTML template that shows the form to create a new Project (see the template specifications below).
    Add a link to the list view for the Project that navigates to the new create view.

Template specifications

There are two templates that need to be changed or created.
The create form

The resulting HTML from a request to the path http://localhost:8000/projects/create/ should result in HTML that has:

    the fundamental five in it
    a main tag that contains:
        a div tag that contains:
            an h1 tag with the content "Create a new project"
            a form tag with method "post" that contains any kind of HTML structures but must include:
                any security stuff
                the rendered form in it
                a button with the content "Create"


The project list view

You need to add a link to this create page on the project list view after the h1 tag and before the table. The HTML that you add should be inside the div tag, after the h1 tag, and be:

    a p tag that contains:
        an a tag with an href attribute that points to the create project URL and has content "Create a new project"

15. This feature is about creating a create view for the Task model, registering the view for a path, registering the tasks paths with the tracker project, and creating a template for the view.

All of this code should be written in the tasks Django app.

    Create a view that will show a form to create an instance of the Task model for all properties except the is_completed field. (You may want to use a ModelForm.)
    In this view, you do not assign the owner of the task. This means that you will use form.save() rather than form.save(False).
    The view must only be accessible by people who are logged in.
    When the view successfully handles the form submission, have it redirect to the list of projects
    Register that view in the tasks app for the path "create/" and the name "create_task" in a new file named tasks/urls.py.
    Include the URL patterns from the tasks app in the tracker project with the prefix "tasks/".
    Create a template for the create view that complies with the following specifications.
    Add a link to create a task from the project detail page that complies with the following specifications.

Template specifications

Two templates need either creation or modification.
Create form for Task

The resulting HTML from a request to the path http://localhost:8000/tasks/create/ should result in HTML that has:

    the fundamental five in it
    a main tag that contains:
        a div tag that contains:
            an h1 tag with the content "Create a new task"
            a form tag with method "post" that contains any kind of HTML structures but must include:
                any security stuff
                the rendered form in it
                a button with the content "Create"

16. This feature allows a logged in person to see the tasks that are assigned to them.

    Create a list view for the Task model with the objects filtered so that the person only sees the tasks assigned to them by filtering with the assignee equal to the currently logged in user.
    The view must only be accessible by people who are logged in.
    Register that view in the tasks app for the path "mine/" and the name "show_my_tasks" in the tasks urls.py file.
    Create an HTML template that conforms with the following specifications.

Template specifications

The resulting HTML from a request to the path http://localhost:8000/tasks/mine/ should result in HTML that has:

    the fundamental five in it
    a main tag that contains:
        a div tag that contains:
            an h1 tag with the content "My Tasks"
            if there are tasks assigned to the person:
                a table with the headers "Name", "Start date", "Due date", "Is completed" and a row for each task that is assigned to the logged in person
                In the last column, if the task is completed, it should show the word "yes", otherwise, it should show "no" (You can use the |yesno filter for this)
            otherwise:
                a p tag with the content "You have no tasks"

17. In this feature, you'll add some navigation to the Web application. Hopefully, you've used template inheritance so that you can just do this in one place. Otherwise, you'll need to add the HTML to all of the places.
Template specification

On all HTML pages, add:

    a header tag as the first child of the body tag before the main tag that contains:
        a header tag that contains
            a nav tag that contains:
                a ul tag that contains:
                    if the person is logged in:
                        an li tag that contains:
                            an a tag with an href to the "show_my_tasks" path with the content "My tasks"
                        an li tag that contains:
                            an a tag with an href to the "list_projects" path with the content "My projects"
                        an li tag that contains:
                            an a tag with an href to the "logout" path with the content "Logout"
                    otherwise:
                        an li tag that contains:
                            an a tag with an href to the "login" path with the content "Login"
                        an li tag that contains:
                            an a tag with an href to the "signup" path with the content "Signup"
