import logging

import discord
from discord.ext import commands
from discord.ext.commands import guild_only

from core import datasource
from core.service.karma_service import KarmaService
from util.config import config
from util.constants import embed_color

log = logging.getLogger(__name__)


class KarmaLeaderboard(commands.Cog):

    def __init__(self, bot, karma_service=KarmaService(datasource.karma)):
        self.bot = bot
        self.karma_service = karma_service

    @guild_only()
    @commands.command(brief='get a global karma leaderboard, categorical leaderboard or a channel leaderboard',
                      usage='{}leaderboard\n{}leaderboard channel [...]'.format(config['prefix'], config['prefix']))
    async def leaderboard(self, ctx, *, params=str):
        embed = discord.Embed(colour=embed_color)
        guild = ctx.message.guild
        leaderboard = list(self.karma_service.aggregate_top_karma_members(str(guild.id)))
        if len(leaderboard) > 0:
            for document in leaderboard:
                member = guild.get_member(int(document['_id']['member_id']))
                karma = document['karma']
                embed.add_field(name=member.name + '#' + member.discriminator, value=karma, inline=False)
            await ctx.channel.send(embed=embed)
