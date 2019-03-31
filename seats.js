x = document.getElementsByTagName('a')
available = 0;
blocked = 0;
for (i = 0; i < x.length; i++) {
  if(x[i].classList.contains('_available')) {
  	available++;
  	
  }
  if(x[i].classList.contains('_blocked')) {
    blocked++;

  }
}
console.log("Available: " + available);
console.log("Blocked: " + blocked);