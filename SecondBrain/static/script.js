
// Mobile nav
document.querySelectorAll('.menu-toggle').forEach(b=>{
  b.addEventListener('click',()=>document.querySelector('.nav-links').classList.toggle('open'));
});

// Filter tabs (events)
document.querySelectorAll('.filter-tabs').forEach(group=>{
  group.querySelectorAll('button').forEach(btn=>{
    btn.addEventListener('click',()=>{
      group.querySelectorAll('button').forEach(b=>b.classList.remove('active'));
      btn.classList.add('active');
      const f=btn.dataset.filter;
      document.querySelectorAll('[data-cat]').forEach(c=>{
        c.style.display=(f==='all'||c.dataset.cat===f)?'':'none';
      });
    });
  });
});

// Scroll reveal
const io=new IntersectionObserver((es)=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

// Form
document.querySelectorAll('form').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();alert('Thank you! We will be in touch.');f.reset()}));

// Play video stub
document.querySelectorAll('.play-circle').forEach(p=>p.addEventListener('click',()=>alert('Video preview coming soon!')));
