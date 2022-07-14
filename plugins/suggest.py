import hikari
import lightbulb
import os
import json


plugin = lightbulb.Plugin('suggestion')

server_suggestions_channel_dict = {}
if os.path.isfile("server_suggestions_channel_dict.json"):
    with open("server_suggestions_channel_dict.json", "r") as f:
        server_suggestions_channel_dict = json.load(f)

@plugin.command()
@lightbulb.option("suggestion", "Type your suggestion here", type=hikari.OptionType.STRING, required=True)
@lightbulb.command("suggest", "Suggest something to the discord server")
@lightbulb.implements(lightbulb.SlashCommand)
async def verify_command(ctx: lightbulb.Context) -> None:
    this_guild_id = str(ctx.guild_id)
    this_user_id = str(ctx.author.id)
    if this_guild_id in server_suggestions_channel_dict:
        the_suggestion = ctx.options.suggestion
        the_suggestion_channel = server_suggestions_channel_dict[this_guild_id]
        embed = hikari.Embed(title="Suggestion", description=the_suggestion).add_field(name="Suggested by:", value=f"<@{this_user_id}>")
        the_message = await ctx.bot.rest.create_message(the_suggestion_channel, embed)
        #add a thumbs up and a thumbs down reaction
        await ctx.bot.rest.add_reaction(the_suggestion_channel, the_message, "👍")
        await ctx.bot.rest.add_reaction(the_suggestion_channel, the_message, "👎")
        await ctx.respond("Your suggestion has been sent to the server")
    else:
        await ctx.respond("You need to set a channel first with `.set_suggestions_channel`")
        
def load(bot):
    bot.add_plugin(plugin)