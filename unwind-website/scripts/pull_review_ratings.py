import os, json, time, base64, urllib.request, urllib.parse, urllib.error
env={}
for line in open(os.path.expanduser("~/ownerrez-mcp/.env")):
    line=line.strip()
    if "=" in line and not line.startswith("#"):
        k,v=line.split("=",1); env[k.strip()]=v.strip()
USER=env["OWNERREZ_USERNAME"]; PAT=env["OWNERREZ_TOKEN"]; OAUTH=env["OWNERREZ_ACCESS_TOKEN"]
UA="OwnerRez MCP"
BASIC="Basic "+base64.b64encode(f"{USER}:{PAT}".encode()).decode()

def api(path, params, auth):
    qs=urllib.parse.urlencode({k:v for k,v in params.items() if v not in (None,"")})
    url=f"https://api.ownerrez.com/v2/{path}"+("?"+qs if qs else "")
    req=urllib.request.Request(url, headers={"Authorization":auth,"User-Agent":UA,"Accept":"application/json"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode())

# 1) properties
props=[]; off=0
while True:
    d=api("properties", {"limit":100,"offset":off,"active":"true"}, BASIC)
    items=d.get("items",[])
    props+=items
    if not d.get("next_page_url"): break
    off+=len(items)
    if len(items)==0: break
print("properties fetched:", len(props))

# 2) reviews per property (visible only)
out={}
for p in props:
    pid=p["id"]; off=0; stars=[]; total=0
    while True:
        d=api("reviews", {"property_id":pid,"limit":100,"offset":off}, "Bearer "+OAUTH)
        items=d.get("items",[])
        if not items: break
        for rv in items:
            if rv.get("visible") is False: continue
            total+=1
            s=rv.get("stars")
            if isinstance(s,(int,float)): stars.append(float(s))
        if not d.get("next_page_url"): break
        off+=len(items)
    avg=round(sum(stars)/len(stars),2) if stars else None
    # slug: last path segment of public_url
    pu=p.get("public_url") or ""
    slug=pu.rstrip("/").split("/")[-1] if pu else None
    out[pid]={"name":p.get("name"),"slug":slug,"count":total,"avg":avg}
    time.sleep(0.05)

# summary
with_rev=[v for v in out.values() if v["count"]>0]
tot=sum(v["count"] for v in out.values())
print("total visible reviews across props:", tot)
print("properties with >=1 review:", len(with_rev), "of", len(out))
# validate Beach Club II (460814)
bc=out.get(460814); print("Beach Club II 460814 ->", bc)
# show a few
for pid,v in list(out.items())[:6]:
    print(f"  {v['count']:>3}  avg {v['avg']}  {v['name']}  [{v['slug']}]")
json.dump(out, open("review_map.json","w"), indent=2)
print("wrote review_map.json")
