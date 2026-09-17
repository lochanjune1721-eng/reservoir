import base64
import shutil
import re

img_src = "/Users/lochan/.gemini/antigravity-ide/brain/a28ccc86-bd0d-49b1-884d-1db8dafd438d/.user_uploaded/media_1789663702849.png"
img_dst = "public/launch_video_1979.png"
shutil.copy(img_src, img_dst)

with open(img_src, "rb") as f:
    b64_data = base64.b64encode(f.read()).decode("utf-8")

data_uri = f"data:image/png;base64,{b64_data}"

with open("public/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Build hero media element matching the reference image layout
hero_media_html = f"""      <div class="media hero-media" style="position:relative; aspect-ratio:16/9; border:1px solid var(--line2); border-radius:16px; overflow:hidden; background:#000; margin:10px 0 6px;">
        <img src="{data_uri}" alt="Reservoir Launch Video 1979" style="width:100%; height:100%; object-fit:cover; display:block;">
        <div style="position:absolute; inset:0; background:rgba(0,0,0,0.15); pointer-events:none;"></div>
        <div style="position:absolute; left:50%; top:50%; transform:translate(-50%, -50%); width:60px; height:60px; border-radius:50%; background:rgba(29,155,240,0.95); display:flex; align-items:center; justify-content:center; box-shadow:0 4px 14px rgba(0,0,0,0.4); cursor:pointer;">
          <svg viewBox="0 0 24 24" width="28" height="28" fill="#fff" style="margin-left:3px;"><path d="M8 5v14l11-7z"/></svg>
        </div>
        <div style="position:absolute; left:12px; bottom:12px; background:rgba(0,0,0,0.75); color:#fff; font-size:12px; font-weight:700; padding:3px 8px; border-radius:4px; display:flex; align-items:center; gap:5px;">
          <span>0:03 / 2:43</span>
        </div>
      </div>
      <div class="clipbar" style="display:flex; justify-content:space-between; align-items:center; font-size:12.5px; color:var(--muted); margin:4px 0 10px; padding:0 4px;">
        <span>Launch film • 2:43</span>
        <button class="dl" style="font:inherit; font-size:12.5px; font-weight:700; color:var(--blue); background:var(--blue-soft); border:0; border-radius:999px; padding:4px 12px; cursor:pointer;">Download clip</button>
      </div>"""

# Update the action row in hero post to include bookmark and share just like in reference image
acts_html = """      <div class="acts">
        <span><svg viewBox="0 0 24 24"><path d="M14.046 2.242l-4.148-.01h-.002c-4.374 0-7.8 3.427-7.8 7.802 0 4.098 3.186 7.206 7.465 7.37v3.828c0 .108.044.286.12.403.142.225.384.347.632.347.138 0 .277-.038.402-.118.264-.168 6.473-4.14 8.088-5.506 1.902-1.61 3.04-3.97 3.04-6.324 0-4.375-3.426-7.799-7.797-7.799z"/></svg> 2.4K</span>
        <span><svg viewBox="0 0 24 24"><path d="M23.77 15.67c-.292-.293-.767-.293-1.06 0l-2.22 2.22V7.65c0-2.068-1.683-3.75-3.75-3.75h-5.85c-.414 0-.75.336-.75.75s.336.75.75.75h5.85c1.24 0 2.25 1.01 2.25 2.25v10.24l-2.22-2.22c-.293-.293-.768-.293-1.06 0s-.294.768 0 1.06l3.5 3.5c.145.147.337.22.53.22s.383-.072.53-.22l3.5-3.5c.294-.292.294-.767 0-1.06zm-10.66 3.28H7.26c-1.24 0-2.25-1.01-2.25-2.25V6.46l2.22 2.22c.148.147.34.22.53.22s.384-.073.53-.22c.293-.293.293-.768 0-1.06l-3.5-3.5c-.293-.294-.768-.294-1.06 0l-3.5 3.5c-.294.292-.294.767 0 1.06s.767.293 1.06 0l2.22-2.22V16.7c0 2.068 1.683 3.75 3.75 3.75h5.85c.414 0 .75-.336.75-.75s-.336-.75-.75-.75z"/></svg> 5.8K</span>
        <span><svg viewBox="0 0 24 24"><path d="M12 21.638h-.014C9.403 21.59 1.95 14.856 1.95 8.478c0-3.064 2.525-5.754 5.403-5.754 2.29 0 3.83 1.58 4.646 2.73.814-1.148 2.354-2.73 4.645-2.73 2.88 0 5.404 2.69 5.404 5.755 0 6.376-7.454 13.11-10.034 13.156H12z"/></svg> 28.1K</span>
        <span><svg viewBox="0 0 24 24"><path d="M8.75 21V3h2v18h-2zM18 21V8.5h2V21h-2zM4 21l.005-6.5H6V21H4zm9.248 0v-9h2v9h-2z"/></svg> 1.2M</span>
        <span><svg viewBox="0 0 24 24"><path d="M4 4.5C4 3.12 5.119 2 6.5 2h11C18.88 2 20 3.12 20 4.5v16.71c0 .4-.45.64-.78.42L12 16.85l-7.22 4.78c-.33.22-.78-.02-.78-.42V4.5z"/></svg></span>
        <span><svg viewBox="0 0 24 24"><path d="M12 2.59l5.7 5.7-1.41 1.42L13 6.41V16h-2V6.41L7.71 9.71 6.3 8.29 12 2.59zM21 15l-.02 3.51c0 1.38-1.12 2.49-2.5 2.49H5.5C4.11 21.01 3 19.9 3 18.51V15h2v3.5c0 .28.22.5.5.5h12.98c.28 0 .5-.22.5-.5L19 15h2z"/></svg></span>
      </div>"""

# Replace in hero post
hero_pattern = r'(<article class="post hero-post" id="hero">.*?<div class="txt">.*?</div>\s*)(<div class="acts">.*?</div>)'
m = re.search(hero_pattern, html, re.DOTALL)
if m:
    new_hero = m.group(1) + hero_media_html + "\n" + acts_html
    html = html[:m.start()] + new_hero + html[m.end():]
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS: Hero post updated with 1979 media!")
else:
    print("ERROR: Could not match hero pattern")
