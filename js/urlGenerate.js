
function urlGen(f){
   var i1 = 'https://kforney1205.github.io/STS-Provider/glass.html?';
   var i2 = 'conference=stsprov'
   var i3 = document.getElementById('videoID').value;
   f.action = i1 + i2 + i3;
   return true;
}