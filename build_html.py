import json

with open('data.json', encoding='utf-8') as f:
    data = json.load(f)

payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')

HTML = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Meet the AI Residency Builders</title>
<meta name="description" content="IIMA Ventures x entreVC x Prodman. Meet the AI Summer Residency cohort. Find a team, find their room.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{
  --cream:#F5EFE1; --surface:#FFFFFF; --green:#1D3A2A; --green-2:#2C5440;
  --sage:#E6ECDA; --sage-ink:#2E4636; --ink:#23291F; --muted:#6C7A6B;
  --border:#E5DDC8; --red:#D8392B; --shadow:0 6px 24px rgba(29,58,42,.10);
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0; background:var(--cream); color:var(--ink);
  font-family:'Inter',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;
  font-size:16px; line-height:1.55; -webkit-font-smoothing:antialiased;
}
.wrap{max-width:940px; margin:0 auto; padding:22px 16px 56px}
.head-kicker{
  font-family:'Oswald',sans-serif; font-weight:600; letter-spacing:.14em;
  text-transform:uppercase; font-size:12.5px; color:var(--green-2);
  display:flex; flex-wrap:wrap; align-items:center; gap:8px 10px;
}
.head-kicker .dot{width:5px;height:5px;border-radius:50%;background:var(--red);display:inline-block}
h1{
  font-family:'Oswald',sans-serif; font-weight:700; color:var(--green);
  font-size:clamp(34px,9vw,60px); line-height:.98; letter-spacing:-.01em;
  margin:.34em 0 .12em; text-transform:uppercase;
}
.sub{font-size:clamp(16px,4.4vw,20px); font-weight:500; color:var(--green-2); margin:0 0 18px}
.intro{font-size:15.5px; color:var(--ink); max-width:660px; margin:0 0 18px}
.facts{display:flex; flex-wrap:wrap; gap:8px; margin:0 0 10px}
.fact{
  background:var(--surface); border:1px solid var(--border); border-radius:999px;
  padding:7px 14px; font-size:14px; font-weight:500; color:var(--green);
  display:inline-flex; align-items:center; gap:7px; box-shadow:var(--shadow);
}
.fact b{font-weight:600}
.note{font-size:13.5px; color:var(--muted); margin:14px 0 16px; max-width:660px}

.jump-label{font-family:'Oswald',sans-serif; font-weight:600; font-size:11.5px; letter-spacing:.1em; text-transform:uppercase; color:var(--muted); margin:0 0 8px}
.secnav{display:flex; flex-wrap:wrap; gap:8px; margin:0 0 20px}
.pill{
  font-family:'Oswald',sans-serif; font-weight:600; font-size:12.5px; letter-spacing:.03em;
  text-transform:uppercase; color:#fff; background:var(--green); border:none; cursor:pointer;
  border-radius:999px; padding:9px 14px; transition:background .15s;
}
.pill:hover{background:var(--green-2)}
.pill:focus-visible{outline:3px solid rgba(44,84,64,.35); outline-offset:2px}

.search{position:relative; margin:0 0 26px}
.search input{
  width:100%; padding:13px 16px 13px 42px; font-size:16px; font-family:inherit;
  border:1px solid var(--border); border-radius:12px; background:var(--surface);
  color:var(--ink); box-shadow:var(--shadow);
}
.search input:focus{outline:none; border-color:var(--green-2); box-shadow:0 0 0 3px rgba(44,84,64,.15)}
.search svg{position:absolute; left:14px; top:50%; transform:translateY(-50%); color:var(--muted)}

.group{margin:0 0 24px; scroll-margin-top:14px}
.group-h{
  font-family:'Oswald',sans-serif; font-weight:600; text-transform:uppercase;
  letter-spacing:.05em; font-size:15px; color:var(--green);
  display:flex; align-items:center; gap:10px; margin:0 0 10px; padding-bottom:7px;
  border-bottom:2px solid var(--green);
}
.group-h .count{
  font-family:'Inter'; font-weight:600; font-size:12px; color:var(--green-2);
  background:var(--sage); border-radius:999px; padding:2px 9px; letter-spacing:0; text-transform:none;
}

