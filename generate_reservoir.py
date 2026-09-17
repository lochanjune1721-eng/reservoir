import os

html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Reservoir Launch Brief</title>
<meta name="robots" content="noindex, nofollow">
<style>
:root{--bg:#ffffff;--ink:#0f1419;--muted:#536471;--line:#eff3f4;--line2:#cfd9de;--blue:#1d9bf0;--blue-soft:#e8f5fe;--cell:#f7f9f9;--green:#00ba7c;--green-soft:#edfbf4;}
*{box-sizing:border-box}html{scroll-behavior:smooth}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:15px;line-height:1.35}
a{color:var(--blue);text-decoration:none}a:hover{text-decoration:underline}a:focus-visible,summary:focus-visible{outline:2px solid var(--blue);outline-offset:2px;border-radius:4px}
.shell{max-width:1080px;margin:0 auto;display:grid;grid-template-columns:260px 1fr;gap:0 30px;padding:0 16px}
@media(max-width:960px){.shell{grid-template-columns:1fr;max-width:680px}.side{display:none}}
.side{position:sticky;top:0;height:100vh;padding:12px 0;display:flex;flex-direction:column;gap:3px;overflow-y:auto}
.side .logo{font-weight:800;font-size:21px;padding:10px 14px;letter-spacing:-.02em;display:flex;align-items:center;gap:8px}
.side .logo svg{flex-shrink:0}
.side a{display:block;padding:9px 14px;border-radius:999px;color:var(--ink);font-size:15px;font-weight:600;transition:background .15s}.side a:hover{background:var(--cell);text-decoration:none}
.side a.active{color:var(--blue);background:var(--blue-soft)}
.side .tag{margin-top:auto;padding:12px 14px;color:var(--muted);font-size:12.5px;line-height:1.4}
.main{border-left:1px solid var(--line);border-right:1px solid var(--line);min-height:100vh;min-width:0}
.top{position:sticky;top:0;z-index:5;background:rgba(255,255,255,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line);padding:12px 16px;font-weight:800;font-size:19px}
.top small{display:block;font-weight:400;font-size:13px;color:var(--muted);margin-top:2px}
.tabs{position:sticky;top:0;z-index:6;display:flex;background:rgba(255,255,255,.95);backdrop-filter:blur(10px);border-bottom:1px solid var(--line);overflow-x:auto;scrollbar-width:none;-ms-overflow-style:none}
.tabs::-webkit-scrollbar{display:none}
.tb{flex:1 0 auto;background:none;border:0;padding:14px 12px 12px;font:inherit;font-size:14px;font-weight:700;color:var(--muted);cursor:pointer;position:relative;white-space:nowrap}
.tb[aria-selected="true"]{color:var(--ink)}.tb[aria-selected="true"]::after{content:"";position:absolute;left:10px;right:10px;bottom:0;height:4px;border-radius:4px;background:var(--blue)}
.tb:hover{background:var(--cell)}.tb:focus-visible{outline:2px solid var(--blue);outline-offset:-2px}

.art{padding:18px 18px 30px;border-bottom:1px solid var(--line)}
.art h2{font-size:24px;font-weight:800;letter-spacing:-.01em;margin:4px 0 10px;line-height:1.2}
.art .sub{color:var(--muted);margin:0 0 16px;font-size:15px;line-height:1.4}
.art ul,.art ol{margin:0;padding-left:22px}.art li{margin:0 0 10px;font-size:15px;line-height:1.45}
.art .n{padding:14px 0;border-top:1px solid var(--line)}.art .n:first-of-type{border-top:0}
.art h3{font-size:17px;font-weight:800;margin:0 0 6px}.art .n p{margin:0 0 8px;font-size:15px;line-height:1.45}
.art .so{color:var(--ink);background:var(--blue-soft);padding:10px 12px;border-radius:10px;border-left:3px solid var(--blue);margin-top:8px}
.art .so b{color:var(--blue);font-weight:700}

