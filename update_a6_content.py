import re

tweets = [
    (
        "Silicon Valley Takes", "@sv_takes", "cynic",
        "imagine building a startup where your customer might not need the product for another 30 years\n\nand you have no fucking idea what the product will be used for yet"
    ),
    (
        "VC Brags", "@vcbrags", "vc pitch",
        "imagine raising $100M for a startup where the entire thesis is\n\n“future medicine might be really fucking good”"
    ),
    (
        "Tech Bro Quotes", "@techbroquotes", "the pitch",
        "VC: when does this become useful?\n\nfounder: honestly we don't know\n\nVC: how big is the market?\n\nfounder: everyone\n\nVC: when will they need it?\n\nfounder: hopefully not for 30 years"
    ),
    (
        "Startups Anonymous", "@startupsanon", "timeline",
        "imagine starting a company where the customer won't know whether they made the right decision for decades"
    ),
    (
        "Startup Logic", "@startuplogic", "asymmetry",
        "the startup:\n\nwe're solving a problem that doesn't exist yet\n\nalso the startup:\n\nif the problem exists by the time you know about it, it's already too late"
    ),
    (
        "Founder Mode", "@foundermode", "pitch deck",
        "imagine telling a VC\n\n“our biggest competitor is literally time”"
    ),
    (
        "Product Critique", "@productcritique", "the contrast",
        "Bryan Johnson: spends millions every year trying to optimize his future\n\nReservoir:\n\nbro you could've just done one thing and gone home"
    ),
    (
        "Internet Culture", "@netculture", "simplicity",
        "Bryan Johnson has turned his entire life into a longevity experiment\n\nimagine if there was a startup whose entire pitch was:\n\n“you don't have to do all that shit”"
    ),
    (
        "Philosophy Tech", "@philosophytech", "inverse utility",
        "imagine building a startup where the less you use the product, the better your life probably went"
    ),
    (
        "Business Model Hub", "@bizmodels", "the model",
        "“what if nobody ever needs your product?”\n\nthat's actually the business model"
    ),
    (
        "SaaS Humor", "@saashumor", "roadmap",
        "imagine your startup's biggest pitch being:\n\n“we don't know what future medicine will look like either”"
    ),
    (
        "Venture Capitalists", "@venturecap", "insane pitch",
        "the most insane startup pitch I've ever heard:\n\n“we're going to prepare you for a medical future that hasn't been invented yet”"
    ),
    (
        "Customer Reviews", "@customerreviews", "review",
        "imagine making a startup where the customer basically says:\n\n“I'll find out if this was worth it when I'm 60”"
    ),
    (
        "Bio Contrarian", "@biocontrarian", "longevity",
        "the entire longevity industry: spend millions trying to control your future\n\nReservoir: you really don't have to do all that"
    ),
    (
        "Option Value", "@optionvalue", "call option",
        "imagine spending $2M a year trying to optimize your biology\n\nwhen a startup could just let you keep your options open for the future"
    ),
    (
        "Startup Ideas", "@startupideas", "timing",
        "startup idea: solve a problem nobody has yet\n\ninvestors: that's insane\n\nstartup: that's literally why you need to do it now"
    )
]