.thead{
  display:grid; grid-template-columns:62px minmax(0,1.45fr) minmax(0,1.55fr) 116px;
  gap:14px; padding:0 16px 8px; font-family:'Oswald',sans-serif; font-weight:600;
  font-size:12px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted);
}
.rows{display:flex; flex-direction:column; gap:8px}
.row{
  display:grid; grid-template-columns:62px minmax(0,1.45fr) minmax(0,1.55fr) 116px;
  gap:16px; align-items:center; background:var(--surface); border:1px solid var(--border);
  border-radius:12px; padding:12px 16px; box-shadow:var(--shadow);
}
.room{
  font-family:'Oswald',sans-serif; font-weight:700; font-size:15px; color:var(--green);
  background:var(--sage); border-radius:10px; text-align:center; padding:8px 4px;
  min-width:0; white-space:nowrap;
}
.room.tba{color:var(--muted); font-weight:600; font-size:12px; letter-spacing:.06em}
.team .name{font-family:'Oswald',sans-serif; font-weight:600; font-size:18px; color:var(--green); line-height:1.12}
.team .ppl{font-size:13.5px; color:var(--muted); margin-top:2px}
.chips{display:flex; flex-wrap:wrap; gap:6px}
.chip{background:var(--sage); color:var(--sage-ink); font-size:12.5px; font-weight:500; padding:4px 10px; border-radius:999px; white-space:nowrap}
.btn{
  font-family:'Oswald',sans-serif; font-weight:600; letter-spacing:.03em; font-size:13.5px;
  text-transform:uppercase; color:#fff; background:var(--green); border:none; cursor:pointer;
  border-radius:10px; padding:11px 12px; width:100%; transition:background .15s;
}
.btn:hover{background:var(--green-2)}
.btn:focus-visible{outline:3px solid rgba(44,84,64,.35); outline-offset:2px}
.cell-label{display:none}
.empty{display:none; text-align:center; color:var(--muted); padding:40px 0; font-size:15px}

