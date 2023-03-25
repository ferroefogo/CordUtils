import nextcord
from nextcord.ext import commands
from discord.ext.commands.errors import MissingPermissions
import config

class DevUtils(commands.Cog, name="devutils"):
    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @nextcord.slash_command(name="newbot", description="Creates environment for bot development")
    @commands.has_permissions(administrator=True)
    async def newbot(self, interaction, botname: str):
        guild = interaction.guild

        channel_perms = {
            guild.default_role: nextcord.PermissionOverwrite(read_messages=False),
            guild.me: nextcord.PermissionOverwrite(read_messages=True)
        }

        # Create category
        category = await guild.create_category(name=botname, overwrites=channel_perms)

        # Create resources chat
        await guild.create_text_channel(name="resources", category=category)

        # Create bot-test chat
        await guild.create_text_channel(name="bot-test", category=category)


        # Embed to show successful creation.
        dev_embed = nextcord.Embed(title=f"{botname} Development Environment Created!",
                                    color=0xff0000
                                    )
        dev_embed.set_footer(text="DevUtils", icon_url=self.__bot.user.avatar)
        dev_embed.add_field(name='Category', value=f"{botname}", inline=False)
        dev_embed.add_field(name='Text Channels', value=f"resources and bot-test", inline=False)

        await interaction.response.send_message(embed=dev_embed, ephemeral=True)



    @nextcord.slash_command(name="purge", description="Purge channel content")
    @commands.has_permissions(administrator=True)
    async def purge(self, interaction):
        await interaction.response.defer()
        await interaction.channel.purge(limit=None)



    # @nextcord.slash_command(name="player", description="Displays players BTD6 stats!")
    # async def player(self, interaction, userid: str):

    #     if getPlayerStats(userid) == "Invalid user ID":
            
    #             invalid_embed = nextcord.Embed(title=f":warning: Invalid user ID",
    #                             color=0xff0000
    #                             )
            
    #             await interaction.response.send_message(embed=invalid_embed)
    #     else:
    #         displayName, avatarURL, mostExpMonkey, rank, veteranRank, totalPopCount, cashEarned, highestRound, chimpsMedal = getPlayerStats(userid)
    #         mostExpMonkeyEMOTE = self.emojis[mostExpMonkey]


    #         stats_embed = nextcord.Embed(title=f"{displayName} Stats",
    #                                 color=0xff0000
    #                                 )
    #         stats_embed.set_footer(text="Banana Farmer", icon_url=self.__bot.user.avatar)
    #         stats_embed.set_thumbnail(avatarURL)
    #         stats_embed.add_field(name='Level',value=f"<:HeroLevelBadge:1078775199652122654> {rank}", inline=False)
    #         stats_embed.add_field(name='Veteran Level',value=f"<:VeteranIcon:1078766458533859328> {veteranRank}", inline=False)
    #         stats_embed.add_field(name='Most Experienced Monkey', value=f"{mostExpMonkeyEMOTE} {mostExpMonkey}", inline=False)
    #         stats_embed.add_field(name='Total Pop Count', value=f"<:redbloon:1078761738448678933> {totalPopCount:,}", inline=False)
    #         stats_embed.add_field(name='Total Cash Earned', value=f"<:MoneyIcon:1078767402294198435> ${cashEarned:,}", inline=False)
    #         stats_embed.add_field(name='Highest Round', value=f"<:DarkMonkey:1078768575835275294> {highestRound}", inline=False)
    #         stats_embed.add_field(name='CHIMPS Medals', value=f"<:chimpsBlack:1078761963779260438> {chimpsMedal}", inline=False)


    #         await interaction.response.send_message(embed=stats_embed)

def setup(bot):
    bot.add_cog(DevUtils(bot))
