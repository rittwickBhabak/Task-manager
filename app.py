from myproject import app, db
from flask import Flask, render_template, request, url_for, redirect, flash , abort 
from flask_login import login_user, login_required, logout_user 
from myproject.models import User, Task, Revesion
from myproject.forms import LoginForm, SignUpForm, NewTaskForm, EditTask