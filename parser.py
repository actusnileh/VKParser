import vk_api
import csv
from tqdm import tqdm
import logging
from datetime import datetime
from vk_api.exceptions import VkApiError

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_vk_api(token):
    vk_session = vk_api.VkApi(token=token)
    return vk_session.get_api()


def get_group_members(vk, group_id):
    members = []
    offset = 0
    count = 1000

    try:
        total_count = vk.groups.getMembers(group_id=group_id)["count"]
        logging.info(f"Общее количество подписчиков: {total_count}")

        while offset < total_count:
            response = vk.groups.getMembers(
                group_id=group_id, offset=offset, count=count, fields="bdate"
            )
            members.extend(response["items"])
            logging.info(f"Загружено {len(members)} из {total_count} подписчиков...")
            offset += count

    except VkApiError as e:
        logging.error(f"Ошибка при получении подписчиков: {e}")

    return members


def filter_by_age(members, min_age=14, max_age=21):
    filtered_members = []
    current_year = datetime.now().year
    logging.info(f"Фильтрация подписчиков по возрасту {min_age}-{max_age}...")

    for member in tqdm(members, desc="Фильтрация"):
        if "bdate" in member and len(member["bdate"].split(".")) == 3:
            day, month, year = map(int, member["bdate"].split("."))
            age = current_year - year
            if min_age <= age <= max_age:
                filtered_members.append(f"https://vk.com/id{member['id']}")

    return filtered_members


def save_to_csv(profile_links, filename):
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Profile Link"])
            for link in profile_links:
                writer.writerow([link])
        logging.info(f"Данные успешно сохранены в {filename}")
    except Exception as e:
        logging.error(f"Ошибка при сохранении в файл: {e}")


def main(token, group_id, min_age=14, max_age=21, output_file=None):
    vk = get_vk_api(token)

    members = get_group_members(vk, group_id)
    if not members:
        logging.error("Не удалось загрузить подписчиков.")
        return

    filtered_members = filter_by_age(members, min_age, max_age)

    if not output_file:
        output_file = f"{group_id}.csv"

    save_to_csv(filtered_members, output_file)
    logging.info(
        f"Собрано {len(filtered_members)} профилей в возрастном диапазоне {min_age}-{max_age}."
    )


if __name__ == "__main__":
    token = "<your_vk_token>"
    group_id = "<your_group_id>"
    main(token, group_id)
