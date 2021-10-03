from pypresence import Presence
import time


app_id = ""
rpc = Presence(app_id)
rpc.connect()

rpc.update(
    details="Title",
    state="Description",
    start=time.time(),
    large_image= "",
    large_text="",

    buttons=[
        {"label": "", "url": ""},
        {"label": "", "url": ""}
    ]
)

input()