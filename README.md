# osu_sbot
An noob nonebot v1 based osu bot write in Python.

# How to use

Clone or Download as zip, then put the whole folder to `/path/to/plugins/`.
Then, you can use these API to run your own bot.

# API(Working on docs)

## The most important api

`await Auth_data.get_auth_code(client_id, client_secret)`

This one must be called at each call of the bot. It returns an temp auth key from ppy.

If you don't have an oauth app, you can go to [Account settings](https://osu.ppy.sh/home/account/edit#oauth) to request your own app.

!!!KEEP YOUR APP SECRET IN SECURE AND DON'T LET ANY OTHER ONE KNOW IT!!!

`client_id`: Your oauth app's id

`client_secret`: Your oauth app's secret


## Binding

`await osu_sbot.binding(authkey, qqid, uid)`

Bind the osu user with his/her qq account.

authkey: will be returned by `osu_sbot.Auth_data.get_auth_code`.

qqid: The user's qq account id.

uid: The user's osu uid.

## Get score

`get_recent(authkey, uid, limit=9, mode)`
`get_bp(authkey, uid, limit, mode)`

...

# LICENSE

under GPL V3.
