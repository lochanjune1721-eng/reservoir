import re

with open("public/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Build the exact new content for tab-intro
new_tab_intro = """<section class="tab" id="tab-intro">
  <article class="post hero-post" id="hero">
    <div class="pl">
      <svg class="av" width="42" height="42" viewBox="0 0 42 42">
        <rect width="42" height="42" rx="21" fill="#0f1419"/>
        <path d="M12 21c2.2-3 5.3-3 7.5 0s5.3 3 7.5 0" stroke="#1d9bf0" stroke-width="2.5" stroke-linecap="round"/>
        <circle cx="21" cy="14" r="2.2" fill="#fff"/>
        <circle cx="21" cy="28" r="2.2" fill="#1d9bf0"/>
      </svg>
    </div>
    <div class="pr">
      <div class="ph-row">
        <b>Reservoir</b>
        <svg class="vb" viewBox="0 0 22 22" width="18" height="18"><path fill="#1d9bf0" d="M20.396 11c-.018-.646-.215-1.275-.57-1.816-.354-.54-.852-.972-1.438-1.246.223-.607.27-1.264.14-1.897-.131-.634-.437-1.218-.882-1.687-.47-.445-1.053-.75-1.687-.882-.633-.13-1.29-.083-1.897.14-.273-.587-.704-1.086-1.245-1.44S11.647 1.62 11 1.604c-.646.017-1.273.213-1.813.568s-.969.854-1.24 1.44c-.608-.223-1.267-.272-1.902-.14-.635.13-1.22.436-1.69.882-.445.47-.749 1.055-.878 1.688-.13.633-.08 1.29.144 1.896-.587.274-1.087.705-1.443 1.245-.356.54-.555 1.17-.574 1.817.02.647.218 1.276.574 1.817.356.54.856.972 1.443 1.245-.224.606-.274 1.263-.144 1.896.13.634.434 1.218.877 1.688.47.443 1.054.747 1.687.878.633.132 1.29.084 1.897-.136.274.586.705 1.084 1.246 1.439.54.354 1.17.551 1.816.569.647-.016 1.276-.213 1.817-.567s.972-.854 1.245-1.44c.604.239 1.266.296 1.903.164.636-.132 1.22-.447 1.68-.907.46-.46.776-1.044.908-1.681s.075-1.299-.165-1.903c.586-.274 1.084-.705 1.439-1.246.354-.54.551-1.17.569-1.816zM9.662 14.85l-3.429-3.428 1.293-1.302 2.072 2.072 4.4-4.794 1.347 1.246z"/></svg>
        <span class="h">@reservoir_bio</span><span class="dot">·</span><span class="h">launch day</span>
        <span class="line">hero</span>
      </div>
      <div class="txt">We’re excited to introduce Reservoir, one of the biggest breakthroughs ever in personalised medicine.

For years preserving your own cells was something only the wealthy had access to, now anyone can do that in 15 minutes.

We’ve raised over $120M from Khosla Ventures, 8VC, Felicis, and Leaps by Bayer, alongside a $25M ARPA-H contract to make that happen.

Thread 🧵</div>
      <div class="acts">
        <span><svg viewBox="0 0 24 24"><path d="M14.046 2.242l-4.148-.01h-.002c-4.374 0-7.8 3.427-7.8 7.802 0 4.098 3.186 7.206 7.465 7.37v3.828c0 .108.044.286.12.403.142.225.384.347.632.347.138 0 .277-.038.402-.118.264-.168 6.473-4.14 8.088-5.506 1.902-1.61 3.04-3.97 3.04-6.324 0-4.375-3.426-7.799-7.797-7.799z"/></svg> 2.4K</span>
        <span><svg viewBox="0 0 24 24"><path d="M23.77 15.67c-.292-.293-.767-.293-1.06 0l-2.22 2.22V7.65c0-2.068-1.683-3.75-3.75-3.75h-5.85c-.414 0-.75.336-.75.75s.336.75.75.75h5.85c1.24 0 2.25 1.01 2.25 2.25v10.24l-2.22-2.22c-.293-.293-.768-.293-1.06 0s-.294.768 0 1.06l3.5 3.5c.145.147.337.22.53.22s.383-.072.53-.22l3.5-3.5c.294-.292.294-.767 0-1.06zm-10.66 3.28H7.26c-1.24 0-2.25-1.01-2.25-2.25V6.46l2.22 2.22c.148.147.34.22.53.22s.384-.073.53-.22c.293-.293.293-.768 0-1.06l-3.5-3.5c-.293-.294-.768-.294-1.06 0l-3.5 3.5c-.294.292-.294.767 0 1.06s.767.293 1.06 0l2.22-2.22V16.7c0 2.068 1.683 3.75 3.75 3.75h5.85c.414 0 .75-.336.75-.75s-.336-.75-.75-.75z"/></svg> 5.8K</span>
        <span><svg viewBox="0 0 24 24"><path d="M12 21.638h-.014C9.403 21.59 1.95 14.856 1.95 8.478c0-3.064 2.525-5.754 5.403-5.754 2.29 0 3.83 1.58 4.646 2.73.814-1.148 2.354-2.73 4.645-2.73 2.88 0 5.404 2.69 5.404 5.755 0 6.376-7.454 13.11-10.034 13.156H12z"/></svg> 28.1K</span>
        <span><svg viewBox="0 0 24 24"><path d="M8.75 21V3h2v18h-2zM18 21V8.5h2V21h-2zM4 21l.005-6.5H6V21H4zm9.248 0v-9h2v9h-2z"/></svg> 1.2M</span>
      </div>
    </div>
  </article>

  <section class="art" id="launch">
    <h2>The launch</h2>
    <ol>
      <li><b>Reservoir is making it possible to preserve your own cells for the future.</b> A 15-minute blood draw, your immune cells are isolated, cryopreserved, and stored long-term. The idea is simple: your biology changes as you age, while medicine keeps getting better.</li>
      <li><b>The biggest question is what future medicine will actually be able to do.</b> AI is moving into biology, scientists are working on cellular reprogramming, and personalized medicine is becoming increasingly real. But if medicine in 20 or 30 years can do something with the cells you have today that it can&#x27;t do with the cells you have then, you can&#x27;t go back and get them.</li>
      <li><b>That&#x27;s why we built Reservoir.</b> The science of cryopreservation already exists. The hard part was building the infrastructure around it: from a blood draw, to processing, to preserving your cells, to keeping them stored for decades.</li>
      <li><b>Reservoir comes out of Cellino, which has spent years building the technology for personalized cell medicine.</b> Cellino uses lasers and AI to work with individual cells and is building autonomous manufacturing for personalized cell therapies.</li>
      <li><b>The bigger bet is on the future of medicine.</b> We don&#x27;t know what scientists will be able to do with your cells 20 years from now. Reservoir doesn&#x27;t try to predict that future. It makes sure your cells are still there when it arrives.</li>
      <li><b>So the product is almost absurdly simple.</b> You give blood for 15 minutes. We preserve your cells. And then you wait.</li>
      <li><b>Because you can&#x27;t go back in time.</b></li>
    </ol>
  </section>

  <section class="art" id="narrative">
    <h2>What's the narrative on X?</h2>
    <p class="sub">Nine stories already run on X. Each one is a door for a Reservoir post.</p>

    <div class="n">
      <h3>1. Anti-AI doomer</h3>
      <p>AI Twitter is having a massive fight over whether we should be accelerating AI or slowing it down.</p>
      <p>Dario Amodei and other frontier AI leaders are warning about the risks of increasingly powerful AI. On the other side, Trump, Jensen Huang and Mark Zuckerberg have been pushing back against slowing AI development.</p>
      <p>But there&#x27;s another part of the argument that gets much less attention.</p>
      <p>Dario himself has said AI could potentially help cure most major diseases within the next 5–10 years.</p>
      <p>So the provocative question is:</p>
      <p><b>If AI can cure diseases that kill millions of people, and we slow it down, aren&#x27;t we potentially killing people who could have been saved?</b></p>
      <p class="so"><b>So, for Reservoir:</b> The angle for us:<br><br><b>Everyone is asking if AI will kill us. What if AI saves us?</b><br><br>If AI really does accelerate medicine, what happens to the biology you have today?<br>That&#x27;s where Reservoir comes in.</p>
    </div>

    <div class="n">
      <h3>2. What insane thing billionaires are doing</h3>
      <p>There&#x27;s already a huge conversation around billionaires preparing for the future.</p>
      <p>Bunkers.<br>Longevity.<br>Cryonics.<br>Experimental medicine.<br>Bryan Johnson spending millions trying to slow aging.</p>
      <p>People see this stuff and think it&#x27;s completely insane.</p>
      <p>But the interesting question is:</p>
      <p><b>What if they&#x27;re preparing for a future that actually happens?</b></p>
      <p>What if medicine 20 or 30 years from now is so much better than medicine today that all of this suddenly makes sense?</p>
      <p class="so"><b>So, for Reservoir:</b> The story isn&#x27;t &quot;billionaires are buying this.&quot;<br><br>It&#x27;s:<br><b>What if the billionaires aren&#x27;t crazy for preparing for the future?</b><br><br>You don&#x27;t need a bunker.<br>You don&#x27;t need millions of dollars.<br>You can preserve your own cells in 15 minutes.</p>
    </div>

    <div class="n">
      <h3>3. Founder story</h3>
      <p>Nabiha Saklayen has one of those stories that feels almost too perfect for this product.</p>
      <p>Physics at Harvard.<br>Lasers.<br>Nanotechnology.<br>Her grandmother dies from severe diabetes.<br>She starts asking a completely different question:</p>
      <p><b>Why can&#x27;t medicine repair the body better?</b></p>
      <p>She moves into biology.<br>Discovers the work showing adult cells can be reprogrammed.<br>Realizes personalized cell medicine could completely change healthcare.<br>Then runs into the biggest problem:</p>
      <p><b>How do you actually manufacture personalized cells at scale?</b></p>
      <p>So she takes the laser technology from her physics work and applies it to biology.<br>Starts Cellino in 2017.<br>Builds laser-based cell technology.<br>Adds AI.<br>Builds Nebula.<br>Gets an FDA Advanced Manufacturing Technology designation.<br>Wins a $25M ARPA-H contract.<br>Works with Mass General Brigham on a Parkinson&#x27;s program.<br>Raises $120M+.</p>
      <p>And after years of building technology around human cells, she realizes something else:</p>
      <p><b>What if future medicine needs the cells you have today?</b></p>
      <p>So she builds Reservoir.</p>
      <p class="so"><b>So, for Reservoir:</b> The founder story is the entire company story.<br><br>She spent years figuring out how to work with people&#x27;s cells. Then realized we also need to make sure we still have them.</p>
    </div>

    <div class="n">
      <h3>4. Infrastructure like AWS or ASML</h3>
      <p>This is the infrastructure story.</p>
      <p>Cryopreservation isn&#x27;t new.<br>Blood collection isn&#x27;t new.<br>Cell isolation isn&#x27;t new.<br>Long-term cryogenic storage isn&#x27;t new.</p>
      <p>But none of those things alone creates a consumer infrastructure for preserving your biology.</p>
      <p>That&#x27;s the interesting part.</p>
      <p>ASML didn&#x27;t invent semiconductor physics.<br>AWS didn&#x27;t invent the internet.<br>They built infrastructure that made something much bigger possible at scale.</p>
      <p class="so"><b>So, for Reservoir:</b> The angle:<br><br><i>&quot;The science already existed. <b>The infrastructure didn&#x27;t.</b> So we built it.&quot;</i><br><br>From your blood draw to cells preserved for decades. That&#x27;s the story.<br>Not: <b>&quot;We freeze cells.&quot;</b><br>It&#x27;s: <b>&quot;We built the infrastructure for preserved human biology.&quot;</b></p>
    </div>

    <div class="n">
      <h3>5. Bryan Johnson / Project Blueprint</h3>
      <p>Bryan Johnson gets an insane amount of shit on X.</p>
      <p>And that&#x27;s exactly why this works.<br>Everyone has an opinion on Blueprint.<br>Everyone makes jokes about him trying to become immortal.</p>
      <p>But what if he&#x27;s right about the most basic thing?</p>
      <p><b>What if the future of medicine is radically better than medicine today?</b></p>
      <p>That&#x27;s the bet behind everything he&#x27;s doing.<br>And Reservoir can actually support that idea without becoming another Blueprint.</p>
      <p class="so"><b>So, for Reservoir:</b> The post:<br><br><i>&quot;Everyone makes fun of Bryan Johnson. <b>What if he&#x27;s right?</b><br>What if medicine in 2045 can do things that sound completely impossible today?<br>Then maybe the dumbest thing you could do is throw away the biology you had in 2026. Because you can&#x27;t get it back.&quot;</i><br><br>Give Bryan the love. Don&#x27;t attack him. <b>Make the people who think he&#x27;s crazy question whether he might actually be early.</b></p>
    </div>

    <div class="n">
      <h3>6. Rage bait / memes</h3>
      <p>This is the &quot;what the fuck is this startup?&quot; angle.</p>
      <p>The product is naturally absurd to someone hearing about it for the first time.<br>You don&#x27;t need Reservoir today.<br>You might need it in 20 years.<br>So make that the entire joke.</p>
      <div class="media quote-card" style="margin:8px 0;">
        <b>&quot;We just built a startup you might not need for 20 years.&quot;</b>
        <p>Give us blood. We&#x27;ll preserve your cells. Then you wait. That&#x27;s literally it.</p>
      </div>
      <p>People will immediately start arguing: <b>&quot;Why would I do this?&quot; &quot;What would I even use them for?&quot; &quot;This is insane.&quot;</b></p>
      <p>Perfect.</p>
      <p class="so"><b>So, for Reservoir:</b> Don&#x27;t fight the comments. The comments become the explainer.</p>
    </div>

    <div class="n">
      <h3>7. Aging can be stopped. The proof is piling up.</h3>
      <p>Longevity is one of the biggest science conversations on X.</p>
      <p>Every few weeks there&#x27;s another paper showing something that would&#x27;ve sounded ridiculous a decade ago:<br>Cellular aging. Reprogramming. Senescent cells. Epigenetic changes. Biological age.</p>
      <p>The conversation is moving from: <b>&quot;Can we slow aging?&quot;</b> to: <b>&quot;How far can we actually reverse it?&quot;</b></p>
      <p>And this is where research performs extremely well on X. A paper drops. Someone posts the result. Scientists argue. Everyone starts asking whether aging is actually something we can manipulate.</p>
      <p class="so"><b>So, for Reservoir:</b> Don&#x27;t use the research to claim Reservoir reverses aging. Use it to establish the bigger premise:<br><br><b>The biology of aging is becoming something scientists can actually manipulate.</b><br>And if biology is going to change dramatically over the next few decades: <b>why throw away the biology you have today?</b></p>
    </div>

    <div class="n">
      <h3>8. Competition is cooked</h3>
      <p>This is the most aggressive longevity angle.</p>
      <p>There are startups everywhere trying to figure out how to make old biology young again:<br>NewLimit, Altos, Retro, Life Biosciences, BioAge.</p>
      <p>Billions are going into figuring out how to reverse or slow aspects of aging.</p>
      <p>And Reservoir comes along with a completely different idea:</p>
      <p><b>What if we don&#x27;t need to make the old cells young? What if we just saved the young ones?</b></p>
      <p class="so"><b>So, for Reservoir:</b> The post:<br><br><i>The longevity industry is spending billions trying to make old cells young again.<br>Reservoir: <b>&quot;Why didn&#x27;t you just save them?&quot;</b></i><br><br>This should create an argument. Obviously these approaches can coexist. But the cultural narrative is extremely strong: <b>Make old cells young vs preserve young cells.</b></p>
    </div>

    <div class="n">
      <h3>9. Sci-fi is becoming real</h3>
      <p>This is the science-fiction story.</p>
      <p><i>Passengers. 2001: A Space Odyssey. Alien.</i></p>
      <p>For decades, movies have imagined humans preserving themselves for a future they can&#x27;t predict: Cryosleep. Suspended animation. Waking up decades later.</p>
      <p>Obviously Reservoir isn&#x27;t freezing humans. But the underlying concept is suddenly much less fictional:</p>
      <p><b>Preserve something from today for a future that doesn&#x27;t exist yet.</b></p>
      <p class="so"><b>So, for Reservoir:</b> The post:<br><br><i>&quot;We&#x27;ve spent 50 years watching science fiction preserve humans for the future. <b>We started with their cells.</b>&quot;</i><br><br>Then show the actual blood draw. Then the processing. Then the cells going into long-term storage.<br><b>That&#x27;s the reveal.</b></p>
    </div>
  </section>
</section>"""

# Find and replace section#tab-intro
pattern = r'<section class="tab" id="tab-intro">.*?</section>'
match = re.search(pattern, html, re.DOTALL)
if match:
    html = html[:match.start()] + new_tab_intro + html[match.end():]
    print("Matched and replaced tab-intro cleanly!")
else:
    print("Could not find tab-intro pattern")

with open("public/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated public/index.html with exact new first page!")
