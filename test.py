robot = {
    "001": {
        "name": "base.start",
        "title": "Начало работы",
        "next": "002",
        "args": {},
    },
    "009": {
        "name": "base.finish",
        "title": "Завершение работы",
        "next": None,
        "args": {},
    },
    "002": {
        "name": "base.console_output",
        "title": "Вывод в консоль",
        "next": "003",
        "args": {"entry": "Начало работы", "level": "debug"},
    },
    "004": {
        "name": "excel.read_range",
        "title": "Прочитать диапазон",
        "next": "005",
        "args": {},
    },
    "003": {
        "name": "excel.open_file",
        "title": "Открытие файла",
        "next": "004",
        "args": {"path": "path/to/file.xlsx"},
    },
    "005": {
        "name": "base.console_output",
        "title": "Вывод в консоль",
        "next": "006",
        "args": {"entry": "Прочитали диапазон", "level": "debug"},
    },
    "007": {
        "name": "excel.close_file",
        "title": "Закрытие файла",
        "next": "008",
        "args": {},
    },
    "006": {
        "name": "excel.save_file",
        "title": "Сохранение файла",
        "next": "007",
        "args": {},
    },
    "008": {
        "name": "base.console_output",
        "title": "Вывод в консоль",
        "next": "009",
        "args": {"entry": "Конец работы", "level": "debug"},
    },
}


class Activity:
    def __init__(self, id_: str, name: str, title: str, next_: str, args: dict[str:str]):
        self.id = id_
        self.name = name
        self.title = title
        self.next = next_
        self.args = args

    @classmethod
    def from_dict(cls, id_, dict_activity: dict[str:dict]):
        name = dict_activity.get("name", "")
        title = dict_activity.get("title", "")
        next_ = dict_activity.get("next", "")
        args = dict_activity.get("args", {})
        return cls(id_, name, title, next_, args)

    def __repr__(self):
        return f"<Activity ID:{self.id}>"


def create_activity_graph(robot: dict[str:dict]) -> list[Activity, ...]:
    activities = []
    for key, value in robot.items():
        activities.append(
            Activity.from_dict(key, value)
        )
    return activities


activities = create_activity_graph(robot)


def traverse_activities(activities: list[Activity, ...], start_id: str):
    map_activities = {}
    for active in activities:
        map_activities[active.id] = active

    current_active = map_activities[start_id]
    index = 0
    # stop = False
    while True:
        print(
            f"Шаг {index}: {current_active.name} - {current_active.title} - {current_active.args} (ID: {current_active.id})")
        next_id = current_active.next
        if current_active.name == "base.finish":
            break
        if not next_id:
            print("нет следующей активности")
            break

        current_active = map_activities[next_id]
        index += 1

print(len(activities))
traverse_activities(activities, "005")