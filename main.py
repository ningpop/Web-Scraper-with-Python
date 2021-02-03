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
from flask import Flask, render_template, request

app = Flask("SuperScrapper")

# @: decorator(데코레이터), 함수를 꾸며주는 역할
@app.route("/")
def home():
    return render_template("potato.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    return render_template("report.html", searchingBy=word, potato="sexy")


app.run(host="0.0.0.0")
