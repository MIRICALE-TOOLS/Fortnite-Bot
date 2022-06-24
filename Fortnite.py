import os
os.system("python3 -m pip install py-cord==2.0.0b4")
os.system("pip install sanic==21.6.2")

import discord
import requests
import aiohttp
from discord.ext import commands
import json
from sanic import Sanic
import sanic

app = Sanic("Fortnite")


from sanic.response import text, file, html
@app.route('/')
def index(request):
    return sanic.response.json({"FortniteX": "online"})

bot = commands.Bot(command_prefix='!')
footertext = "made with ❤ by NRG Cristi" #embed footer text remove credits = skid
color = 0x5865F2     #embed color (blurple)




@bot.event
async def on_connect():
  coro = app.create_server(
		host='0.0.0.0',
		port=8000,
		return_asyncio_server=True,
    access_log=False,
	)
  server = await coro

@bot.event
async def on_ready():
  print("Fortnite Is Online")







  message = await bot.wait_for('message', check=check)
  async with aiohttp.ClientSession() as session:
    async with session.request(
      method="POST",
      url="https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token",
      data=f"grant_type=authorization_code&code={message.content}",
      headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE=",
      }
    ) as r:
      d = await r.json()


      acc_id = d.get('account_id')
      token_ref = d.get('access_token')
      dn = d.get('displayName')

      rq = requests.get(url=f"https://avatar-service-prod.identity.live.on.epicgames.com/v1/avatar/fortnite/ids?accountIds={acc_id}", headers={"Content-Type": "application/json", "Authorization": f"bearer {token_ref}"})
      pp = rq.json()
      skinid = (pp[0]['avatarId'].replace('ATHENACHARACTER:', ''))
      await ctx.author.send(embed=embed)
      with open('users.json', 'r') as f:
          logs = json.load(f)
      logs[str(ctx.author.id)] = f'{acc_id}'
      with open('users.json', 'w') as f: 
          json.dump(logs, f, indent=3)

async def logout(ctx):
  try:
    with open('users.json', 'r') as f: 
      users = json.load(f) 
    id=users[f"{ctx.author.id}"]
    print(id + " Logged Out!")
    del users[f"{ctx.author.id}"]
    with open('users.json', 'w') as f: 
        json.dump(users, f, indent=3)
    embed=discord.Embed(title="Succesfully unlinked your Epic Games From Fortnite", color=color)
    embed.set_footer(text=footertext)
    await ctx.respond(embed=embed)
  except:
    await embeds.not_logged_in(ctx=ctx)
    return


async def crowns(ctx, amount):
  try:
    with open('users.json', 'r') as f: 
      users = json.load(f) 
    id = users[f'{str(ctx.author.id)}']
    print(id + " Updated Their Crowns")
    requests.get(f"/change/crown/{id}/{str(amount)}")
    embed=discord.Embed(title=f"Changed Crown Wins To {amount}", color=color)
    embed.set_footer(text="⚠️ This will update when u change a cosmetic in your locker or restart your game")
    await ctx.respond(embed=embed)
  except:
    await embeds.not_logged_in(ctx=ctx)
    return


async def level(ctx, amount):
  try:
    with open('users.json', 'r') as f: 
      users = json.load(f) 
    id = users[f'{str(ctx.author.id)}']
    print(id + " Updated Their Level")
    requests.get(f"/change/level/{id}/{str(amount)}")
    embed=discord.Embed(title=f"Changed Level To {amount}", color=color)
    embed.set_footer(text="⚠️ This will update when u change a cosmetic in your locker or restart your game")
    await ctx.respond(embed=embed)
  except:
    await embeds.not_logged_in(ctx=ctx)
    return




async def battlestars(ctx, amount):
  try:
    with open('users.json', 'r') as f: 
      users = json.load(f) 
    id = users[f'{str(ctx.author.id)}']
    print(id + " Updated Their Battle Stars")
    requests.get(f"/change/battlestars/{id}/{str(amount)}")
    embed=discord.Embed(title=f"Changed Battle Stars To {amount}", color=color)
    embed.set_footer(text="⚠️ This will update when u change a cosmetic in your locker or restart your game")
    await ctx.respond(embed=embed)
  except:
    await embeds.not_logged_in(ctx=ctx)
    return


async def style_points(ctx, amount):
  try:
    with open('users.json', 'r') as f: 
      users = json.load(f) 
    id = users[f'{str(ctx.author.id)}']
    print(id + " style points")
    requests.get(f"/change/style_points/{id}/{str(amount)}")
    embed=discord.Embed(title=f"Changed Omni Chips To {amount}", color=color)
    embed.set_footer(text="⚠️ This will update when u change a cosmetic in your locker or restart your game")
    await ctx.respond(embed=embed)
  except:
    await embeds.not_logged_in(ctx=ctx)
    return


async def vbucks(ctx, amount):
  try:
    with open('users.json', 'r') as f: 
      users = json.load(f) 
    id = users[f'{str(ctx.author.id)}']
    print(id + " vbucs")
    requests.get(f"/change/vbucs/{id}/{str(amount)}")
    embed=discord.Embed(title=f"Changed vbucs To {amount}", color=color)
    embed.set_footer(text="⚠️ This will update when u restart your game")
    await ctx.respond(embed=embed)
  except:
    await embeds.not_logged_in(ctx=ctx)
    return


