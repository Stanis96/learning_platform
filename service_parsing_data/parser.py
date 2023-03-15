import requests

from bs4 import BeautifulSoup

from .data_to_db import save_data_to_db


def get_all_pages() -> int:
    url: str = "https://codeforces.com/problemset/?order=BY_SOLVED_DESC"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    pagination = soup.find("div", {"class": "pagination"}).find_all("a")
    pages: str = pagination[-2].text
    return int(pages) + 1


def parse_data(number_page: int) -> list:
    url: str = (
        f"https://codeforces.com/problemset/page/{number_page}?order=BY_SOLVED_DESC&locale=ru"
    )
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    task_list = []
    tasks_table = soup.find("table", {"class": "problems"}).find_all("tr")
    for task in tasks_table[1:]:
        number_for_link = task.find("td", {"class": "id"}).find("a")
        number = task.find("td", {"class": "id"}).find("a").get_text().strip()
        title: str = task.find("div", {"style": "float: left;"}).find("a").text.strip()
        link: str = "https://codeforces.com/" + number_for_link.get("href")
        topic: list = [x.text for x in task.find_all("a", {"class": "notice"})]
        difficulty = task.find("span", {"title": "Сложность"})
        if difficulty:
            difficulty = int(difficulty.text)
        else:
            difficulty = 0
        count_solved = task.find("a", {"title": "Количество решивших задачу"})
        if count_solved:
            count_solved = int(count_solved.text[2:])
        else:
            count_solved = 0
        task_list.append(
            {
                "number": number,
                "title": title,
                "link": link,
                "topic": topic,
                "difficulty": difficulty,
                "count_solved": count_solved,
            }
        )
    return task_list


def parse_all_pages():
    pages = get_all_pages()
    task_list = []
    for page in range(1, pages):
        task_list += parse_data(page)
    save_data_to_db(task_list)
