""" only indeed scrapping """
# from indeed import extract_indeed_pages, extract_indeed_jobs

# last_indeed_page = extract_indeed_pages()
# indeed_jobs = extract_indeed_jobs(last_indeed_page)
# print(indeed_jobs)

""" stackoverflow scrapping """
# from indeed import get_jobs as get_indeed_jobs
# from so import get_jobs as get_so_jobs
# from save import save_to_file

# so_jobs = get_so_jobs()
# indeed_jobs = get_indeed_jobs()
# jobs = so_jobs + indeed_jobs
# save_to_file(jobs)

""" Web Scrapper with Flask """
from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")

db = {}

# @: decorator(데코레이터), 함수를 꾸며주는 역할
@app.route("/")
def home():
    return render_template("potato.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html",
        searchingBy=word,
        resultsNumber=len(jobs),
        jobs=jobs
    )

@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        return f"Generate CSV for {word}"
    except:
        return redirect("/")


app.run(host="0.0.0.0")
