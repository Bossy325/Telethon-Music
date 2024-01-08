import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "26744258"))
    API_HASH = os.environ.get("API_HASH", "7c7dbcb9e6654389d112b418e10583fa")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6559502514:AAFlgE57Mc0izZZb7kYj7gU-KyUJ7aXWovE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKMBu1IXDOJSEUBkuy0t4iiql5gEchsz-UXr_dEzSuZCSfU_mHyf_qeLJd_ezfc-NtrEKhT-l_MAkNDbcehkglpXJlFqs5f2p_50wXtaWO3mO3sdrV1ABuUFh-JRfKp4VpBQV9s8SN480OpkwYAHDB402VEynr9nwfrv8oDZWjI5U-89ECXq34OYfWDm7T7jNmkY6-oDf_b-dfgqfaTFL7F0nrDitbX7VYLwrA3FGYIYNo1wmXcsdJJJXlzff8fHinbe6KD7F6QKcmEFLrgg8IH8he9EYjNzdPR2aR_jh6RwIUs72L4ukwEWnxzY4_W-DGOx0AB54edPfzQstOl5DBqyHGQ=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Muguwara789_bot")
    SUPPORT = os.environ.get("SUPPORT", "-1002015179601") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "-1002023679721") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6266348511")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
