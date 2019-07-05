# https://discordapp.com/oauth2/authorize?client_id=596095379716571290&scope=bot&permissions=8 // inv url
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Everything's all ready to go~")

@bot.command()
async def test(ctx, *, arg):
    '''
    Tests the bot avaliblity.
    '''
    await ctx.send(f"```Test Command\n------------\nMessage: {arg}\nAuthor: {ctx.author}\nServer: {ctx.guild}```")

@bot.command()
async def ping(ctx):
    '''
    Tests the latency of the bot to the server it runs on [Chase#0157]
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(f"**PONG!!** :ping_pong:\nLatency = {latency}")

@bot.command()
async def greet(ctx, user):
    '''
    Greet somebody into joining the server!
    '''
    await ctx.send(f":smiley: :wave: Hello, there! {user}")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Kermit", description="Nicest bot there is ever.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Developer", value="Chase#0157")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="https://shorturl.at/jsuT1")

    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Kermit", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="$test [argument]", value="Tests the bot's avaliblity", inline=False)
    embed.add_field(name="$ping", value="Tests the bot's ping to it's server", inline=False)
    embed.add_field(name="$greet [user]", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
    embed = discord.Embed(title="Kermit", description="A Very Nice bot!", color=0xeee657)

    embed.add_field(name="Invite Link", value="https://shorturl.at/jsuT1", inline=True)

    await ctx.send(embed=embed)


token = open("token.txt","r").read()
bot.run(token)

# shorturl.at/jsuT1