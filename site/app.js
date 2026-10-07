document.addEventListener('DOMContentLoaded', () => {
  if (window.renderMathInElement) renderMathInElement(document.querySelector('main'), {
    delimiters: [{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],
    throwOnError:false
  });
  const search=document.querySelector('#search');
  if (!search) return;
  const area=document.querySelector('#area');
  const status=document.querySelector('#research-status');
  const cards=[...document.querySelectorAll('.card')];
  const groups=[...document.querySelectorAll('.area-group')];
  function filter() {
    const words=search.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let visible=0;
    cards.forEach(card => {
      card.hidden=!(words.every(word=>card.dataset.search.includes(word)) && (!area.value || card.dataset.area===area.value) && (!status.value || card.dataset.status===status.value));
      if(!card.hidden) visible++;
    });
    groups.forEach(group => {
      const count=[...group.querySelectorAll('.card')].filter(card=>!card.hidden).length;
      group.hidden=count===0;
      group.querySelector('.area-count').textContent=`${count} problem${count === 1 ? "" : "s"}`;
    });
    document.querySelector('#count').textContent=`${visible} problem${visible === 1 ? "" : "s"}`;
    document.querySelector('#empty').hidden=visible>0;
  }
  search.addEventListener('input',filter);
  area.addEventListener('change',filter);
  status.addEventListener('change',filter);
});
