from flask import Blueprint, render_template, url_for
from jinja2 import FileSystemLoader

import os
from os import path
import re
from datetime import date
from operator import itemgetter

root_dir = path.join(path.dirname(__file__), path.pardir)
# dirname(__file__) is the hacksoc_org python module folder
# its parent is the git repository root, directly under which the static/, and template/ folders lie

blueprint = Blueprint(
    "routes",
    __name__,
    template_folder=path.join(root_dir, "templates/"),
    static_folder=path.join(root_dir, "static"),
)

@blueprint.route("/<string:page>.html")
def render_page(page : str):
    return render_template(f"content/{page}.html.jinja2") # TODO: .jinja2

@blueprint.route("/")
def index():
    return render_page("index")

@blueprint.route("/servers/<string:page>.html")
def render_server_page(page: str):
    raise NotImplemented

@blueprint.route("/minutes.html")
def render_minutes():
    # TODO: check flask priority resolution -- does render_page need to go below this?

    re_filename = re.compile(r"^(\d{4}-[01]\d-[0123]\d)-(.*)\.pdf$")

    minutes_listing = []
    for filename in os.listdir(path.join(root_dir, "static", "minutes")):
        match = re_filename.match(filename)
        if match is None: continue

        try:
            minutes_listing.append({
                'date': date.fromisoformat(match[1]),
                'meeting': match[2],
                'url': url_for('.static', filename=f"minutes/{filename}")
            })
        except ValueError as e:
            print(f"Error while parsing {filename}:")
            print(e)
            print("Document will be skipped.")
            continue
    
    minutes_listing.sort(key=itemgetter('date'))

    return render_template(f"content/minutes.html.jinja2", minutes=minutes_listing)