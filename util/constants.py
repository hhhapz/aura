from discord import Color

zero_width_space = '\u200b'
thumps_up = '👍'  # used to indicate positive karma gain
thumps_down = '👎'  # used to indicate that karma gain can be reverted by the user
clock = '🕒'  # used to indicate cooldown periods
skull = '☠️'  # used to indicate that user is blacklisted
revoke_message = 'If you {}, didn\'t intend to give karma to this person,' + \
                 ' react to the' + thumps_down + 'of your original thanks message'
embed_max_columns = 3  # 3 because discord embeds can have three fields in a line
embed_color = Color.dark_gold()