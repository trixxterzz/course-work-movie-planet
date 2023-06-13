from flask import Flask, request, flash, get_flashed_messages, render_template, redirect, session
import tmdbsimple as tmdb
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
import urllib.parse
import requests

def login_required(f):
    @wraps(f)
    def func(*args, **kwargs):
        if session.get("user_id") == None:
            return redirect("/login")
        else: 
            return f(*args, **kwargs)
    return func

