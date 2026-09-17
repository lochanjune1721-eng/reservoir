import re

with open("public/index.html", "r", encoding="utf-8") as f:
    html = f.read()

hero_media_clean = """      <div class="media hero-media" style="position:relative; aspect-ratio:16/9; border:1px solid var(--line2); border-radius:16px; overflow:hidden; background:#000; margin:10px 0 6px;">
        <img src="/launch_video_1979.png" alt="1979 Launch Video Still" style="width:100%; height:100%; object-fit:cover; display:block;">
        <div style="position:absolute; inset:0; background:rgba(0,0,0,0.1); pointer-events:none;"></div>
        <div style="position:absolute; left:50%; top:50%; transform:translate(-50%, -50%); width:60px; height:60px; border-radius:50%; background:rgba(29,155,240,0.95); display:flex; align-items:center; justify-content:center; box-shadow:0 4px 22px rgba(29,155,240,0.6); cursor:pointer; z-index:3;">
          <svg viewBox="0 0 24 24" width="28" height="28" fill="#ffffff" style="margin-left:3px;"><path d="M8 5v14l11-7z"></path></svg>
        </div>
        <div style="position:absolute; left:14px; bottom:14px; background:rgba(0,0,0,0.75); color:#ffffff; font-size:12px; font-weight:700; padding:4px 10px; border-radius:6px; display:flex; align-items:center; gap:6px; z-index:2; backdrop-filter:blur(4px); border:1px solid rgba(255,255,255,0.12);">
          <span style="width:6px; height:6px; border-radius:50%; background:#ef4444; display:inline-block;"></span>
          <span>0:03 / 2:43</span>
        </div>
      </div>"""

pattern = r'<div class="media hero-media".*?</div>(?=\s*<div class="clipbar")'
match = re.search(pattern, html, re.DOTALL)
if match:
    html = html[:match.start()] + hero_media_clean + html[match.end():]
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS: public/index.html updated with clean static image URL!")
else:
    print("ERROR: Could not match hero-media pattern!")
