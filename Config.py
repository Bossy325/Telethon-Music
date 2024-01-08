import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "26744258"))
    API_HASH = os.environ.get("API_HASH", "7c7dbcb9e6654389d112b418e10583fa")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6559502514:AAFlgE57Mc0izZZb7kYj7gU-KyUJ7aXWovE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJMBuxwVcU2aMLN4wuzKoTK3LLOrF_Ppi9TxiUbV-G79Xg0MP72yHNPFMXbr5uGTkFM_E_FQylkCnfR63C9nbCUctZiBCjNoSUDSVfMlAfxi5AetrFLSSbOBbDa_hmva-rCNA07O8k5jBA8n27PXBH2t7mLe4gUX3E9fqk05tSv8RQ4V_LQggp_FXQov_N_DIM_xMUymtTLR7c1pz_LpOd0yyERlACYhUlHP5MB-gnrZyvZebBTRbXR1Z-96cDHUZMpm0zAQ0lv15xu0q5UP410-45L3zGnAOaukI7q5V-qQJzsWUfQErbXQUQt3KvwLN-MSz9cXPAZQdI4Y04UGTlv99a8=")
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
