import re

with open("public/index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_launch = """  <section class="art" id="launch">
    <h2>The launch</h2>
    <ol>
      <li><b>Reservoir is a new kind of biological infrastructure.</b> Not a treatment. Not a genetic test. It lets you preserve your own immune cells today and keep them stored for the future.</li>
      <li><b>Your biology changes as you age.</b> The cells you have today are the youngest cells you’ll ever have. We don't know what medicine will be able to do with those cells 20 or 30 years from now. But you can't go back and get the biology you had today.</li>
      <li><b>The insane part is the infrastructure.</b> The problem wasn't figuring out how to freeze cells. That already existed. The problem was connecting blood collection, shipping, cell isolation, cryopreservation, and long-term storage into one system that could actually work at scale. Reservoir built that infrastructure.</li>
      <li><b>You can do it in 15 minutes.</b> Walk into a partner clinic, get a simple blood draw, and Reservoir handles everything from there. Your sample goes through the network, your immune cells are isolated and cryopreserved, and they're stored long-term in liquid nitrogen vapor with redundant monitoring.</li>
      <li><b>The future medicine angle is the real story.</b> Cellino is building technology to make personalized cell medicine possible at scale. Reservoir makes sure the biological starting material is still there when that future arrives.</li>
      <li><b>The founders and technology have been building toward this for years.</b> Nabiha Saklayen started Cellino in 2017, coming from a background in physics and laser technology. Cellino developed technology using lasers and AI to work with individual cells and automate personalized cell manufacturing.</li>
      <li><b>The credibility is already there.</b> Cellino has raised over $120M from Khosla Ventures, 8VC, Felicis, Leaps by Bayer and others, alongside a $25M ARPA-H contract to build autonomous manufacturing for personalized cell therapies.</li>
      <li><b>The launch video tells the story through time.</b> Technology goes from primitive to impossible. Computers can create almost anything. AI can do things that seemed impossible decades ago. Then we hit the one thing we can't recreate: the exact biology you have today. That's why Reservoir exists.</li>
    </ol>
  </section>"""

pattern = r'<section class="art" id="launch">.*?</section>'
match = re.search(pattern, html, re.DOTALL)
if match:
    html = html[:match.start()] + new_launch + html[match.end():]
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS: The launch section updated successfully!")
else:
    print("ERROR: Could not find launch section")
