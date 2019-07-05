# https://discordapp.com/oauth2/authorize?client_id=596095379716571290&scope=bot&permissions=8 // inv url
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Everything's all ready to go~")
    game = discord.Game("with my dick!")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event
async def on_message(message):
    channel = bot.get_channel(596097652140146699)
    if message.guild is None:
        await channel.send(message.content)
    await bot.process_commands(message)

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
    embed.add_field(name="$cat", value="Shows a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Shows a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Shows this message", inline=False)
    embed.add_field(name="$kick [user]", value="Kicks an asshole :)", inline=False)
    embed.add_field(name="$ban [user]", value="Bans a bigger asshole :)", inline=False)
    embed.add_field(name="$purge [number]", value="Removes a number of messages.", inline=False)
    embed.add_field(name="$perms [user]", value="Returns the member’s guild permissions value.", inline=False)
    embed.add_field(name="$nick [user]", value="Gives [user] a nickname in the server.", inline=False)
    embed.add_field(name="$mute [user]", value="Mutes [user].", inline=False)
    embed.add_field(name="$add_role [user] [role]", value="Adds a role to [user].", inline=False)
    embed.add_field(name="$remove_role [user] [role]", value="Removes a role from [user].", inline=False)


    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
    embed = discord.Embed(title="Kermit", description="A Very Nice bot!", color=0xeee657)

    embed.add_field(name="Invite Link", value="https://shorturl.at/jsuT1", inline=True)

    await ctx.send(embed=embed)

@bot.command()
async def kick(ctx, username: discord.Member):
        kicker = ctx.author.mention
        try:
            if ctx.author.guild_permissions.administrator or ctx.author.guild_permissions.kick_members or ctx.author.id == 302409090959671297:
                await username.kick()
                await ctx.send(f"Successfully kicked {username} by {kicker}")
            else:
                await ctx.send(f"You do not have permission to run this command. {kicker}")
        except:
            await ctx.send(f"Error kicking {username}!")

@bot.command()
async def purge(ctx, num: int):
    '''Bulk Deletes Messages (Requires Admin Permissions)'''
    mention = ctx.author.mention
    try:
        if ctx.author.guild_permissions.administrator or ctx.author.guild_permissions.manage_messages or ctx.author.id == 302409090959671297:
            await ctx.channel.purge(limit=num + 1)
            await ctx.send(f"Deleted {num} Messages Successfully! {mention}")
        else:
            await ctx.send(f"You do not have permission to run this command. {mention}")
    except:
        await ctx.send(f"Error Purging messages!")


@bot.command()
async def ban(ctx, username: discord.Member):
        banner = ctx.author.mention
        try:
            if ctx.author.guild_permissions.administrator or ctx.author.guild_permissions.ban_members or ctx.author.id == 302409090959671297:
                await username.ban()
                await ctx.send(f"Successfully banned {username} by {banner}")
            else:
                await ctx.send(f"You do not have permission to run this command. {banner}")
        except:
            await ctx.send(f"Error banning {username}!")

@bot.command()
async def perms(ctx, username: discord.Member):
    await ctx.send(f"{username.guild_permissions}")

@bot.command()
async def nick(ctx, username: discord.Member, *, nickname):
    caller = ctx.author.mention
    try:
        if ctx.author.guild_permissions.manage_nicknames or ctx.author.guild_permissions.administrator or ctx.author.id == 302409090959671297:
            await username.edit(nick= nickname)
        else:
            await ctx.send(f"You do not have permission to run this command. {caller}")

    except:
        await ctx.send(f"Error calling this command {caller}!")

@bot.command()
async def mute(ctx, username: discord.Member):
    muter = ctx.author.mention
    try:
        if ctx.author.guild_permissions.mute_members or ctx.author.guild_permissions.administrator or ctx.author.id == 302409090959671297:
            await username.edit(mute=True)
        else:
            await ctx.send(f"You do not have permission to run this command. {muter}")

    except:
        await ctx.send(f"Error muting {username}!")

@bot.command()
async def add_role(ctx, Member: discord.Member, Role: discord.Role):
    '''Adds Roles to a Member (Requires Admin Permissions)'''
    mention = ctx.author.mention
    try:
        if ctx.author.guild_permissions.administrator or ctx.author.guild_permissions.manage_roles or ctx.author.id == 302409090959671297:
            await Member.add_roles(Role, reason=None, atomic=True)
            await ctx.send(f"Added Role: {Role} to {Member}")
        else:
            await ctx.send(f"You do not have permission to run this command. {mention}")
    except:
        await ctx.send(f"Error adding role to {Member}!")

@bot.command()
async def remove_role(ctx, Member: discord.Member, Role: discord.Role):
    '''Removes Roles from a Member (Requires Admin Permissions)'''
    mention = ctx.author.mention
    try:
        if ctx.author.guild_permissions.administrator or ctx.author.guild_permissions.manage_roles or ctx.author.id == 302409090959671297:
            await Member.remove_roles(Role, reason=None, atomic=True)
            await ctx.send(f"Removed Role: {Role} from {Member}")
        else:
            await ctx.send(f"You do not have permission to run this command. {mention}")
    except:
        await ctx.send(f"Error removing role from {Member}!")


token = open("token.txt","r").read()
bot.run(token)

# shorturl.at/jsuT1