let threshold = 50;     // required min distance traveled to be considered swipe
let restraint = 45;     // maximum distance allowed at the same time in perpendicular direction
let allowedTime = 300;  // maximum time allowed to travel that distance

// credit: http://www.javascriptkit.com/javatutors/touchevents2.shtml
function swipedetect(touchsurface, callback) {

  let swipedir = undefined;
  let startX = undefined;
  let startY = undefined;
  let distX = undefined;
  let distY = undefined;
  let elapsedTime = undefined;
  let startTime = undefined;
  let handleswipe = callback || function(swipedir){};

  touchsurface.addEventListener('touchstart', function(e) {
    let touchobj = e.changedTouches[0];
    swipedir = -1;
    startX = touchobj.pageX;
    startY = touchobj.pageY;
    startTime = new Date().getTime();  // record time when finger first makes contact with surface
    e.preventDefault();
  }, false);

  touchsurface.addEventListener('touchmove', function(e) {
    e.preventDefault();  // prevent scrolling when inside DIV
  }, false);

  touchsurface.addEventListener('touchend', function(e) {
    let touchobj = e.changedTouches[0];
    distX = touchobj.pageX - startX;  // get horizontal dist traveled by finger while in contact with surface
    distY = touchobj.pageY - startY;  // get vertical dist traveled by finger while in contact with surface
    elapsedTime = new Date().getTime() - startTime;  // get time elapsed
    if (elapsedTime <= allowedTime) {  // first condition for swipe met
      if (Math.abs(distX) >= threshold && Math.abs(distY) <= restraint) {  // 2nd condition for horizontal swipe met
        swipedir = (distX < 0)? 0 : 2;  // if dist traveled is negative, it indicates left swipe
      }
      else if (Math.abs(distY) >= threshold && Math.abs(distX) <= restraint) {  // 2nd condition for vertical swipe met
        swipedir = (distY < 0)? 1 : 3;  // if dist traveled is negative, it indicates up swipe
      }
    }
    handleswipe(swipedir);
    e.preventDefault();
  }, false)
}