posts_html = []
for i, (name, handle, line, text) in enumerate(tweets, 1):
    pid = f"p6-{i}"
    likes = f"{15 + (i * 3) % 25}.{i % 9}K"
    rts = f"{2 + i % 5}.{i % 8}K"
    replies = f"{300 + (i * 123) % 800}"
    views = f"{1 + (i * 2) % 4}.{i % 9}M"
    
    post = f"""  <!-- TWEET {i} -->
  <article class="post" id="{pid}">
    <div class="pl"><svg class="av" width="40" height="40" viewBox="0 0 40 40"><rect width="40" height="40" rx="20" fill="#f4212e"/><text x="12" y="26" fill="#fff" font-weight="700" font-size="14">RB</text></svg></div>
    <div class="pr">
      <div class="ph-row"><b>{name}</b><svg class="vb" viewBox="0 0 22 22" width="18" height="18"><path fill="#1d9bf0" d="M20.396 11c-.018-.646-.215-1.275-.57-1.816-.354-.54-.852-.972-1.438-1.246.223-.607.27-1.264.14-1.897-.131-.634-.437-1.218-.882-1.687-.47-.445-1.053-.75-1.687-.882-.633-.13-1.29-.083-1.897.14-.273-.587-.704-1.086-1.245-1.44S11.647 1.62 11 1.604c-.646.017-1.273.213-1.813.568s-.969.854-1.24 1.44c-.608-.223-1.267-.272-1.902-.14-.635.13-1.22.436-1.69.882-.445.47-.749 1.055-.878 1.688-.13.633-.08 1.29.144 1.896-.587.274-1.087.705-1.443 1.245-.356.54-.555 1.17-.574 1.817.02.647.218 1.276.574 1.817.356.54.856.972 1.443 1.245-.224.606-.274 1.263-.144 1.896.13.634.434 1.218.877 1.688.47.443 1.054.747 1.687.878.633.132 1.29.084 1.897-.136.274.586.705 1.084 1.246 1.439.54.354 1.17.551 1.816.569.647-.016 1.276-.213 1.817-.567s.972-.854 1.245-1.44c.604.239 1.266.296 1.903.164.636-.132 1.22-.447 1.68-.907.46-.46.776-1.044.908-1.681s.075-1.299-.165-1.903c.586-.274 1.084-.705 1.439-1.246.354-.54.551-1.17.569-1.816zM9.662 14.85l-3.429-3.428 1.293-1.302 2.072 2.072 4.4-4.794 1.347 1.246z"/></svg><span class="h">{handle}</span><span class="dot">·</span><span class="h">draft {i}</span><span class="line">{line}</span></div>
      <div class="txt">{text}</div>
      <div style="margin-top:10px; display:inline-flex; align-items:center; gap:6px; background:#f0f3f4; color:#536471; font-size:11.5px; font-weight:700; padding:4px 10px; border-radius:6px; border:1px solid var(--line2);">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14zm-5-7l-3 3.72L9 13l-3 4h12l-4-5z"/></svg>
        <span>Meme asset</span>
      </div>
      <div class="acts" style="margin-top:10px;">
        <span><svg viewBox="0 0 24 24"><path d="M14.046 2.242l-4.148-.01h-.002c-4.374 0-7.8 3.427-7.8 7.802 0 4.098 3.186 7.206 7.465 7.37v3.828c0 .108.044.286.12.403.142.225.384.347.632.347.138 0 .277-.038.402-.118.264-.168 6.473-4.14 8.088-5.506 1.902-1.61 3.04-3.97 3.04-6.324 0-4.375-3.426-7.799-7.799z"/></svg> {replies}</span>
        <span><svg viewBox="0 0 24 24"><path d="M23.77 15.67c-.292-.293-.767-.293-1.06 0l-2.22 2.22V7.65c0-2.068-1.683-3.75-3.75-3.75h-5.85c-.414 0-.75.336-.75.75s.336.75.75.75h5.85c1.24 0 2.25 1.01 2.25 2.25v10.24l-2.22-2.22c-.293-.293-.768-.293-1.06 0s-.294.768 0 1.06l3.5 3.5c.145.147.337.22.53.22s.383-.072.53-.22l3.5-3.5c.294-.292.294-.767 0-1.06zm-10.66 3.28H7.26c-1.24 0-2.25-1.01-2.25-2.25V6.46l2.22 2.22c.148.147.34.22.53.22s.384-.073.53-.22c.293-.293.293-.768 0-1.06l-3.5-3.5c-.293-.294-.768-.294-1.06 0l-3.5 3.5c-.294.292-.294.767 0 1.06s.767.293 1.06 0l2.22-2.22V16.7c0 2.068 1.683 3.75 3.75 3.75h5.85c.414 0 .75-.336.75-.75s-.336-.75-.75-.75z"/></svg> {rts}</span>
        <span><svg viewBox="0 0 24 24"><path d="M12 21.638h-.014C9.403 21.59 1.95 14.856 1.95 8.478c0-3.064 2.525-5.754 5.403-5.754 2.29 0 3.83 1.58 4.646 2.73.814-1.148 2.354-2.73 4.645-2.73 2.88 0 5.404 2.69 5.404 5.755 0 6.376-7.454 13.11-10.034 13.156H12z"/></svg> {likes}</span>
        <span><svg viewBox="0 0 24 24"><path d="M8.75 21V3h2v18h-2zM18 21V8.5h2V21h-2zM4 21l.005-6.5H6V21H4zm9.248 0v-9h2v9h-2z"/></svg> {views}</span>
      </div>
    </div>
  </article>"""
    posts_html.append(post)

all_posts = "\n\n".join(posts_html)

new_tab_a6 = f"""<section class="tab" id="tab-a6" hidden>
  <div class="ahead">
    <span class="k">Angle 6</span>
    <h2>The startup you might not need for 30 years</h2>
    <p class="one">The concept behind Reservoir is so fucking weird that <b>the concept itself is the content</b>.</p>
    <p class="who"><b>The Absurd Premise:</b> We're used to startups solving problems people have <b>right now</b>. This is the opposite. What if you built a company around a problem that might not exist yet? What if the technology that makes your product valuable hasn't even been invented? What if your customer pays you today and doesn't find out whether they made the right decision for another 20 or 30 years? That's the kind of absurdity we can lean into. The posts can make fun of the startup, the business model, the VC pitch and even the idea of Bryan Johnson spending millions on longevity when something much simpler could exist. Then the reveal is basically: <b>Maybe you don't need to spend millions preparing for the future. Maybe you just need to make one decision today. That's Reservoir.</b></p>

    <div class="blk">
      <h4>Why this angle</h4>
      <ol>
        <li><b>The concept is inherently controversial.</b> People will immediately argue whether this is genius, pointless, insane or the future.</li>
        <li><b>We don't have to explain the product.</b> The absurd business model is enough to make someone curious.</li>
        <li><b>It creates a perfect contrast with people like Bryan Johnson.</b> He's spending millions trying to optimize his future. The joke becomes: <i>what if you could prepare for the future without turning your entire life into a longevity experiment?</i></li>
        <li><b>The product reveal feels earned.</b> Once people understand the crazy premise, Reservoir becomes the answer to the question the post created.</li>
      </ol>
    </div>
  </div>

  <div class="feed-label" style="padding:10px 16px; font-size:13px; font-weight:700; color:var(--muted); border-bottom:1px solid var(--line); background:#fafcfc;">
    Tweets we can do (16 draft posts)
  </div>

{all_posts}
</section>"""

with open("public/index.html", "r", encoding="utf-8") as f:
    html = f.read()

start_marker = '<section class="tab" id="tab-a6" hidden>'
end_marker = '<section class="tab" id="tab-a7" hidden>'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found!")
    exit(1)

updated_html = html[:start_idx] + new_tab_a6 + "\n\n<!-- TAB A7: SCIENCE FICTION -->\n" + html[end_idx:]

with open("public/index.html", "w", encoding="utf-8") as f:
    f.write(updated_html)

print("Successfully replaced tab-a6 in public/index.html")