/* Modal */
.overlay{
  position:fixed; inset:0; background:rgba(20,33,26,.55); backdrop-filter:blur(2px);
  display:none; align-items:flex-end; justify-content:center; z-index:50; padding:0;
}
.overlay.open{display:flex}
.modal{
  background:var(--cream); width:100%; max-width:640px; max-height:92vh; overflow:hidden;
  border-radius:20px 20px 0 0; display:flex; flex-direction:column; box-shadow:0 -8px 40px rgba(0,0,0,.25);
}
.modal-top{
  display:flex; align-items:flex-start; gap:12px; padding:20px 20px 14px;
  border-bottom:1px solid var(--border); background:var(--surface);
}
.modal-top .m-room{
  font-family:'Oswald',sans-serif; font-weight:700; font-size:13px; color:var(--green);
  background:var(--sage); border-radius:8px; padding:6px 11px; white-space:nowrap;
}
.modal-top .m-room.tba{color:var(--muted); font-weight:600}
.m-titles{flex:1; min-width:0}
.m-titles .m-sector{font-family:'Oswald',sans-serif; font-weight:600; font-size:11.5px; letter-spacing:.1em; text-transform:uppercase; color:var(--green-2)}
.m-titles .m-name{font-family:'Oswald',sans-serif; font-weight:700; font-size:24px; color:var(--green); line-height:1.05; margin:2px 0}
.m-titles .m-ppl{font-size:14px; color:var(--muted)}
.m-links{display:flex; flex-wrap:wrap; gap:8px; margin-top:10px}
.m-link{
  display:inline-flex; align-items:center; gap:6px; font-size:13px; font-weight:600;
  color:var(--green); background:var(--sage); border-radius:999px; padding:6px 12px;
  text-decoration:none;
}
.m-link:hover{background:#d9e2ca}
.m-link svg{width:14px; height:14px}
.x{
  border:none; background:var(--sage); color:var(--green); width:38px; height:38px; flex:none;
  border-radius:50%; font-size:20px; cursor:pointer; line-height:1; display:flex; align-items:center; justify-content:center;
}
.x:hover{background:#d9e2ca}
.modal-body{padding:20px; overflow-y:auto; -webkit-overflow-scrolling:touch}
.m-h{font-family:'Oswald',sans-serif; font-weight:600; text-transform:uppercase; letter-spacing:.06em; font-size:13px; color:var(--green); margin:0 0 6px}
.m-h.sol{margin-top:22px}
.m-text{font-size:15px; color:var(--ink); white-space:pre-line; margin:0}
.m-text.none{color:var(--muted); font-style:italic; white-space:normal}
.modal-nav{
  display:flex; gap:10px; padding:14px 20px calc(16px + env(safe-area-inset-bottom));
  border-top:1px solid var(--border); background:var(--surface);
}
.nav-btn{
  flex:1; font-family:'Oswald',sans-serif; font-weight:600; text-transform:uppercase; font-size:13px;
  letter-spacing:.04em; padding:12px; border-radius:10px; border:1px solid var(--border);
  background:var(--cream); color:var(--green); cursor:pointer; display:flex; align-items:center; justify-content:center; gap:6px;
}
.nav-btn:hover{background:var(--sage)}

@media (min-width:560px){
  .overlay{align-items:center; padding:24px}
  .modal{border-radius:20px}
}
@media (max-width:640px){
  .thead{display:none}
  .row{grid-template-columns:1fr; gap:11px; padding:15px 16px}
  .room{justify-self:start; padding:6px 14px; min-width:64px}
  .room.tba{padding:6px 12px}
  .cell-label{display:block; font-family:'Oswald',sans-serif; font-weight:600; font-size:10.5px; letter-spacing:.09em; text-transform:uppercase; color:var(--muted); margin-bottom:5px}
  .btn{width:100%}
  .c-room{order:1} .c-team{order:2} .c-prob{order:3} .c-btn{order:4}
}
.foot{text-align:center; color:var(--muted); font-size:13px; margin-top:36px; line-height:1.6}
.foot a{color:var(--green-2)}
</style>
</head>
<body>
<div class="wrap">
  <div class="head-kicker">
    <span>IIMA Ventures</span><span class="dot"></span><span>entreVC</span><span class="dot"></span><span>Prodman</span>
  </div>
  <h1>Meet the AI<br>Residency Builders</h1>
  <p class="sub">An evening of ideas, feedback and conversations.</p>
  <p class="intro">The AI Summer Residency brought together 40 builders who spent eight weeks on campus turning ideas into real, working AI products, and a few have already closed their first customer deals. Find a team, see what they built, then head to their room to say hi.</p>
  <div class="facts">
    <span class="fact">📅 <b>27 June, Saturday</b></span>
    <span class="fact">⏰ <b>6:00 PM – 9:00 PM</b></span>
    <span class="fact">📍 <b>IIMA Ventures</b></span>
  </div>
  <p class="note">Tap <b>Read more</b> on any team to read their full problem and solution. Room numbers will be filled in shortly, so check back to find where each team is set up.</p>

  <p class="jump-label">Jump to a sector</p>
  <nav class="secnav" id="secnav" aria-label="Jump to sector"></nav>

  <div class="search">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
    <input id="q" type="search" placeholder="Search team, person, or sector" autocomplete="off" aria-label="Search teams">
  </div>

  <main id="list"></main>
  <p class="empty" id="empty">No teams match that search.</p>

  <p class="foot">IIMA Ventures &times; entreVC &times; Prodman<br>Questions? Reach out to Pradyuman Agrawal &middot; +91 83172 99236</p>
</div>

<div class="overlay" id="overlay" role="dialog" aria-modal="true" aria-labelledby="m-name">
  <div class="modal">
    <div class="modal-top">
      <span class="m-room" id="m-room"></span>
      <div class="m-titles">
        <div class="m-sector" id="m-sector"></div>
        <div class="m-name" id="m-name"></div>
        <div class="m-ppl" id="m-ppl"></div>
        <div class="m-links" id="m-links"></div>
      </div>
      <button class="x" id="x" aria-label="Close">&times;</button>
    </div>
    <div class="modal-body">
      <div class="m-h">The problem</div>
      <p class="m-text" id="m-prob"></p>
      <div class="m-h sol" id="m-sol-h">The solution</div>
      <p class="m-text" id="m-sol"></p>
    </div>
    <div class="modal-nav">
      <button class="nav-btn" id="prev">&#8249;&nbsp; Previous</button>
      <button class="nav-btn" id="next">Next &nbsp;&#8250;</button>
    </div>
  </div>
</div>

<script id="data" type="application/json">__DATA__</script>
<script>
(function(){
  var DATA = JSON.parse(document.getElementById('data').textContent);
  var teams = DATA.teams, order = DATA.groupOrder;
  teams.forEach(function(t,i){ t._i = i; });

  var list = document.getElementById('list');
  var secnav = document.getElementById('secnav');
  function esc(s){ return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
  function slug(s){ return 'sec-' + s.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,''); }

  order.forEach(function(g){
    var items = teams.filter(function(t){ return t.sector === g; });
    if(!items.length) return;
    var id = slug(g);
    var pill = document.createElement('button');
    pill.className = 'pill';
    pill.type = 'button';
    pill.textContent = g;
    pill.addEventListener('click', function(){
      var target = document.getElementById(id);
      if(target) target.scrollIntoView({behavior:'smooth', block:'start'});
    });
    secnav.appendChild(pill);

    var sec = document.createElement('section');
    sec.className = 'group';
    sec.id = id;
    sec.dataset.group = g;
    var h = '<div class="group-h">'+esc(g)+'<span class="count">'+items.length+'</span></div>';
    h += '<div class="thead"><div>Room</div><div>Team</div><div>Problem area</div><div></div></div>';
    h += '<div class="rows">';
    items.forEach(function(t){
      var title = t.startup || t.members;
      var roomCls = t.room ? 'room' : 'room tba';
      var roomTxt = t.room ? esc(t.room) : 'TBA';
      var chips = t.keywords.map(function(k){ return '<span class="chip">'+esc(k)+'</span>'; }).join('');
      h += '<div class="row" data-i="'+t._i+'" data-search="'+esc((title+' '+t.members+' '+t.sector+' '+t.keywords.join(' ')).toLowerCase())+'">'
        +   '<div class="c-room"><span class="cell-label">Room</span><span class="'+roomCls+'">'+roomTxt+'</span></div>'
        +   '<div class="c-team team"><div class="name">'+esc(title)+'</div><div class="ppl">'+esc(t.members)+'</div></div>'
        +   '<div class="c-prob"><span class="cell-label">Problem area</span><div class="chips">'+chips+'</div></div>'
        +   '<div class="c-btn"><button class="btn" data-open="'+t._i+'">Read more</button></div>'
        + '</div>';
    });
    h += '</div>';
    sec.innerHTML = h;
    list.appendChild(sec);
  });

  // Modal
  var overlay = document.getElementById('overlay');
  var cur = -1, lastFocus = null;
  var el = {
    room: document.getElementById('m-room'), sector: document.getElementById('m-sector'),
    name: document.getElementById('m-name'), ppl: document.getElementById('m-ppl'),
    prob: document.getElementById('m-prob'), sol: document.getElementById('m-sol'),
    solH: document.getElementById('m-sol-h'), links: document.getElementById('m-links')
  };
  var globeSvg = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 2.5 15 0 18M12 3c-2.5 2.5-2.5 15 0 18"/></svg>';
  var xSvg = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.9 2H22l-7.2 8.2L23 22h-6.6l-5.2-6.8L5.3 22H2.2l7.7-8.8L1.5 2h6.8l4.7 6.2L18.9 2Zm-1.2 18h1.8L7.4 3.9H5.5L17.7 20Z"/></svg>';
  function render(i){
    var t = teams[i]; if(!t) return;
    cur = i;
    el.room.textContent = t.room || 'TBA';
    el.room.className = t.room ? 'm-room' : 'm-room tba';
    el.sector.textContent = t.sector;
    el.name.textContent = t.startup || t.members;
    el.ppl.textContent = t.members;
    var lk = '';
    if(t.website) lk += '<a class="m-link" href="'+esc(t.website)+'" target="_blank" rel="noopener">'+globeSvg+'Website</a>';
    if(t.x) lk += '<a class="m-link" href="'+esc(t.x)+'" target="_blank" rel="noopener">'+xSvg+'X</a>';
    el.links.innerHTML = lk;
    el.links.style.display = lk ? 'flex' : 'none';
    el.prob.textContent = t.problem || 'Coming soon.';
    el.prob.className = t.problem ? 'm-text' : 'm-text none';
    if(t.solution){ el.sol.textContent = t.solution; el.sol.className='m-text'; el.solH.style.display=''; el.sol.style.display=''; }
    else { el.solH.style.display='none'; el.sol.style.display='none'; }
    document.querySelector('.modal-body').scrollTop = 0;
  }
  function open(i){ lastFocus = document.activeElement; render(i); overlay.classList.add('open'); document.body.style.overflow='hidden'; document.getElementById('x').focus(); }
  function close(){ overlay.classList.remove('open'); document.body.style.overflow=''; if(lastFocus) lastFocus.focus(); }
  function step(d){ var n = (cur + d + teams.length) % teams.length; render(n); }

  document.addEventListener('click', function(e){
    var b = e.target.closest('[data-open]');
    if(b){ open(+b.getAttribute('data-open')); }
  });
  document.getElementById('x').addEventListener('click', close);
  document.getElementById('prev').addEventListener('click', function(){ step(-1); });
  document.getElementById('next').addEventListener('click', function(){ step(1); });
  overlay.addEventListener('click', function(e){ if(e.target === overlay) close(); });
  document.addEventListener('keydown', function(e){
    if(!overlay.classList.contains('open')) return;
    if(e.key === 'Escape') close();
    else if(e.key === 'ArrowLeft') step(-1);
    else if(e.key === 'ArrowRight') step(1);
  });

  // Search
  var q = document.getElementById('q'), empty = document.getElementById('empty');
  q.addEventListener('input', function(){
    var v = q.value.trim().toLowerCase();
    var any = false;
    document.querySelectorAll('.group').forEach(function(sec){
      var shown = 0;
      sec.querySelectorAll('.row').forEach(function(r){
        var match = !v || r.dataset.search.indexOf(v) !== -1;
        r.style.display = match ? '' : 'none';
        if(match) shown++;
      });
      sec.style.display = shown ? '' : 'none';
      if(shown) any = true;
    });
    empty.style.display = any ? 'none' : 'block';
  });
})();
</script>
</body>
</html>
'''

HTML = HTML.replace('__DATA__', payload)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(HTML)
print('wrote index.html', len(HTML), 'bytes')
