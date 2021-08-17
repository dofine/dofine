import requests
import os


def get_user_stats(screen_name):
    url = "https://stat.ink/api/v2/user-stats"
    r = requests.get(url, params={"screen_name": screen_name}).json()
    return r


def get_battle(screen_name):
    url = "https://stat.ink/api/v2/battle"
    r = requests.get(url, params={"screen_name": screen_name}).json()
    return r


def get_user_battle(screen_name, api_key, **kwargs):
    kwargs["screen_name"] = screen_name
    url = "https://stat.ink/api/v2/user-battle"
    r = requests.get(
        url,
        headers={
            "Authorization": "Bearer {api_key}".format(api_key=api_key),
            "Content-Type": "application/json",
        },
        params=kwargs,
    ).json()
    print(r)

    return r


def write_readme(fp, lines_to_write):
    with open(fp, "r") as f:
        lines = f.readlines()
    for ix in range(len(lines)):
        if lines[ix] == "<!-- SPLATOON-STAT:START -->":
            for _, line in enumerate(lines_to_write):
                lines.insert(ix, line)
    with open(fp, "w") as f:
        f.writelines(lines)
    return True


if __name__ == "__main__":
    file_path = os.getenv("INPUT_README_PATH")
    j = get_user_battle(
        os.getenv("SCREEN_NAME"), os.getenv("STAT_API_KEY"), order="desc",
    )

    lines = "\t".join(
        [
            str(x)
            for x in [
                j[0]["kill"],
                j[0]["death"],
                j[0]["kill_or_assist"],
                j[0]["special"],
            ]
        ]
    )
    lines = lines.split("\n")
    write_readme(file_path, lines)
