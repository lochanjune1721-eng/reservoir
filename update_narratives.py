import re

with open("public/index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_narrative = """  <section class="art" id="narrative">
    <h2>What's the narrative on X?</h2>
    <p class="sub">Nine stories already run on X. Each one is a door for a Reservoir post.</p>

    <div class="n">
      <h3>1. Anti-AI doomer</h3>
      <p>AI Twitter is split between people saying we need to slow down and people saying we're going to regret slowing down.</p>
      <p>Dario and Sam are focused on the risks of increasingly powerful AI. Trump, Jensen and Zuckerberg are much more aligned with the build faster / open AI side.</p>
      <p>And then Dario says AI could potentially cure most major diseases in 5–10 years.</p>
      <p><b>The provocative question:</b></p>
      <p>If AI can cure diseases that kill millions of people, and we slow it down, aren't we potentially mass murdering the people it could have saved?</p>
      <p class="so"><b>So, for Reservoir:</b> Everyone asks if AI will kill us.<br><br><b>What if AI saves us?</b><br><br>And if medicine gets insanely good, you better still have your biology from today.</p>
    </div>

    <div class="n">
      <h3>2. What insane thing are billionaires doing?</h3>
      <p>There is always a viral conversation around what billionaires are doing to prepare for the future.</p>
      <p>Bunkers.<br>Anti-aging.<br>Cryonics.<br>Extreme health tracking.<br>Biotech.</p>
      <p>Putin has talked about radical advances in biotechnology and life extension. China is heavily investing in longevity too.</p>
      <p>People see these things and think billionaires are fucking insane.</p>
      <p class="so"><b>So, for Reservoir:</b> show the insane things first.<br><br>Then:<br><br><b>For years, preserving your own biology was something only billionaires could access. Now anyone can do it in 15 minutes.</b><br><br>That's the entire story.</p>
    </div>

    <div class="n">
      <h3>3. Founder story</h3>
      <p>Nabiha started in physics.<br>Harvard PhD.<br>Lasers and nanotechnology.<br>Her grandmother dies from severe diabetes.<br>She moves into biology.<br>Discovers cellular reprogramming.<br>Realizes personalized medicine could be built from someone's own cells.<br>Then realizes the technology isn't scalable.<br>So she takes her laser technology into biology.<br>Starts Cellino.<br>Builds AI + laser technology for individual cells.<br>Builds Nebula.<br>Gets the FDA Advanced Manufacturing Technology designation.<br>$25M ARPA-H contract.<br>$120M+ raised.</p>
      <p>Then realizes:</p>
      <p><b>If future medicine needs your cells, you need to still have them.</b></p>
      <p class="so"><b>So, for Reservoir:</b> So she builds Reservoir.</p>
    </div>

    <div class="n">
      <h3>4. Infrastructure like AWS or ASML</h3>
      <p>Everyone talks about the science.<br>Nobody talks about the infrastructure.</p>
      <p>Cryopreservation exists.<br>Blood draws exist.<br>Cell processing exists.<br>Long-term storage exists.</p>
      <p>But connecting all of it into one scalable system didn't.</p>
      <p>ASML didn't invent semiconductors.<br>AWS didn't invent the internet.</p>
      <p class="so"><b>So, for Reservoir:</b> the science existed.<br><br><b>The infrastructure didn't.</b><br><br>So we built it.</p>
    </div>

    <div class="n">
      <h3>5. Bryan Johnson / Project Blueprint</h3>
      <p>Bryan Johnson gets absolutely destroyed on X.<br>Everyone thinks he's insane.</p>
      <p>But what if he's right?</p>
      <p>What if medicine in 2045 is dramatically better than medicine today?</p>
      <p class="so"><b>So, for Reservoir:</b> give Bryan the love.<br><br>Don't argue about every Blueprint protocol.<br><br>Just:<br><b>What if the guy everyone is laughing at is actually early?</b><br><br>If future medicine gets radically better, preserving your biology today suddenly makes a lot more sense.</p>
    </div>

    <div class="n">
      <h3>6. Rage bait / memes</h3>
      <p>Every launch needs a little controversy.</p>
      <p>And Reservoir has the perfect controversial opinion:</p>
      <p><b>We're building a solution for a problem that might not even exist.</b></p>
      <p>You might not need your cells for 20 years.<br>Maybe medicine never figures out what to do with them.<br>Maybe it does.</p>
      <p>That's what makes it crazy.</p>
      <div class="media quote-card" style="margin:10px 0;">
        <b>Fake startup ideas:</b>
        <p>• "We raised $10M to solve a problem that doesn't exist yet."<br>
        • "We built a startup where the customer does nothing for 20 years."<br>
        • "What if your most important healthcare decision is for a disease that hasn't been cured yet?"</p>
      </div>
      <p class="so"><b>So, for Reservoir:</b> lean into how fucking insane the idea sounds.</p>
    </div>

    <div class="n">
      <h3>7. Aging can be stopped. The proof is piling up.</h3>
      <p>Research papers are doing numbers on X.<br>Someone finds a crazy paper.<br>Screenshots it.<br>Explains it in five sentences.<br>Millions of views.<br>And the longevity conversation keeps getting bigger.</p>
      <p class="so"><b>So, for Reservoir:</b> we can do the same thing with cell preservation.<br><br>Cryopreservation.<br>PBMCs.<br>Cell viability.<br>Freezing and thawing.<br>Long-term storage.<br>New preservation research.<br><br>Paper after paper.<br><br><b>The research is the content. Reservoir is the company making the idea real.</b></p>
    </div>

    <div class="n">
      <h3>8. Competition is cooked</h3>
      <p>The longevity industry is spending billions trying to make old cells young again.</p>
      <p>NewLimit.<br>Altos.<br>Retro.<br>Life Biosciences.<br>BioAge.</p>
      <p>The question everyone is asking:<br><b>How do we reverse aging?</b></p>
      <p>Reservoir asks:<br><b>Why not just keep the young cells?</b></p>
      <p class="so"><b>So, for Reservoir:</b> this is the provocative post.<br><br>The longevity industry is trying to make old cells young.<br>Reservoir just saved the young ones.<br><br><b>Rejuvenation vs preservation.<br>That's the debate.</b></p>
    </div>

    <div class="n">
      <h3>9. Sci-fi is becoming real</h3>
      <p><i>Passengers. Alien. 2001: A Space Odyssey.</i></p>
      <p>Science fiction has spent decades imagining humans preserving themselves for a future that doesn't exist yet.</p>
      <p>Cryosleep.<br>Suspended animation.<br>Waking up decades later.</p>
      <p>Obviously Reservoir isn't freezing humans.</p>
      <p>But the idea is similar:</p>
      <p><b>Take something biological from today. Preserve it. Let the future catch up.</b></p>
      <p class="so"><b>So, for Reservoir:</b><br><br>Science fiction spent 50 years freezing humans for the future.<br><br><b>We started with their cells.</b></p>
    </div>
  </section>"""

pattern = r'<section class="art" id="narrative">.*?</section>'
match = re.search(pattern, html, re.DOTALL)
if match:
    html = html[:match.start()] + new_narrative + html[match.end():]
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS: Updated narrative section with new text!")
else:
    print("ERROR: Could not find narrative section in public/index.html")