.ahead{padding:16px 18px 14px;border-bottom:1px solid var(--line);background:var(--cell)}
.ahead .k{display:inline-block;background:var(--ink);color:#fff;font-size:11px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;border-radius:999px;padding:3px 10px;margin-bottom:6px}
.ahead h2{font-size:24px;font-weight:800;letter-spacing:-.01em;margin:4px 0 8px;line-height:1.2}
.ahead .one{margin:0 0 10px;font-size:15.5px;line-height:1.45;color:var(--ink)}
.ahead .who{margin:0 0 12px;font-size:13.5px;color:var(--muted)}.ahead .who b{color:var(--ink)}
.ahead .blk{border-top:1px solid var(--line2);padding:10px 0 4px}.ahead h4{margin:0 0 6px;font-size:14px;font-weight:700}
.ahead ol,.ahead ul{margin:6px 0 4px;padding-left:22px}.ahead li{font-size:14px;line-height:1.45;margin:0 0 6px}
.ahead .avoid{list-style:none;padding-left:0}.ahead .avoid li{position:relative;padding-left:18px;list-style:none}.ahead .avoid li::before{content:"✕";position:absolute;left:0;top:0;font-size:12px;font-weight:700;color:#f4212e}
.ahead .lines li{font-style:italic;color:#0f1419}

.post{display:grid;grid-template-columns:42px 1fr;gap:0 12px;padding:14px 16px 10px;border-bottom:1px solid var(--line);transition:background .15s}
.post:hover{background:#fafcfc}
.hero-post{background:#fbfdff;border-bottom:2px solid var(--line)}
.av{border-radius:50%;display:block}
.ph-row{display:flex;align-items:center;gap:5px;font-size:15px;flex-wrap:wrap}.ph-row b{font-weight:700}.ph-row .h,.ph-row .dot{color:var(--muted)}.ph-row .line{margin-left:auto;font-size:11px;font-weight:700;color:var(--muted);border:1px solid var(--line2);border-radius:4px;padding:1px 6px;text-transform:uppercase}
.vb{margin-left:1px;vertical-align:middle}
.txt{white-space:pre-wrap;font-size:15px;line-height:1.42;margin:4px 0 10px;word-wrap:break-word}
.media{position:relative;display:block;width:100%;border:1px solid var(--line2);border-radius:14px;overflow:hidden;background:var(--cell);margin:0 0 8px;padding:14px 16px}
.media.quote-card{border-left:4px solid var(--blue);background:#fbfdff}
.media.quote-card b{display:block;font-size:15px;margin-bottom:4px}
.media.quote-card p{margin:0;font-size:14px;color:var(--muted);line-height:1.4}
.acts{display:flex;justify-content:space-between;max-width:440px;padding:4px 0 2px;margin-left:-6px}.acts span{display:flex;align-items:center;justify-content:center;gap:4px;min-width:32px;height:32px;border-radius:50%;color:var(--muted);font-size:12px;cursor:pointer;transition:all .15s}.acts span:hover{background:var(--blue-soft);color:var(--blue)}.acts svg{width:16px;height:16px;fill:currentColor}
.note{margin:8px 0 4px;padding:9px 12px;border-radius:8px;background:var(--cell);font-size:13px;line-height:1.4;color:var(--muted);border-left:3px solid var(--line2)}.note b{color:var(--ink)}
.foot{padding:24px 18px 60px;color:var(--muted);font-size:13px;text-align:center}

@media(max-width:680px){
  .shell{padding:0}.main{border:0}.post{padding:12px 14px 8px}.art,.ahead{padding-left:14px;padding-right:14px}.tb{font-size:13px;padding:12px 8px 10px}
}
</style>
</head>
<body>
<div class="shell">
<aside class="side">
  <div class="logo">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
      <circle cx="12" cy="12" r="10" stroke="#0f1419" stroke-width="2.2"/>
      <path d="M7 12c1.5-2 3.5-2 5 0s3.5 2 5 0" stroke="#1d9bf0" stroke-width="2.2" stroke-linecap="round"/>
      <circle cx="12" cy="7" r="1.5" fill="#1d9bf0"/>
      <circle cx="12" cy="17" r="1.5" fill="#1d9bf0"/>
    </svg>
    Reservoir Brief
  </div>
  <a href="#intro" data-tab="intro" class="active">Brief</a>
  <a href="#a1" data-tab="a1">AI Doomer</a>
  <a href="#a2" data-tab="a2">Billionaires</a>
  <a href="#a3" data-tab="a3">Founder</a>
  <a href="#a4" data-tab="a4">Research</a>
  <a href="#a5" data-tab="a5">Bryan Johnson</a>
  <a href="#a6" data-tab="a6">Rage Bait</a>
  <a href="#a7" data-tab="a7">Science Fiction</a>
  <a href="#a8" data-tab="a8">Infrastructure</a>
  <a href="#a9" data-tab="a9">Anti-Aging</a>
  <div class="tag">Reservoir Cultural Narrative Map<br>Shown Media Strategy Brief</div>
</aside>

<main class="main">
<div class="tabs" role="tablist">
  <button type="button" role="tab" class="tb" data-tab="intro" aria-selected="true">Brief</button>
  <button type="button" role="tab" class="tb" data-tab="a1" aria-selected="false">AI Doomer</button>
  <button type="button" role="tab" class="tb" data-tab="a2" aria-selected="false">Billionaires</button>
  <button type="button" role="tab" class="tb" data-tab="a3" aria-selected="false">Founder</button>
  <button type="button" role="tab" class="tb" data-tab="a4" aria-selected="false">Research</button>
  <button type="button" role="tab" class="tb" data-tab="a5" aria-selected="false">Bryan Johnson</button>
  <button type="button" role="tab" class="tb" data-tab="a6" aria-selected="false">Rage Bait</button>
  <button type="button" role="tab" class="tb" data-tab="a7" aria-selected="false">Sci-Fi</button>
  <button type="button" role="tab" class="tb" data-tab="a8" aria-selected="false">Infrastructure</button>
  <button type="button" role="tab" class="tb" data-tab="a9" aria-selected="false">Anti-Aging</button>
</div>

<!-- TAB INTRO -->
<section class="tab" id="tab-intro">
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
      <div class="txt">We built a startup you might not need for 20 years. Until medicine gets really good.

The biggest conversations in tech right now are whether AI will destroy humanity, whether billionaires are hiding in bunkers, and whether we can radically extend human life.

Dario Amodei, Jensen Huang, and Sam Altman are all betting AI will compress decades of biological breakthroughs into the next 5 to 10 years.

There is only one catch nobody talks about:

When miraculous cellular reprogramming and personalized therapies arrive in 2040... you won&#x27;t have the cells you have today.

Introducing Reservoir. Consumer infrastructure for human cellular preservation.
15-minute blood draw → cell isolation → cryogenic preservation for decades.

Don&#x27;t just survive the transition to the future. Make sure your biology is there to live it.</div>
      <div class="media quote-card">
        <b>Reservoir Launch Thesis</b>
        <p>Cultural Narrative Map: Each angle starts with something people on X are already furiously arguing about, then Reservoir enters that conversation in an unexpected, provocative way.</p>
      </div>
      <div class="acts">
        <span><svg viewBox="0 0 24 24"><path d="M14.046 2.242l-4.148-.01h-.002c-4.374 0-7.8 3.427-7.8 7.802 0 4.098 3.186 7.206 7.465 7.37v3.828c0 .108.044.286.12.403.142.225.384.347.632.347.138 0 .277-.038.402-.118.264-.168 6.473-4.14 8.088-5.506 1.902-1.61 3.04-3.97 3.04-6.324 0-4.375-3.426-7.799-7.799z"/></svg> 1.8K</span>
        <span><svg viewBox="0 0 24 24"><path d="M23.77 15.67c-.292-.293-.767-.293-1.06 0l-2.22 2.22V7.65c0-2.068-1.683-3.75-3.75-3.75h-5.85c-.414 0-.75.336-.75.75s.336.75.75.75h5.85c1.24 0 2.25 1.01 2.25 2.25v10.24l-2.22-2.22c-.293-.293-.768-.293-1.06 0s-.294.768 0 1.06l3.5 3.5c.145.147.337.22.53.22s.383-.072.53-.22l3.5-3.5c.294-.292.294-.767 0-1.06zm-10.66 3.28H7.26c-1.24 0-2.25-1.01-2.25-2.25V6.46l2.22 2.22c.148.147.34.22.53.22s.384-.073.53-.22c.293-.293.293-.768 0-1.06l-3.5-3.5c-.293-.294-.768-.294-1.06 0l-3.5 3.5c-.294.292-.294.767 0 1.06s.767.293 1.06 0l2.22-2.22V16.7c0 2.068 1.683 3.75 3.75 3.75h5.85c.414 0 .75-.336.75-.75s-.336-.75-.75-.75z"/></svg> 4.2K</span>
        <span><svg viewBox="0 0 24 24"><path d="M12 21.638h-.014C9.403 21.59 1.95 14.856 1.95 8.478c0-3.064 2.525-5.754 5.403-5.754 2.29 0 3.83 1.58 4.646 2.73.814-1.148 2.354-2.73 4.645-2.73 2.88 0 5.404 2.69 5.404 5.755 0 6.376-7.454 13.11-10.034 13.156H12z"/></svg> 19.4K</span>
        <span><svg viewBox="0 0 24 24"><path d="M8.75 21V3h2v18h-2zM18 21V8.5h2V21h-2zM4 21l.005-6.5H6V21H4zm9.248 0v-9h2v9h-2z"/></svg> 840K</span>
      </div>
    </div>
  </article>

  <section class="art" id="launch">
    <h2>The Launch Strategy</h2>
    <p class="sub">What you actually want is a cultural narrative map, where each angle starts with something people are already arguing about, then Reservoir enters that conversation in an unexpected way.</p>
    <ol>
      <li><b>The AI-doomer angle should be much more aggressive.</b> If AI can cure diseases and reverse biological damage, are we actually going to slow it down? If stopping AI means stopping technology that could save millions of lives, aren&#x27;t slowdown advocates potentially mass-murdering the future?</li>
      <li><b>Billionaires are preparing for a future nobody else is ready for.</b> The richest people on Earth are pouring fortune into bunkers, cryonics, and experimental medicine. What if preserving your biology is the one tangible step you should take before the technology arrives?</li>
      <li><b>The founder story isn&#x27;t generic biotech.</b> Nabiha Saklayen: Harvard laser physics, losing her grandmother, cell reprogramming, founding Cellino. The person who spent years building the tools to manipulate human cells realized we also needed to save them.</li>
      <li><b>Research papers: not rejuvenating old cells, but preserving young cells.</b> Cryobiology and immune-cell banking across the lifespan (PubMed, Geromedicine). The research provides the unshakeable credibility layer underneath the cultural narrative.</li>
      <li><b>Bryan Johnson gets mocked constantly. We give him love.</b> He is running a public experiment around radical life extension and immortality by 2039. What if he&#x27;s right? Wouldn&#x27;t you want your biology from today waiting for it?</li>
      <li><b>Rage bait: the startup you won&#x27;t need for 20 years.</b> Spark explosive debate: &quot;Why would I freeze my cells? This is bullshit!&quot; The answer is the entire thesis: We don&#x27;t know what future medicine will need yet. That&#x27;s the point.</li>
      <li><b>Science fiction is becoming real.</b> <i>Passengers</i>, <i>Alien</i>, <i>2001</i> all imagined biological time travel. Reservoir is the real-world, cell-level version.</li>
      <li><b>The infrastructure story: ASML for biology.</b> ASML didn&#x27;t invent silicon. AWS didn&#x27;t invent the internet. Reservoir didn&#x27;t invent cryo. It built the consumer-scale pipeline.</li>
      <li><b>Anti-aging startups vs. cell preservation.</b> Longevity VCs are spending billions trying to make 70-year-old cells act like 30-year-old cells. Why not just keep your 30-year-old cells?</li>
    </ol>
  </section>

  <section class="art" id="narrative">
    <h2>What's the narrative on X?</h2>
    <p class="sub">Nine cultural debates already dominating X. Each one is a high-traffic doorway for Reservoir.</p>
    
    <div class="n">
      <h3>1. AI Doomers are arguing about whether AI will destroy humanity</h3>
      <p>Dario Amodei is warning about the risks of frontier AI while arguing AI could cure most major diseases in 5–10 years. Jensen Huang calls doomerism unhelpful. Trump pushed back on AI slowdowns.</p>
      <p class="so"><b>So, for Reservoir:</b> If stopping AI stops the cure to diseases, slowdown advocates are arguing for millions of preventable deaths. And if AI does save us, you want your pristine biology to still be there.</p>
    </div>

    <div class="n">
      <h3>2. Billionaires are preparing for a future nobody else is ready for</h3>
      <p>Massive internet obsession with tech billionaires building apocalypse bunkers, funding Altos Labs, Retro Biosciences, and experimental longevity treatments.</p>
      <p class="so"><b>So, for Reservoir:</b> The richest people on Earth are investing fortunes into technologies that don&#x27;t exist yet. What if preserving your cellular biology is what you should do before that technology arrives?</p>
    </div>

    <div class="n">
      <h3>3. The founder story: she spent years figuring out what we can do with cells</h3>
      <p>Physics at Harvard → laser biophysics → loss of grandmother → cellular reprogramming → building Cellino to automate cell therapies.</p>
      <p class="so"><b>So, for Reservoir:</b> The person who spent a decade mastering how to manipulate human cells realized the ultimate limiting factor: if you don&#x27;t save your younger cells now, future medicine won&#x27;t have pristine raw material.</p>
    </div>

    <div class="n">
      <h3>4. Research papers: we&#x27;re not trying to make old cells young</h3>
      <p>We don&#x27;t use speculative rejuvenation claims. We cite rigorous cryopreservation research showing immune-cell banking is already an enabling technology for modern therapies (PubMed 39113431, Geromedicine 2026.0026).</p>
      <p class="so"><b>So, for Reservoir:</b> We build a credible science series on immune-cell aging, cryo-viability, and long-term lifespan banking as the unshakeable foundation for the brand.</p>
    </div>

    <div class="n">
      <h3>5. Bryan Johnson gets shit on constantly. We&#x27;re going to give him the love.</h3>
      <p>The internet mocks his Blueprint diet, plasma swaps, and &quot;Don&#x27;t Die&quot; mantra. Yet he is publicly pursuing immortality by 2039.</p>
      <p class="so"><b>So, for Reservoir:</b> Turn the meme on its head: Mock him all you want, but what if he&#x27;s right? When radical life extension arrives, you will desperately wish you had your 2026 biology waiting for it.</p>
    </div>

    <div class="n">
      <h3>6. Rage bait: build a startup you might need in 20 years</h3>
      <p>&quot;This might be the dumbest startup idea ever. Until medicine gets really good.&quot; Provoking people into arguing about utility drives massive reach.</p>
      <p class="so"><b>So, for Reservoir:</b> When critics shout &quot;Why would I freeze my cells? What will I use them for?&quot; we answer: We don&#x27;t know yet. That&#x27;s the entire thesis.</p>
    </div>

    <div class="n">
      <h3>7. Science fiction is becoming real</h3>
      <p><i>Passengers</i>, <i>Alien</i>, <i>Interstellar</i>, and <i>2001</i> captivated humanity with cryosleep across deep time.</p>
      <p class="so"><b>So, for Reservoir:</b> Sci-fi imagined preserving the whole body. Reservoir builds the practical real-world counterpart: preserving the critical cellular material so it can meet medicine that hasn&#x27;t been invented yet.</p>
    </div>

    <div class="n">
      <h3>8. The infrastructure story: ASML for biology</h3>
      <p>ASML didn&#x27;t invent silicon. AWS didn&#x27;t invent the internet. Reservoir didn&#x27;t invent liquid nitrogen or cell separation.</p>
      <p class="so"><b>So, for Reservoir:</b> Reservoir engineered the end-to-end consumer network: 15-minute blood draw → cold chain → cellular isolation → cryogenic banking. The infrastructure is the product.</p>
    </div>

    <div class="n">
      <h3>9. The longevity industry is trying to make old cells young. We&#x27;re keeping young cells.</h3>
      <p>Billions flow into partial reprogramming and cellular rejuvenation trying to reverse epigenetic damage.</p>
      <p class="so"><b>So, for Reservoir:</b> The counter-intuitive bet: Why spend a fortune trying to make 70-year-old damaged cells act 30, when you can just bank your 30-year-old cells today?</p>
    </div>
  </section>

  <section class="art" id="angles">
    <h2>The Nine Angles</h2>
    <ol>
      <li><a href="#a1" data-tab="a1"><b>Angle 1. AI Doomers:</b></a> Everyone is asking whether AI will destroy humanity. What if slowing AI means stopping the technology that could cure diseases and save millions of lives? Dario himself has argued AI could cure most major diseases. That&#x27;s the debate Reservoir enters.</li>
      <li><a href="#a2" data-tab="a2"><b>Angle 2. Billionaires:</b></a> Everyone is obsessed with billionaires building bunkers and preparing for the future. What are the people with unlimited money actually doing? What if preserving biology is what you must do before tech arrives?</li>
      <li><a href="#a3" data-tab="a3"><b>Angle 3. Founder:</b></a> She spent years learning how to manipulate human cells. Then realized we needed to preserve them. Physics → lasers → biology → Cellino → personalized medicine → Reservoir.</li>
      <li><a href="#a4" data-tab="a4"><b>Angle 4. Research:</b></a> Don&#x27;t use rejuvenation papers as proof. Build a research series specifically around cell aging, immune-cell preservation, cryopreservation, viability, and future biological banking.</li>
      <li><a href="#a5" data-tab="a5"><b>Angle 5. Bryan Johnson:</b></a> Everyone makes fun of Bryan Johnson. We ask: what if he&#x27;s right? He made biological aging a public experiment. Wouldn&#x27;t you want your biology waiting for the future?</li>
      <li><a href="#a6" data-tab="a6"><b>Angle 6. Rage bait:</b></a> We just built a startup you might not need for 20 years. Let people argue about whether it&#x27;s insane. You don&#x27;t know what future medicine will need until that future arrives.</li>
      <li><a href="#a7" data-tab="a7"><b>Angle 7. Science fiction:</b></a> Passengers, Alien, and 2001 imagined humans surviving enormous gaps in time. Reservoir flips the idea from preserving the whole human to preserving the cells that matter.</li>
      <li><a href="#a8" data-tab="a8"><b>Angle 8. Infrastructure:</b></a> ASML for chips, AWS for software, Reservoir for human biology. The individual processes existed; connecting them into a consumer network is the story.</li>
      <li><a href="#a9" data-tab="a9"><b>Angle 9. Anti-aging startups:</b></a> Everyone is trying to make old cells young. Reservoir is keeping young cells from becoming old. Make people argue about which approach wins over a 20–30 year horizon.</li>
    </ol>
  </section>
</section>

<!-- TAB A1: AI DOOMER -->
<section class="tab" id="tab-a1" hidden>
  <div class="ahead">
    <span class="k">Angle 1</span>
    <h2>The AI Doomer Inversion: Are AI Slowdown Advocates Mass-Murdering the Future?</h2>
    <p class="one">Enter the biggest tech debate from the opposite extreme: If AI can cure diseases and reverse biological damage, are we actually going to slow it down?</p>
    <p class="who"><b>Who to target:</b> e/acc, AI X, Dario Amodei, Jensen Huang, Yann LeCun, AI safety community.</p>
    <div class="blk">
      <h4>The Hook & Tension</h4>
      <p>Dario Amodei warns about catastrophic frontier risk while writing in &quot;Machines of Loving Grace&quot; that AI could compress 50–100 years of biological breakthroughs into 5–10 years. Jensen Huang argues that slowing AI is dangerous and counterproductive. Trump pushes back on AI regulations.</p>
      <p>Reservoir enters with the most aggressive counter-position: If slowing AI stops the technology that cures cancer, Alzheimer&#x27;s, and organ failure, isn&#x27;t pausing AI effectively a death sentence for millions?</p>
    </div>
    <div class="blk">
      <h4>Lines to Use</h4>
      <ul class="lines">
        <li>&quot;Everyone is asking what happens if AI kills us. What if AI is the thing that saves us?&quot;</li>
        <li>&quot;If AI cures disease in 10 years, the only real tragedy is dying in year 9.&quot;</li>
        <li>&quot;You can argue about p(doom) all day. But if superintelligence cures biological decay, you want your biology to still be there.&quot;</li>
      </ul>
    </div>
  </div>

  <article class="post" id="p1-1">
    <div class="pl"><svg class="av" width="40" height="40" viewBox="0 0 40 40"><rect width="40" height="40" rx="20" fill="#0f1419"/><text x="12" y="26" fill="#fff" font-weight="700" font-size="16">R</text></svg></div>
    <div class="pr">
      <div class="ph-row"><b>Reservoir</b><svg class="vb" viewBox="0 0 22 22" width="18" height="18"><path fill="#1d9bf0" d="M20.396 11c-.018-.646-.215-1.275-.57-1.816-.354-.54-.852-.972-1.438-1.246.223-.607.27-1.264.14-1.897-.131-.634-.437-1.218-.882-1.687-.47-.445-1.053-.75-1.687-.882-.633-.13-1.29-.083-1.897.14-.273-.587-.704-1.086-1.245-1.44S11.647 1.62 11 1.604c-.646.017-1.273.213-1.813.568s-.969.854-1.24 1.44c-.608-.223-1.267-.272-1.902-.14-.635.13-1.22.436-1.69.882-.445.47-.749 1.055-.878 1.688-.13.633-.08 1.29.144 1.896-.587.274-1.087.705-1.443 1.245-.356.54-.555 1.17-.574 1.817.02.647.218 1.276.574 1.817.356.54.856.972 1.443 1.245-.224.606-.274 1.263-.144 1.896.13.634.434 1.218.877 1.688.47.443 1.054.747 1.687.878.633.132 1.29.084 1.897-.136.274.586.705 1.084 1.246 1.439.54.354 1.17.551 1.816.569.647-.016 1.276-.213 1.817-.567s.972-.854 1.245-1.44c.604.239 1.266.296 1.903.164.636-.132 1.22-.447 1.68-.907.46-.46.776-1.044.908-1.681s.075-1.299-.165-1.903c.586-.274 1.084-.705 1.439-1.246.354-.54.551-1.17.569-1.816zM9.662 14.85l-3.429-3.428 1.293-1.302 2.072 2.072 4.4-4.794 1.347 1.246z"/></svg><span class="h">@reservoir_bio</span><span class="dot">·</span><span class="h">1d</span><span class="line">doomer debate</span></div>
      <div class="txt">Dario Amodei says AI will cure most diseases in 5 to 10 years.

At the same time, AI doomers are petitioning governments to pause frontier models.

If stopping AI means stopping the technology that cures cancer and reverses organ failure, aren&#x27;t slowdown advocates potentially signing death warrants for tens of millions of people?

The entire internet is debating what happens if AI kills us.

Nobody is preparing for what happens if AI actually saves us.

When superintelligence figures out how to reprogram human biology, you want your cells from today preserved and waiting.</div>
      <div class="note"><b>Why this works:</b> Reframes the doomer debate from abstract rogue AI into immediate human lives saved vs lost, and plants cellular banking right at the center of the solution.</div>
    </div>
  </article>
</section>

<!-- TAB A2: BILLIONAIRES -->
<section class="tab" id="tab-a2" hidden>
  <div class="ahead">
    <span class="k">Angle 2</span>
    <h2>Billionaires Are Preparing for a Future Nobody Else Is Ready For</h2>
    <p class="one">The richest and most future-obsessed people on Earth are spending enormous fortunes preparing for technologies that don&#x27;t exist yet.</p>
    <p class="who"><b>Who to target:</b> Wealth watchers, Peter Thiel, Jeff Bezos, Sam Altman, tech culture commentators.</p>
    <div class="blk">
      <h4>The Narrative</h4>
      <p>The internet fixates on bunkers, cryonics, and billionaires funding anti-aging moonshots. But the angle isn&#x27;t &quot;billionaires preserve their cells.&quot; We verify every individual claim: Altos Labs ($3B), Retro Biosciences ($180M), Peter Thiel&#x27;s parabiosis and cryonics interest.</p>
      <p>Then Reservoir introduces the democratizing counter-punch: Billionaires are banking on experimental breakthroughs. But you don&#x27;t need a billion dollars to preserve your pristine immune cells today.</p>
    </div>
  </div>

  <article class="post" id="p2-1">
    <div class="pl"><svg class="av" width="40" height="40" viewBox="0 0 40 40"><rect width="40" height="40" rx="20" fill="#1d9bf0"/><text x="11" y="26" fill="#fff" font-weight="700" font-size="14">TW</text></svg></div>
    <div class="pr">
      <div class="ph-row"><b>Tech Watcher</b><span class="h">@techinsider</span><span class="dot">·</span><span class="h">3d</span><span class="line">curiosity</span></div>
      <div class="txt">Jeff Bezos put $3 billion into Altos Labs to crack cellular rejuvenation.
Sam Altman poured $180 million into Retro Biosciences to add 10 healthy years to human life.
Peter Thiel signed up for cryonics decades ago.

Everyone mocks them for &quot;billionaire death fear.&quot;

What if they simply understand the math?

If medical technology hits an inflection point in the 2030s, the only people who lose are those who didn&#x27;t preserve their baseline biology.

@reservoir_bio is doing what billionaires do, but for the rest of us.</div>
      <div class="note"><b>Why this works:</b> Anchors Reservoir alongside the most verified, high-profile longevity investments in history, framing cellular banking as the obvious rational hedge.</div>
    </div>
  </article>
</section>

<!-- TAB A3: FOUNDER -->
<section class="tab" id="tab-a3" hidden>
  <div class="ahead">
    <span class="k">Angle 3</span>
    <h2>The Founder Story: She Spent Years Figuring Out What We Can Do With Cells</h2>
    <p class="one">Physics at Harvard → laser biophysics → losing her grandmother → cellular reprogramming → building Cellino → founding Reservoir.</p>
    <p class="who"><b>Who to target:</b> Biotech founders, deep-tech investors, Harvard alumni, women in STEM, personalized medicine builders.</p>
    <div class="blk">
      <h4>The Story Arc</h4>
      <p>This is not a generic startup bio. Nabiha Saklayen spent a decade developing laser physics to edit and manufacture induced pluripotent stem cells (iPSCs) at scale at Cellino. While building the future of cell therapies, she confronted the foundational bottleneck: by the time patients need autologous cellular medicine, their own cells are aged, mutated, and depleted.</p>
      <p>Reservoir was born from the realization that we need to preserve human biology while it is still young, viable, and genetically intact.</p>
    </div>
  </div>

  <article class="post" id="p3-1">
    <div class="pl"><svg class="av" width="40" height="40" viewBox="0 0 40 40"><rect width="40" height="40" rx="20" fill="#014421"/><text x="12" y="26" fill="#fff" font-weight="700" font-size="16">N</text></svg></div>
    <div class="pr">
      <div class="ph-row"><b>Nabiha Saklayen</b><svg class="vb" viewBox="0 0 22 22" width="18" height="18"><path fill="#1d9bf0" d="M20.396 11c-.018-.646-.215-1.275-.57-1.816-.354-.54-.852-.972-1.438-1.246.223-.607.27-1.264.14-1.897-.131-.634-.437-1.218-.882-1.687-.47-.445-1.053-.75-1.687-.882-.633-.13-1.29-.083-1.897.14-.273-.587-.704-1.086-1.245-1.44S11.647 1.62 11 1.604c-.646.017-1.273.213-1.813.568s-.969.854-1.24 1.44c-.608-.223-1.267-.272-1.902-.14-.635.13-1.22.436-1.69.882-.445.47-.749 1.055-.878 1.688-.13.633-.08 1.29.144 1.896-.587.274-1.087.705-1.443 1.245-.356.54-.555 1.17-.574 1.817.02.647.218 1.276.574 1.817.356.54.856.972 1.443 1.245-.224.606-.274 1.263-.144 1.896.13.634.434 1.218.877 1.688.47.443 1.054.747 1.687.878.633.132 1.29.084 1.897-.136.274.586.705 1.084 1.246 1.439.54.354 1.17.551 1.816.569.647-.016 1.276-.213 1.817-.567s.972-.854 1.245-1.44c.604.239 1.266.296 1.903.164.636-.132 1.22-.447 1.68-.907.46-.46.776-1.044.908-1.681s.075-1.299-.165-1.903c.586-.274 1.084-.705 1.439-1.246.354-.54.551-1.17.569-1.816zM9.662 14.85l-3.429-3.428 1.293-1.302 2.072 2.072 4.4-4.794 1.347 1.246z"/></svg><span class="h">@nabihasaklayen</span><span class="dot">·</span><span class="h">launch day</span><span class="line">founder</span></div>
      <div class="txt">I spent the last 8 years building the physics and AI to engineer human stem cells.

We made incredible progress. We learned how to manipulate human cells with laser precision.

And then I saw the wall the entire industry is running into:

When someone gets sick at 65 and needs personalized cell therapy... their own cells are exhausted, mutated, and depleted.

You can have the best biological manufacturing on Earth, but if you don&#x27;t have pristine starting material, your options are limited.

That&#x27;s why we founded @reservoir_bio.

Before we can use the medicines of tomorrow, we have to save the biology of today.</div>
      <div class="note"><b>Why this works:</b> Establishes domain authority. Nabiha isn&#x27;t an influencer selling wellness—she is a Harvard-trained laser biophysicist solving the real manufacturing bottleneck of cell therapy.</div>
    </div>
  </article>
</section>

<!-- TAB A4: RESEARCH -->
<section class="tab" id="tab-a4" hidden>
  <div class="ahead">
    <span class="k">Angle 4</span>
    <h2>Research Papers: We're Not Trying to Make Old Cells Young</h2>
    <p class="one">The scientific credibility layer: Cryopreservation of immune cells, viability retention, and lifelong biological banking.</p>
    <p class="who"><b>Who to target:</b> Academic bio Twitter, longevity researchers, clinicians, skeptical doctors.</p>
    <div class="blk">
      <h4>Peer-Reviewed Foundations</h4>
      <ul>
        <li><b>PubMed 39113431:</b> Cryopreservation of immune cells is already the foundational enabling technology for modern cellular therapies (CAR-T, stem cell transplants).</li>
        <li><b>Geromedicine 2026.0026:</b> Intersecting cryobiology with aging: expanding biological banking across human lifespan for future regenerative medicine.</li>
        <li><b>No Rejuvenation Hand-Waving:</b> We don&#x27;t claim cells can be magically resurrected. We prove that cryopreservation stops the biological clock cold at -196°C in liquid nitrogen.</li>
      </ul>
    </div>
  </div>

  <article class="post" id="p4-1">
    <div class="pl"><svg class="av" width="40" height="40" viewBox="0 0 40 40"><rect width="40" height="40" rx="20" fill="#0f1419"/><text x="12" y="26" fill="#fff" font-weight="700" font-size="16">R</text></svg></div>
    <div class="pr">
      <div class="ph-row"><b>Reservoir Science</b><span class="h">@reservoir_bio</span><span class="dot">·</span><span class="h">2d</span><span class="line">papers</span></div>
      <div class="txt">We don&#x27;t claim to reverse your biological age by 20 years. That&#x27;s speculative science.

Here is what is already clinically proven:

1. Immune-cell cryopreservation is the backbone of FDA-approved CAR-T cell therapies (PubMed 39113431).
2. Cells stored in liquid nitrogen at -196°C enter total metabolic stasis. Biochemical reactions cease.
3. Emerging work in Geromedicine shows that biological banking across the lifespan preserves genetic integrity before clonal hematopoiesis and thymic involution degrade immune diversity.

The future of medicine isn&#x27;t fixing broken cells. It&#x27;s having your unbroken cells ready.</div>
      <div class="media quote-card">
        <b>Citations & References</b>
        <p>• Frontiers in Aging: Trends in cellular rejuvenation and viability.<br>• PubMed 39113431: Immune cell cryopreservation and post-thaw efficacy.<br>• Geromedicine 2026.0026: Lifespan biological banking for future therapeutics.</p>
      </div>
    </div>
  </article>
</section>

<!-- TAB A5: BRYAN JOHNSON -->
<section class="tab" id="tab-a5" hidden>
  <div class="ahead">
    <span class="k">Angle 5</span>
    <h2>Bryan Johnson Gets Shit on Constantly. We're Going to Give Him the Love.</h2>
    <p class="one">Deliberately go against the internet meme grain: &quot;You can mock Bryan Johnson all you want. But what if he&#x27;s right?&quot;</p>
    <p class="who"><b>Who to target:</b> Blueprint followers, Don&#x27;t Die movement, fitness & health optimizers, tech skeptics.</p>
    <div class="blk">
      <h4>The Argument</h4>
      <p>Bryan Johnson is the internet&#x27;s favorite target. His diet, 100 pills a day, blood swaps, biomarkers, and declaration that he wants to achieve immortality by 2039. Everyone laughs.</p>
      <p>Reservoir takes the unexpected stance: He is running an open-source public experiment on human longevity. If radical life extension technology arrives, wouldn&#x27;t you want your 2026 biology preserved?</p>
    </div>
  </div>

  <article class="post" id="p5-1">
    <div class="pl"><svg class="av" width="40" height="40" viewBox="0 0 40 40"><rect width="40" height="40" rx="20" fill="#24292e"/><text x="12" y="26" fill="#fff" font-weight="700" font-size="14">BJ</text></svg></div>
    <div class="pr">
      <div class="ph-row"><b>Longevity Angle</b><span class="h">@blueprint_watch</span><span class="dot">·</span><span class="h">1d</span><span class="line">culture</span></div>
      <div class="txt">The internet spends all day making fun of Bryan Johnson.

His 100 pills.
His bedtime routine.
His &quot;Don&#x27;t Die&quot; shirts.
His claim that he wants to live forever by 2039.

You can laugh all you want.

But what if he&#x27;s right?
What if longevity escape velocity actually happens in the next 15 years?

If medicine arrives that can rebuild your immune system, wouldn&#x27;t you want your 2026 cells waiting in liquid nitrogen instead of starting from scratch at 60?

Laugh at Bryan Johnson. But bank your cells.</div>
      <div class="note"><b>Why this works:</b> Polarizing figures drive the highest quote-tweet volume. Defending his underlying thesis forces readers to evaluate their own future preparedness.</div>
    </div>
  </article>
</section>

<!-- TAB A6: RAGE BAIT -->
<section class="tab" id="tab-a6" hidden>
  <div class="ahead">
    <span class="k">Angle 6</span>
    <h2>Rage Bait: Build a Startup You Might Need in 20 Years</h2>
    <p class="one">Deliberately lean into the counter-intuitive absurdity: &quot;This might be the dumbest startup idea ever. Until medicine gets really good.&quot;</p>
    <p class="who"><b>Who to target:</b> Startup cynics, product hunt critics, Twitter tech debate accounts.</p>
    <div class="blk">
      <h4>The Virality Mechanics</h4>
      <p>Trigger the comments section: &quot;Why would anyone freeze their cells? You can&#x27;t even use them for anything right now! This is a scam!&quot;</p>
      <p>The trap snaps shut: <b>That is the entire thesis.</b> You don&#x27;t buy health insurance after you crash your car. You don&#x27;t preserve your cells after you have cancer. You preserve them when you don&#x27;t need them, so you have them when you do.</p>
    </div>
  </div>

  <article class="post" id="p6-1">
    <div class="pl"><svg class="av" width="40" height="40" viewBox="0 0 40 40"><rect width="40" height="40" rx="20" fill="#f4212e"/><text x="12" y="26" fill="#fff" font-weight="700" font-size="14">RB</text></svg></div>
    <div class="pr">
      <div class="ph-row"><b>Silicon Valley Takes</b><span class="h">@sv_takes</span><span class="dot">·</span><span class="h">4h</span><span class="line">debate</span></div>
      <div class="txt">We just found the dumbest startup idea of 2026:

A company that takes your blood, extracts your immune cells, puts them into liquid nitrogen, and charges you to keep them there for 20 years.

You can&#x27;t cure anything with them today.
You can&#x27;t inject them back tomorrow.
You literally just freeze them and wait.

...Unless medicine gets ridiculously good by 2040.

Then it might be the only startup that mattered.</div>
      <div class="note"><b>Why this works:</b> Bait first, real reason second. The mock skepticism attracts cynics who read to the end and realize the sheer logical asymmetry of the bet.</div>
    </div>
  </article>
</section>

<!-- TAB A7: SCIENCE FICTION -->
<section class="tab" id="tab-a7" hidden>
  <div class="ahead">
    <span class="k">Angle 7</span>
    <h2>Science Fiction Is Becoming Real: Biological Time Travel</h2>
    <p class="one">Passengers, Alien, Interstellar, and 2001: A Space Odyssey imagined humans surviving deep time. Reservoir is the real-world version.</p>
    <p class="who"><b>Who to target:</b> Sci-fi culture accounts, futurists, cinematic film critics, speculative tech writers.</p>
    <div class="blk">
      <h4>The Sci-Fi Bridge</h4>
      <p>For decades, Hollywood put astronauts into cryosleep pods so their bodies could traverse interstellar voids and arrive in a radically different future without aging. (Smithsonian Magazine analysis on cryosleep plausibility).</p>
      <p>Reservoir flips the trope: We are not freezing your entire body to cross space. We are freezing your critical cellular biology to cross time—letting your 25-year-old immune cells meet the medicines of 2050.</p>
    </div>
  </div>

  <article class="post" id="p7-1">
    <div class="pl"><svg class="av" width="40" height="40" viewBox="0 0 40 40"><rect width="40" height="40" rx="20" fill="#0b1e36"/><text x="12" y="26" fill="#fff" font-weight="700" font-size="14">SF</text></svg></div>
    <div class="pr">
      <div class="ph-row"><b>Futurism & Film</b><span class="h">@scifi_future</span><span class="dot">·</span><span class="h">1d</span><span class="line">cinema</span></div>
      <div class="txt">In Passengers, 2001, and Alien, humanity solved deep time with cryosleep:

Freeze human biology today so it can wake up in a future with advanced technology.

We always thought it was pure science fiction.

Turns out Hollywood had the scale wrong.
You don&#x27;t need to freeze the whole human.

You just need to freeze the cells that matter.

@reservoir_bio is building biological time travel at the cellular level.</div>
      <div class="media quote-card">
        <b>Smithsonian Magazine: The Plausibility of Cryosleep</b>
        <p>&quot;The science of cryopreservation has advanced from whole-organism fantasy to precise cellular vitrification, enabling living human cells to remain viable across decades of storage.&quot;</p>
      </div>
    </div>
  </article>
</section>

<!-- TAB A8: INFRASTRUCTURE -->
<section class="tab" id="tab-a8" hidden>
  <div class="ahead">
    <span class="k">Angle 8</span>
    <h2>The Infrastructure Story: ASML for Human Biology</h2>
    <p class="one">ASML didn&#x27;t invent silicon. AWS didn&#x27;t invent the internet. Reservoir didn&#x27;t invent cryopreservation. It built the consumer scaling pipeline.</p>
    <p class="who"><b>Who to target:</b> Deep tech investors, semiconductor & hardware thinkers, supply chain operators.</p>
    <div class="blk">
      <h4>The Industrial Pipeline</h4>
      <p>The individual technologies have existed for years: phlebotomy, ficoll density gradient separation, cryoprotectants, controlled-rate freezing, liquid nitrogen tanks at -196°C. But nobody connected them into a consumer-accessible network.</p>
      <p>The product isn&#x27;t the freezer. The infrastructure pipeline is the product:
      <b>15-min blood draw → certified cold chain → cell isolation → viability eval → cryopreservation → indefinite storage.</b></p>
    </div>
  </div>

  <article class="post" id="p8-1">
    <div class="pl"><svg class="av" width="40" height="40" viewBox="0 0 40 40"><rect width="40" height="40" rx="20" fill="#0f1419"/><text x="12" y="26" fill="#fff" font-weight="700" font-size="16">R</text></svg></div>
    <div class="pr">
      <div class="ph-row"><b>Reservoir</b><svg class="vb" viewBox="0 0 22 22" width="18" height="18"><path fill="#1d9bf0" d="M20.396 11c-.018-.646-.215-1.275-.57-1.816-.354-.54-.852-.972-1.438-1.246.223-.607.27-1.264.14-1.897-.131-.634-.437-1.218-.882-1.687-.47-.445-1.053-.75-1.687-.882-.633-.13-1.29-.083-1.897.14-.273-.587-.704-1.086-1.245-1.44S11.647 1.62 11 1.604c-.646.017-1.273.213-1.813.568s-.969.854-1.24 1.44c-.608-.223-1.267-.272-1.902-.14-.635.13-1.22.436-1.69.882-.445.47-.749 1.055-.878 1.688-.13.633-.08 1.29.144 1.896-.587.274-1.087.705-1.443 1.245-.356.54-.555 1.17-.574 1.817.02.647.218 1.276.574 1.817.356.54.856.972 1.443 1.245-.224.606-.274 1.263-.144 1.896.13.634.434 1.218.877 1.688.47.443 1.054.747 1.687.878.633.132 1.29.084 1.897-.136.274.586.705 1.084 1.246 1.439.54.354 1.17.551 1.816.569.647-.016 1.276-.213 1.817-.567s.972-.854 1.245-1.44c.604.239 1.266.296 1.903.164.636-.132 1.22-.447 1.68-.907.46-.46.776-1.044.908-1.681s.075-1.299-.165-1.903c.586-.274 1.084-.705 1.439-1.246.354-.54.551-1.17.569-1.816zM9.662 14.85l-3.429-3.428 1.293-1.302 2.072 2.072 4.4-4.794 1.347 1.246z"/></svg><span class="h">@reservoir_bio</span><span class="dot">·</span><span class="h">2d</span><span class="line">infrastructure</span></div>
      <div class="txt">ASML didn&#x27;t invent the transistor.
AWS didn&#x27;t invent the internet.
Reservoir didn&#x27;t invent cryopreservation.

What was missing was the infrastructure to make cellular banking reliable, scalable, and consumer-accessible.

Our pipeline:
1. 15-minute standard blood draw at a local clinic
2. Certified temperature-controlled cold logistics
3. High-throughput PBMC & immune cell isolation
4. Controlled-rate freezing to protect cell membranes
5. Decades of secure storage in vapor-phase liquid nitrogen at -196°C

The freezer is not the innovation.
The infrastructure is the innovation.</div>
      <div class="note"><b>Why this works:</b> Appeals to hard-tech investors and engineers who respect execution, scale, and operational moats over hand-waving biology claims.</div>
    </div>
  </article>
</section>

<!-- TAB A9: ANTI-AGING STARTUPS -->
<section class="tab" id="tab-a9" hidden>
  <div class="ahead">
    <span class="k">Angle 9</span>
    <h2>The Longevity Industry Is Trying to Make Old Cells Young. We're Keeping Young Cells.</h2>
    <p class="one">The &quot;competition is cooked&quot; angle: The longevity sector is spending billions trying to reverse damage. Why not prevent it?</p>
    <p class="who"><b>Who to target:</b> Biohackers, longevity VCs, rejuvenation researchers, biotech contrarians.</p>
    <div class="blk">
      <h4>The Tension</h4>
      <p>The entire longevity sector is obsessed with cellular reprogramming (Yamanaka factors, partial reprogramming, epigenetic resetting). While promising (Frontiers in Aging), reversing 70 years of somatic mutations and telomere erosion is extraordinarily hard.</p>
      <p>Reservoir&#x27;s bet: Instead of spending billions asking &quot;How do we make 70-year-old cells act 30?&quot; we asked: <b>&quot;Why not just keep your 30-year-old cells while they are still 30?&quot;</b></p>
    </div>
  </div>

  <article class="post" id="p9-1">
    <div class="pl"><svg class="av" width="40" height="40" viewBox="0 0 40 40"><rect width="40" height="40" rx="20" fill="#00ba7c"/><text x="12" y="26" fill="#fff" font-weight="700" font-size="14">BT</text></svg></div>
    <div class="pr">
      <div class="ph-row"><b>Bio Contrarian</b><span class="h">@biotech_takes</span><span class="dot">·</span><span class="h">1d</span><span class="line">provocation</span></div>
      <div class="txt">Biotech startups are spending tens of billions of dollars trying to turn 75-year-old damaged cells into 30-year-old cells.

Epigenetic resetting.
Yamanaka factor transfection.
Telomerase gene therapies.

It&#x27;s brilliant work.

Meanwhile, @reservoir_bio just asked:

&quot;Why don&#x27;t you just keep your 30-year-old cells while you&#x27;re still 30?&quot;

It takes 15 minutes. It uses proven cryobiology. And you don&#x27;t have to wait for someone to solve cellular reprogramming to know it works.</div>
      <div class="note"><b>Why this works:</b> Extremely shareable contrarian framing. Creates intellectual tension between active rejuvenation and preventive cell preservation.</div>
    </div>
  </article>
</section>

</main>
</div>

<footer class="foot">
  Reservoir Launch Brief • Internal Cultural Narrative Map • Shown Media Writers
</footer>

<script>
(function(){
  var tabs = document.querySelectorAll(".tb");
  var panes = document.querySelectorAll(".tab");
  var sideLinks = document.querySelectorAll(".side a[data-tab]");

  function show(id) {
    tabs.forEach(function(t) {
      t.setAttribute("aria-selected", t.dataset.tab === id ? "true" : "false");
    });
    panes.forEach(function(p) {
      p.hidden = (p.id !== "tab-" + id);
    });
    sideLinks.forEach(function(a) {
      if (a.dataset.tab === id) {
        a.classList.add("active");
      } else {
        a.classList.remove("active");
      }
    });
    try {
      history.replaceState(null, "", "#" + id);
    } catch(e) {}
    window.scrollTo({top: 0});
  }

  tabs.forEach(function(t) {
    t.addEventListener("click", function() {
      show(t.dataset.tab);
    });
  });

  sideLinks.forEach(function(a) {
    a.addEventListener("click", function(e) {
      e.preventDefault();
      show(a.dataset.tab);
    });
  });

  var h = (location.hash || "").replace("#", "");
  show(document.getElementById("tab-" + h) ? h : "intro");
})();
</script>
</body>
</html>
"""

with open("public/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: public/index.html created successfully!")
