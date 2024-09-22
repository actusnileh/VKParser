import vk_api
import csv
from tqdm import tqdm

token = ""
group_id = ""  # ID группы, с которой работаем

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()


def get_group_members(group_id):
    members = []
    offset = 0
    count = 1000
    total_count = vk.groups.getMembers(group_id=group_id)["count"]

    print(f"Общее количество подписчиков: {total_count}")

    while True:
        response = vk.groups.getMembers(
            group_id=group_id, offset=offset, count=count, fields="bdate"
        )
        members.extend(response["items"])

        print(f"Загружено {len(members)} из {total_count} подписчиков...")

        offset += count
        if offset >= total_count:
            break

    return members


def filter_by_age(members, min_age=14, max_age=21):
    filtered_members = []
    print(f"Фильтрация подписчиков по возрасту {min_age}-{max_age}...")

    for member in tqdm(members, desc="Фильтрация"):
        if "bdate" in member and len(member["bdate"].split(".")) == 3:
            day, month, year = map(int, member["bdate"].split("."))
            age = 2024 - year
            if min_age <= age <= max_age:
                filtered_members.append(f"https://vk.com/id{member['id']}")

    return filtered_members


def save_to_csv(profile_links):
    with open(f"{group_id}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Profile Link"])
        for link in profile_links:
            writer.writerow([link])


members = get_group_members(group_id)
filtered_members = filter_by_age(members)
save_to_csv(filtered_members)

print(f"Собрано {len(filtered_members)} профилей в возрастном диапазоне 14-22.")
