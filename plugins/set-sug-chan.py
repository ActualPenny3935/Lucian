import hikari
import lightbulb
import os
import json

plugin = lightbulb.Plugin('set_suggestions_channel')

server_suggestions_channel_dict = {}
if os.path.isfile("server_suggestions_channel_dict.json"):
    with open("server_suggestions_channel_dict.json", "r") as f:
        server_suggestions_channel_dict = json.load(f)

@plugin.command()
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.ADMINISTRATOR))
@lightbulb.option("channel", "The channel that you will use for suggestions", type=hikari.OptionType.CHANNEL, required=True)
@lightbulb.command("set_suggestions_channel", "(ADMIN ONLY) Set the channel that you will use for suggestions")
@lightbulb.implements(lightbulb.SlashCommand)
async def verify_command(ctx: lightbulb.Context) -> None:
    global server_suggestions_channel_dict
    this_user_id = str(ctx.author.id)
    the_suggestion_channel = str(ctx.options.channel.id)
    this_guild_id = str(ctx.guild_id)

    server_suggestions_channel_dict[this_guild_id] = the_suggestion_channel
    with open("server_suggestions_channel_dict.json", "w") as f:
        json.dump(server_suggestions_channel_dict, f)
    await ctx.respond(f"The suggestion channel has been set as <#{the_suggestion_channel}>")
    
    
def load(bot):
    bot.add_plugin(plugin)